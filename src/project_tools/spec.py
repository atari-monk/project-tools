from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ArgumentSpec:
    short_flag: str
    flag: str
    required: bool
    help: str
    action: str | None = None
    dest: str | None = None
    default: Any = None
    nargs: str | int | None = None
    type: str | None = None


@dataclass(frozen=True)
class CommandSpec:
    name: str
    help: str
    function: str
    args: tuple[ArgumentSpec, ...]