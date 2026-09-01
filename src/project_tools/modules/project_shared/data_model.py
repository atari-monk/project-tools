from dataclasses import dataclass
from pathlib import Path


@dataclass
class ProjectConfig:
    name: str
    description: str
    path: Path
    page_name:str


def get_page_title(project_name: str) -> str:
    return f"title: {project_name.replace("-", " ").replace("_", " ").title()}"


def set_project(name: str, description: str, workspace_path: Path) -> ProjectConfig:
    return ProjectConfig(
        name,
        description,
        path = workspace_path / name,
        page_name = get_page_title(name))