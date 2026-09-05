from pathlib import Path
from typing import Final

WORKSPACE_PATH: Final[Path] = Path("/home/atari-monk/atari-monk/project")
LOGS_PATH: Final[Path] = WORKSPACE_PATH / "log"
NOTE_LOG_CONFIG_PATH: Final[Path] = (WORKSPACE_PATH / "project-tools" / "data" / "note-logs.json")