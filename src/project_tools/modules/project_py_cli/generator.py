import json
from logging import Logger

from project_tools.config import WORKSPACE_PATH
from project_tools.modules.project_common.data_model import PyCliConfig
from project_tools.modules.project_common.generator import create_docs, create_python_package
from project_tools.shared.file_system import FileSystemResult, create_file, create_folder_with_logging, log_file_system_result
from project_tools.modules.project_py_cli.const import INIT_MAIN, PYRIGHT_CONFIG


def set_pyright_config(config: PyCliConfig) -> FileSystemResult:
    content = json.dumps(PYRIGHT_CONFIG, indent=4) + "\n"
    return create_file(config.project.path, "pyrightconfig.json", content)


def set_pyproject_toml(config: PyCliConfig) -> FileSystemResult:
    content = f"""[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "{config.project.name}"
version = "1.0.0"
description = "{config.project.description}"
requires-python = ">=3.11"

[project.scripts]
{config.cli_name} = "cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""
    return create_file(config.project.path, "pyproject.toml", content)


def set_gitignore(config: PyCliConfig) -> FileSystemResult:
    content = f""".venv/
.ruff_cache/
{config.package_name}.egg-info/
pycache/
"""
    return create_file(config.project.path, ".gitignore", content)


def create_project(config: PyCliConfig, logger: Logger):
    create_folder_with_logging(WORKSPACE_PATH, config.project.name, logger)

    result = set_pyproject_toml(config)
    log_file_system_result(result, logger)

    result = set_pyright_config(config)
    log_file_system_result(result, logger)

    result = set_gitignore(config)
    log_file_system_result(result, logger)

    create_python_package(config, logger, INIT_MAIN)
    create_docs(config, logger)