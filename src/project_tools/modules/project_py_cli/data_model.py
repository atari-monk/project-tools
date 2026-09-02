from dataclasses import dataclass
from pathlib import Path

from project_tools.modules.project_shared.data_model import ProjectConfig, get_page_title


@dataclass
class PythonProjectConfig(ProjectConfig):
    cli_name: str
    package_name: str


def set_py_cli_project(name: str, description: str, workspace_path: Path, cli_name: str) -> PythonProjectConfig:
    return PythonProjectConfig(
        name,
        description,
        path = workspace_path / name,
        page_name = get_page_title(name),
        cli_name = cli_name,
        package_name = name.replace("-", "_"))