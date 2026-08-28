from logging import Logger

from project_tools.modules.project_common.data_model import PyCliConfig
from project_tools.shared.file_system import create_file_with_logging, create_folder_with_logging


def create_docs(config: PyCliConfig, logger: Logger):
    create_folder_with_logging(config.project.path, "docs", logger)
    create_file_with_logging(config.project.path / "docs", "_config.yml", config.project.page_name, logger)
    create_folder_with_logging(config.project.path / "docs", "software requirements specification", logger)


def create_python_package(config: PyCliConfig, logger: Logger, main_content: str):
    create_folder_with_logging(config.project.path, "src", logger)
    create_folder_with_logging(config.project.path / "src", config.package_name, logger)
    create_file_with_logging(config.project.path / "src" / config.package_name, "cli.py", main_content, logger)