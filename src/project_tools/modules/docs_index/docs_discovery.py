from pathlib import Path


def discover_documentation_files(docs_path: Path) -> list[str]:
    """Discover all eligible markdown files below docs_path.

    Returned paths are relative to docs_path and always use '/' separators.
    """
    if not docs_path.exists():
        return []

    if not docs_path.is_dir():
        raise NotADirectoryError(docs_path)

    discovered: list[str] = []

    for path in docs_path.rglob("*"):
        if not path.is_file():
            continue

        relative_path = path.relative_to(docs_path)

        if not _is_eligible_path(relative_path):
            continue

        discovered.append(relative_path.as_posix())

    discovered.sort()
    return discovered


def _is_eligible_path(relative_path: Path) -> bool:
    """Return whether a relative path is an indexable documentation file."""
    if relative_path.suffix != ".md":
        return False

    if relative_path.name == "index.md":
        return False

    return all(not part.startswith("_") for part in relative_path.parts)