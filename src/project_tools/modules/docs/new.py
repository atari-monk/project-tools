import re
import shutil
import subprocess
from pathlib import Path


_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def read_clipboard() -> str:
    """Read text from the system clipboard."""
    if shutil.which("wl-paste"):
        result = subprocess.run(
            ["wl-paste", "--no-newline"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout

    if shutil.which("xclip"):
        result = subprocess.run(
            ["xclip", "-selection", "clipboard", "-o"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout

    if shutil.which("xsel"):
        result = subprocess.run(
            ["xsel", "--clipboard", "--output"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout

    raise RuntimeError(
        "No clipboard utility found. Install wl-clipboard, xclip, or xsel."
    )


def validate_name(name: str) -> None:
    """Validate that a document name is kebab-case."""
    if not _NAME_PATTERN.fullmatch(name):
        raise ValueError(
            "Document name must be kebab-case using lowercase letters, "
            "numbers, and hyphens."
        )


def validate_category(category: str) -> None:
    """Validate that category is a relative path."""
    category_path = Path(category)

    if category_path.is_absolute() or ".." in category_path.parts:
        raise ValueError("Category must be a relative path.")


def create_doc(
    docs_path: Path,
    category: str,
    name: str,
    content: str | None = None,
) -> Path:
    """Create a new markdown document from clipboard content."""
    validate_name(name)
    validate_category(category)

    doc_path = docs_path / category / f"{name}.md"

    if doc_path.exists():
        raise FileExistsError(f"Document already exists: {doc_path}")

    if content is None:
        content = read_clipboard()

    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(content, encoding="utf-8")

    return doc_path