import json
from dataclasses import dataclass
from pathlib import Path
from typing import TypeGuard, cast


@dataclass(frozen=True)
class NoteConfig:
    logs: tuple[str, ...]

    def contains(self, log_name: str) -> bool:
        return log_name in self.logs


def is_list_of_str(obj: object) -> TypeGuard[list[str]]:
    """Return True if obj is a list of strings, and narrow the type accordingly."""
    if not isinstance(obj, list):
        return False
    # Cast to list[object] so the type checker knows each element is an object.
    # The runtime check below verifies every element is a str.
    as_list = cast(list[object], obj)
    return all(isinstance(item, str) for item in as_list)


def load_config(path: Path) -> NoteConfig:
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    logs = data.get("logs")

    if not is_list_of_str(logs):
        raise ValueError("Note log config must contain a 'logs' list of strings.")

    # logs is now inferred as list[str]
    return NoteConfig(logs=tuple(logs))