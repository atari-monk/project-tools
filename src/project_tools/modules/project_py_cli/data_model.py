from dataclasses import dataclass

from project_tools.modules.project_shared.data_model import ProjectConfig


@dataclass
class PyCliConfig:
    project: ProjectConfig
    cli_name: str
    package_name: str


def set_py_cli_project(project: ProjectConfig, cli_name: str) -> PyCliConfig:
    return PyCliConfig(
        project,
        cli_name,
        package_name = project.name.replace("-", "_"))