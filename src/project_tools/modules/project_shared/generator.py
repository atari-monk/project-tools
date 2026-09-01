from logging import Logger

from project_tools.modules.project_shared.data_model import ProjectConfig
from project_tools.shared.file_system import create_file_with_logging, create_folder_with_logging


def create_docs(config: ProjectConfig, logger: Logger):
    create_folder_with_logging(config.path, "docs", logger)
    create_folder_with_logging(config.path / "docs", "software requirements specification", logger)
    create_file_with_logging(config.path / "docs", "_config.yml", config.page_name, logger)
    create_file_with_logging(config.path / "docs", "_prompt.md", "", logger)