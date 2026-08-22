import json
from pathlib import Path

import pytest

from project_tools.shared.setup_structure.loader import (
    ProjectDataError,
    ProjectNotFoundError,
    load_project,
    load_projects,
)


def test_load_projects(tmp_path: Path) -> None:
    data_path = tmp_path / "projects.json"

    data_path.write_text(
        json.dumps(
            {
                "projects": {
                    "example": {
                        "path": "/tmp/example",
                        "folders": ["src", "tests"],
                        "files": ["README.md", "src/main.py"],
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    projects = load_projects(data_path)

    assert projects["example"].name == "example"
    assert projects["example"].path == "/tmp/example"
    assert projects["example"].folders == ["src", "tests"]
    assert projects["example"].files == [
        "README.md",
        "src/main.py",
    ]


def test_load_project(tmp_path: Path) -> None:
    data_path = tmp_path / "projects.json"

    data_path.write_text(
        json.dumps(
            {
                "projects": {
                    "example": {
                        "path": "/tmp/example",
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    project = load_project(data_path, "example")

    assert project.name == "example"
    assert project.folders == []
    assert project.files == []


def test_load_project_raises_for_unknown_project(tmp_path: Path) -> None:
    data_path = tmp_path / "projects.json"

    data_path.write_text(
        json.dumps({"projects": {}}),
        encoding="utf-8",
    )

    with pytest.raises(ProjectNotFoundError):
        load_project(data_path, "missing")


def test_load_project_rejects_invalid_path(tmp_path: Path) -> None:
    data_path = tmp_path / "projects.json"

    data_path.write_text(
        json.dumps(
            {
                "projects": {
                    "example": {
                        "path": 123,
                    }
                }
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(ProjectDataError):
        load_project(data_path, "example")