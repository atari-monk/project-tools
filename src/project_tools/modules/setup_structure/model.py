from dataclasses import dataclass, field


@dataclass(frozen=True)
class Project:
    """Description of a project structure."""

    name: str
    path: str
    folders: list[str] = field(default_factory=list[str])
    files: list[str] = field(default_factory=list[str])