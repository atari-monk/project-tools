from pathlib import Path

from project_tools.shared.setup_structure.model import Project
from project_tools.shared.setup_structure.creator import create_structure


def test_create_structure(tmp_path: Path):
    project = Project(
        name="example",
        path=str(tmp_path / "project"),
        folders=[
            "src",
            "tests",
            "src/utils",
        ],
        files=[
            "README.md",
            "src/main.py",
            "src/utils/helpers.py",
            "tests/test_main.py",
        ],
    )

    create_structure(project)

    project_path = Path(project.path)

    assert (project_path / "src").is_dir()
    assert (project_path / "tests").is_dir()
    assert (project_path / "src/utils").is_dir()

    assert (project_path / "README.md").is_file()
    assert (project_path / "src/main.py").is_file()
    assert (project_path / "src/utils/helpers.py").is_file()
    assert (project_path / "tests/test_main.py").is_file()


def test_create_structure_does_not_overwrite_existing_file(tmp_path: Path):
    file_path = tmp_path / "project" / "README.md"
    file_path.parent.mkdir(parents=True)

    file_path.write_text("existing content", encoding="utf-8")

    project = Project(
        name="example",
        path=str(tmp_path / "project"),
        files=["README.md"],
    )

    create_structure(project)

    assert file_path.read_text(encoding="utf-8") == "existing content"