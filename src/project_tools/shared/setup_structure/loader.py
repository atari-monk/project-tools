import json
from pathlib import Path
from typing import TypeGuard, cast

from .model import Project


class ProjectNotFoundError(ValueError):
    """Raised when a requested project does not exist."""


class ProjectDataError(ValueError):
    """Raised when project data has an invalid structure."""


ProjectJson = dict[str, object]


def load_projects(data_path: Path) -> dict[str, Project]:
    """Load all projects from a JSON data file."""

    with data_path.open("r", encoding="utf-8") as file:
        raw_data: object = json.load(file)

    if not _is_string_object(raw_data):
        raise ProjectDataError("Project data must be a JSON object.")

    projects_data = raw_data.get("projects", {})

    if not _is_string_object(projects_data):
        raise ProjectDataError("'projects' must be an object.")

    projects: dict[str, Project] = {}

    for name, project_data in projects_data.items():
        if not _is_project_data(project_data):
            raise ProjectDataError(
                f"Project '{name}' has an invalid project structure."
            )

        projects[name] = _load_project(name, project_data)

    return projects


def load_project(data_path: Path, name: str) -> Project:
    """Load a single project by name."""

    projects = load_projects(data_path)

    try:
        return projects[name]
    except KeyError as exc:
        raise ProjectNotFoundError(
            f"Project '{name}' was not found in {data_path}."
        ) from exc


def _load_project(name: str, data: ProjectJson) -> Project:
    path = data.get("path")
    folders = data.get("folders", [])
    files = data.get("files", [])

    if not isinstance(path, str) or not path:
        raise ProjectDataError(
            f"Project '{name}' must have a non-empty string 'path'."
        )

    if not _is_string_list(folders):
        raise ProjectDataError(
            f"Project '{name}' has invalid 'folders'."
        )

    if not _is_string_list(files):
        raise ProjectDataError(
            f"Project '{name}' has invalid 'files'."
        )

    return Project(
        name=name,
        path=path,
        folders=folders,
        files=files,
    )


def _is_project_data(value: object) -> TypeGuard[ProjectJson]:
    """Check whether a value has the expected project structure."""

    if not _is_string_object(value):
        return False

    path = value.get("path")
    folders = value.get("folders", [])
    files = value.get("files", [])

    return (
        isinstance(path, str)
        and bool(path)
        and _is_string_list(folders)
        and _is_string_list(files)
    )


def _is_string_object(value: object) -> TypeGuard[dict[str, object]]:
    """Check whether a value is a JSON object with string keys."""

    if not isinstance(value, dict):
        return False

    typed_value = cast(dict[object, object], value)

    return all(isinstance(key, str) for key in typed_value)


def _is_string_list(value: object) -> TypeGuard[list[str]]:
    """Check whether a value is a non-empty-string list."""

    if not isinstance(value, list):
        return False

    typed_value = cast(list[object], value)

    return all(
        isinstance(item, str) and bool(item)
        for item in typed_value
    )