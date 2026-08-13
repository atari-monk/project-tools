from pathlib import Path
from typing import TypedDict


class _Section(TypedDict):
    directory: str
    files: list[str]
    children: list["_Section"]


def build_docs_index(paths: list[str]) -> str:
    """Build the complete contents of docs/index.md."""
    root_files: list[str] = []
    sections: list[_Section] = []

    for path in paths:
        relative_path = Path(path)

        if len(relative_path.parts) == 1:
            root_files.append(path)
            continue

        _add_path(sections, path)

    lines: list[str] = [
        "## Documentation Index",
        "",
    ]

    for path in root_files:
        lines.append(_format_entry(path))

    if root_files and sections:
        lines.append("")

    _render_sections(lines, sections, level=3)

    return "\n".join(lines).rstrip() + "\n"


def _add_path(
    sections: list[_Section],
    path: str,
) -> None:
    """Add a documentation path to the section tree."""
    parts = Path(path).parts
    directory_parts = parts[:-1]

    current_sections = sections

    for index, directory in enumerate(directory_parts):
        section = _find_section(current_sections, directory)

        if section is None:
            section = _create_section(directory)
            current_sections.append(section)

        if index == len(directory_parts) - 1:
            section["files"].append(path)

        current_sections = section["children"]


def _create_section(directory: str) -> _Section:
    """Create an empty documentation section."""
    return {
        "directory": directory,
        "files": [],
        "children": [],
    }


def _find_section(
    sections: list[_Section],
    directory: str,
) -> _Section | None:
    """Find a section by its directory name."""
    for section in sections:
        if section["directory"] == directory:
            return section

    return None


def _render_sections(
    lines: list[str],
    sections: list[_Section],
    level: int,
) -> None:
    """Render documentation sections recursively."""
    for index, section in enumerate(sections):
        lines.append(
            f'{"#" * level} {_title_case(section["directory"])}'
        )
        lines.append("")

        for path in section["files"]:
            lines.append(_format_entry(path))

        if section["files"] and section["children"]:
            lines.append("")

        _render_sections(
            lines,
            section["children"],
            level + 1,
        )

        if index < len(sections) - 1:
            lines.append("")


def _format_entry(path: str) -> str:
    """Format a documentation path as an index entry."""
    file_name = Path(path).name.removesuffix(".md")

    return f"* [{_title_case(file_name)}]({path})"


def _title_case(value: str) -> str:
    """Convert kebab-case names to title case."""
    return " ".join(
        part[:1].upper() + part[1:]
        for part in value.split("-")
    )
