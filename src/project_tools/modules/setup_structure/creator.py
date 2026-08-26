from pathlib import Path

from .model import Project


def create_structure(project: Project) -> None:
    """Create the directory and file structure described by a project."""

    project_path = Path(project.path)
    project_path.mkdir(parents=True, exist_ok=True)

    for folder in project.folders:
        _create_folder(project_path, folder)

    for file in project.files:
        _create_file(project_path, file)


def _create_folder(project_path: Path, folder: str) -> None:
    folder_path = project_path / folder
    folder_path.mkdir(parents=True, exist_ok=True)


def _create_file(project_path: Path, file: str) -> None:
    file_path = project_path / file

    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Do not overwrite existing files.
    file_path.touch(exist_ok=True)