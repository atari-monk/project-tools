from argparse import Namespace
import logging

from project_tools.config import WORKSPACE_PATH
from project_tools.modules.project_py_cli.const import INIT_MAIN, get_page_title
from project_tools.shared.file_system import create_file_with_logging, create_folder_with_logging, log_file_system_result
from project_tools.modules.project_py_cli.generator import set_gitignore, set_pyproject_toml, set_pyright_config


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    project_path = WORKSPACE_PATH / args.project
    package_name = args.project.replace("-", "_")

    create_folder_with_logging(WORKSPACE_PATH, args.project, logger)

    result = set_pyproject_toml(args.project, args.description, args.cli_name)
    log_file_system_result(result, logger)

    result = set_pyright_config(args.project)
    log_file_system_result(result, logger)

    result = set_gitignore(args.project)
    log_file_system_result(result, logger)

    create_folder_with_logging(project_path, "src", logger)
    create_folder_with_logging(project_path / "src", package_name, logger)
    create_file_with_logging(project_path / "src" / package_name, "cli.py", INIT_MAIN, logger)

    create_folder_with_logging(project_path, "docs", logger)
    create_file_with_logging(project_path / "docs", "_config.yml", get_page_title(args.project), logger)
    create_folder_with_logging(project_path / "docs", "requirements", logger)
