import json


from project_tools.config import WORKSPACE_PATH
from project_tools.shared.file_system import FileSystemResult, create_file
from project_tools.modules.project_py_cli.const import PYRIGHT_CONFIG


def set_pyright_config(project_name: str) -> FileSystemResult:
    parent = WORKSPACE_PATH / project_name
    content = json.dumps(PYRIGHT_CONFIG, indent=4) + "\n"

    return create_file(parent, "pyrightconfig.json", content)


def set_pyproject_toml(
    project_name: str,
    description: str,
    cli_name: str
) -> FileSystemResult:
    parent = WORKSPACE_PATH / project_name
    content = f"""[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "1.0.0"
description = "{description}"
requires-python = ">=3.11"

[project.scripts]
{cli_name} = "cli:main"

[tool.setuptools.packages.find]
where = ["src"]
"""

    return create_file(parent, "pyproject.toml", content)


def set_gitignore(project_name: str) -> FileSystemResult:
    parent =  WORKSPACE_PATH / project_name 
    package_name = project_name.replace("-", "_")

    content = f""".venv/
.ruff_cache/
{package_name}.egg-info/
pycache/
"""

    return create_file(parent, ".gitignore", content)
