from pathlib import Path
from typing import TypedDict


from project_tools.modules.docs.discovery import (
    discover_documentation_files,
)


class DocsCategory(TypedDict):
    name: str
    path: str
    files: list[str]
    children: list["DocsCategory"]


def scan_docs(path: Path) -> list[DocsCategory]:
    """Scan documentation files and build a category tree."""
    if not path.exists():
        return []

    if not path.is_dir():
        raise NotADirectoryError(path)

    discovered = discover_documentation_files(path)

    categories: list[DocsCategory] = []

    for relative_path in discovered:
        relative = Path(relative_path)

        if len(relative.parts) < 2:
            continue

        _add_path(categories, relative_path)

    return categories


def _add_path(
    categories: list[DocsCategory],
    file_path: str,
) -> None:
    """Add a documentation file to the category tree."""
    parts = Path(file_path).parts
    directories = parts[:-1]

    current_categories: list[DocsCategory] = categories
    current_path = Path()
    leaf: DocsCategory | None = None

    for directory in directories:
        current_path /= directory

        category = _find_category(
            current_categories,
            directory,
        )

        if category is None:
            category = DocsCategory(
                name=directory,
                path=current_path.as_posix(),
                files=[],
                children=[],
            )
            current_categories.append(category)

        leaf = category
        current_categories = category["children"]

    if leaf is not None:
        leaf["files"].append(file_path)


def _find_category(
    categories: list[DocsCategory],
    name: str,
) -> DocsCategory | None:
    """Find a category by name."""
    for category in categories:
        if category["name"] == name:
            return category

    return None


def print_docs(data: list[DocsCategory]) -> str:
    """Render documentation categories for console output."""
    lines: list[str] = []

    _render_categories(lines, data, level=0)

    return "\n".join(lines).rstrip()


def _render_categories(
    lines: list[str],
    categories: list[DocsCategory],
    level: int,
) -> None:
    """Render documentation categories recursively."""
    indent = "  " * level

    for category in categories:
        lines.append(
            f"{indent}{_title_case(category['name'])}"
        )

        for file_path in category["files"]:
            file_name = Path(file_path).name.removesuffix(".md")

            lines.append(
                f"{indent}  - {_title_case(file_name)}"
            )

        _render_categories(
            lines,
            category["children"],
            level + 1,
        )


def _title_case(value: str) -> str:
    """Convert kebab-case names to title case."""
    return " ".join(
        part[:1].upper() + part[1:]
        for part in value.split("-")
    )