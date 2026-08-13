from pathlib import Path


def update_order_file(
    docs_path: Path,
    discovered_paths: list[str],
) -> list[str]:
    """Update docs/order.txt and return its resulting entries."""
    order_path = docs_path / "order.txt"

    existing_paths = _read_order_file(order_path) if order_path.exists() else []

    discovered_set = set(discovered_paths)

    preserved_paths = [
        path
        for path in existing_paths
        if path in discovered_set
    ]

    preserved_set = set(preserved_paths)

    new_paths = [
        path
        for path in discovered_paths
        if path not in preserved_set
    ]

    result = preserved_paths + new_paths

    _write_order_file(order_path, result)

    return result


def _read_order_file(order_path: Path) -> list[str]:
    """Read and normalize order.txt entries."""
    content = order_path.read_text(encoding="utf-8")

    result: list[str] = []

    for line in content.splitlines():
        entry = line.strip()

        if not entry:
            continue

        normalized = _normalize_order_entry(entry)

        if normalized is None:
            continue

        if normalized not in result:
            result.append(normalized)

    return result


def _normalize_order_entry(entry: str) -> str | None:
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


def _write_order_file(order_path: Path, paths: list[str]) -> None:
    """Write order.txt without introducing blank lines."""
    content = "".join(f"{path}\n" for path in paths)
    order_path.write_text(content, encoding="utf-8")