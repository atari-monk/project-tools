import json
from logging import Logger

from project_tools.config import WORKSPACE_PATH
from project_tools.modules.project_py_cli.data_model import PythonProjectConfig
from project_tools.modules.project_py_cli.files import get_files
from project_tools.modules.project_shared.generator import create_docs
from project_tools.shared.file_system import create_file_with_logging, create_folder_with_logging


def create_py_cli_project(config: PythonProjectConfig, logger: Logger):
    create_folder_with_logging(WORKSPACE_PATH, config.name, logger)
    create_folder_with_logging(config.path, "src", logger)
    create_folder_with_logging(config.path / "src", config.package_name, logger)
    files = get_files(config)
    pyproject = "pyproject.toml"
    pyrightconfig = "pyrightconfig.json"
    gitignore = ".gitignore"
    cli = "cli.py"
    create_file_with_logging(config.path, pyproject, files[pyproject], logger)
    create_file_with_logging(config.path, pyrightconfig, json.dumps(files[pyrightconfig], indent=4) + "\n", logger)
    create_file_with_logging(config.path, gitignore, files[gitignore], logger)
    create_file_with_logging(config.path / "src" / config.package_name, cli, files[cli], logger)
    create_docs(config, logger)