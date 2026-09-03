from pathlib import Path
from typing import Any
import yaml
from project_tools.spec import ArgumentSpec, CommandSpec


def load_command_specs(path: Path) -> tuple[CommandSpec, ...]:
    with path.open("r", encoding="utf-8") as file:
        data: dict[str, Any] = yaml.safe_load(file)

    commands = data["commands"]

    return tuple(
        _load_command_spec(name, command_data)
        for name, command_data in commands.items()
    )


def _load_command_spec(
    name: str,
    data: dict[str, Any],
) -> CommandSpec:
    args = tuple(
        ArgumentSpec(**arg)
        for arg in data.get("args", [])
    )

    commands = tuple(
        _load_command_spec(child_name, child_data)
        for child_name, child_data in data.get("commands", {}).items()
    )

    return CommandSpec(
        name=name,
        help=data["help"],
        function=data.get("function"),
        args=args,
        commands=commands,
    )