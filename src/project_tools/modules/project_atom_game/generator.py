from dataclasses import dataclass
from logging import Logger
from pathlib import Path

from project_tools.config import WORKSPACE_PATH
from project_tools.shared.file_system import create_file_with_logging, create_folder_with_logging
from project_tools.shared.page_config import get_page_title


@dataclass
class WebProject:
    name: str
    path: Path
    page_name:str


def set_project(name: str) -> WebProject:
    return WebProject(
        name,
        path = WORKSPACE_PATH / name,
        page_name = get_page_title(name))


def create_project(project: WebProject, logger: Logger):
    create_folder_with_logging(WORKSPACE_PATH, project.name, logger)

    create_folder_with_logging(project.path, "docs", logger)
    create_file_with_logging(project.path / "docs", "_config.yml", project.page_name, logger)