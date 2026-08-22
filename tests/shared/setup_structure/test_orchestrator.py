from pathlib import Path

import pytest

from project_tools.shared.setup_structure import orchestrator


class TestLogger:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def info(self, message: str, *args: object) -> None:
        self.messages.append(message % args)


def test_create_project(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    data_path = tmp_path / "projects.json"

    data_path.write_text(
        """
        {
          "projects": {
            "example": {
              "path": "PROJECT_PATH",
              "folders": ["src"],
              "files": ["README.md", "src/main.py"]
            }
          }
        }
        """.replace("PROJECT_PATH", str(tmp_path / "project")),
        encoding="utf-8",
    )

    monkeypatch.setattr(orchestrator, "DATA_PATH", data_path)

    logger = TestLogger()

    orchestrator.create_project_test("example", logger)

    project_path = tmp_path / "project"

    assert project_path.is_dir()
    assert (project_path / "src").is_dir()
    assert (project_path / "README.md").is_file()
    assert (project_path / "src/main.py").is_file()

    assert logger.messages
    assert any("Creating project" in message for message in logger.messages)