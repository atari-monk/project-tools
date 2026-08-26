from pathlib import Path

from project_tools.modules.docs_index.docs_index_render import build_docs_index


def generate_docs_index(docs_path: Path) -> None:
    """Generate docs/index.md from the existing docs/order.txt."""
    order_path = docs_path / "order.txt"
    index_path = docs_path / "index.md"

    ordered_paths = _read_order_file(order_path)

    content = build_docs_index(ordered_paths)

    index_path.write_text(content, encoding="utf-8")


def _read_order_file(order_path: Path) -> list[str]:
    """Read and validate documentation paths from order.txt."""
    content = order_path.read_text(encoding="utf-8")

    paths: list[str] = []

    for line in content.splitlines():
        entry = line.strip()

        if not entry:
            continue

        normalized = _normalize_order_entry(entry)

        if normalized is None:
            continue

        paths.append(normalized)

    return paths


def _normalize_order_entry(entry: str) -> str | None:
    """Return a safe docs-relative markdown path or None."""
    normalized = entry.replace("\\", "/")

    if normalized.startswith("/"):
        return None

    parts = normalized.split("/")

    if any(part in ("", ".", "..") for part in parts):
        return None

    if not normalized.endswith(".md"):
        return None

    if parts[-1] == "index.md":
        return None

    if any(part.startswith("_") or part.startswith(".") for part in parts):
        return None

    return normalized