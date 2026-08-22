from logging import Logger
from pathlib import Path
from typing import Protocol

from .creator import create_structure
from .loader import load_project


class TestLogger(Protocol):
    def info(self, message: str, *args: object) -> None:
        ...


DATA_PATH = (
    Path(__file__).resolve().parents[4]
    / "data"
    / "projects.json"
)


def create_project(name: str, logger: Logger) -> None:
    """Create the project structure identified by name."""

    logger.info("Loading project '%s'.", name)

    project = load_project(DATA_PATH, name)

    logger.info(
        "Creating project '%s' at '%s'.",
        project.name,
        project.path,
    )

    create_structure(project)

    logger.info("Project '%s' created.", project.name)


def create_project_test(name: str, logger: TestLogger) -> None:
    """Create the project structure identified by name."""

    logger.info("Loading project '%s'.", name)

    project = load_project(DATA_PATH, name)

    logger.info(
        "Creating project '%s' at '%s'.",
        project.name,
        project.path,
    )

    create_structure(project)

    logger.info("Project '%s' created.", project.name)