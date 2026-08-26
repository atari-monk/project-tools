from dataclasses import dataclass
import json
from logging import Logger
from pathlib import Path

from project_tools.config import WORKSPACE_PATH
from project_tools.shared.file_system import FileSystemResult, create_file, create_file_with_logging, create_folder_with_logging, log_file_system_result
from project_tools.modules.project_py_cli.const import INIT_MAIN, PYRIGHT_CONFIG
from project_tools.shared.page_config import get_page_title


@dataclass
class PyProject:
    name: str
    description: str
    cli_name: str
    path: Path
    package_name: str
    page_name:str


def set_py_project(name: str, description: str, cli_name:str) -> PyProject:
    return PyProject(
        name,
        description,
        cli_name,
        path = WORKSPACE_PATH / name,
        package_name = name.replace("-", "_"),
        page_name = get_page_title(name))


def set_pyright_config(project: PyProject) -> FileSystemResult:
    content = json.dumps(PYRIGHT_CONFIG, indent=4) + "\n"
    return create_file(project.path, "pyrightconfig.json", content)


def set_pyproject_toml(project: PyProject) -> FileSystemResult:
    content = f"""[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "{project.name}"
version = "1.0.0"
description = "{project.description}"
requires-python = ">=3.11"

[project.scripts]
{project.cli_name} = "cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""
    return create_file(project.path, "pyproject.toml", content)


def set_gitignore(project: PyProject) -> FileSystemResult:
    content = f""".venv/
.ruff_cache/
{project.package_name}.egg-info/
pycache/
"""
    return create_file(project.path, ".gitignore", content)


def create_project(project: PyProject, logger: Logger):
    create_folder_with_logging(WORKSPACE_PATH, project.name, logger)

    result = set_pyproject_toml(project)
    log_file_system_result(result, logger)

    result = set_pyright_config(project)
    log_file_system_result(result, logger)

    result = set_gitignore(project)
    log_file_system_result(result, logger)

    create_folder_with_logging(project.path, "src", logger)
    create_folder_with_logging(project.path / "src", project.package_name, logger)
    create_file_with_logging(project.path / "src" / project.package_name, "cli.py", INIT_MAIN, logger)

    create_folder_with_logging(project.path, "docs", logger)
    create_file_with_logging(project.path / "docs", "_config.yml", project.page_name, logger)
    create_folder_with_logging(project.path / "docs", "requirements", logger)