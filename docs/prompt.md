Refactor acording to updated SRS so that logger is fixed as stated in it:
I would preferr if we removed custom logger config form timer and use cli app one

## Timer

### Argparse setup

* Setup boilerplate code for command:
```sh
proj timer -t 25m
```
* All args/flags are optional

#### Time Arg

* Arg `-t` accepts a time string like `5s or 1h or 25m`
* Add `--time` alias

#### Pomodoro flag

* `-o` flag runs timer for pomodoro with 25m set
* Add `--pomodoro` alias

#### Print flag

* `-p` flag prints log file to console
* Add `--print` alias

#### Edit flag

* `-e` flag opens log file in visual studio code to edit
* `code <log-file>`
* Add `--edit` alias

### Logger

* Use same setup as cli app logger
* Add a separate log file `/home/atari-monk/atari-monk/project/log/timer.log`
* So logger logs to console, `project_tools.log` and `timer.log`
* Make sure other commands dont log to `timer.log`

### Behavior

* Log info message: `Starting timer -t x`
* Run timer asynchronously/backgrounded while the CLI remains usable
* When timer runs down log `Stopping timer -t x`
* Use ubuntu notify pop up to signal timer end
* Use sound on ubuntu to signal timer end
* When no args or wrong args, print help

### Commits 

* feat: timer setup
* feat: implement timer functionality

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/logger.py

```python
import logging
from pathlib import Path


def setup_logger(log_folder_path: Path, log_file_name: str) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_folder_path / f"{log_file_name}.log"),
        ],
    )
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/cli.py

```python
from project_tools.const import WORKSPACE_PATH
from project_tools.file_system import create_folder
from project_tools.logger import setup_logger
from project_tools.argparse_setup import setup_argparse


def main() -> None:
    create_folder(WORKSPACE_PATH, "log")
    setup_logger(WORKSPACE_PATH / "log", "project-tools")
    setup_argparse()
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/command/timer.py

```python
from argparse import Namespace
import logging

from project_tools.shared.timer.duration import (
    InvalidDurationError,
    parse_duration,
)
from project_tools.shared.timer.log import edit_log, print_log
from project_tools.shared.timer.logger import get_log_path
from project_tools.shared.timer.runner import start_timer # type: ignore


logger = logging.getLogger(__name__)

POMODORO_DURATION = "25m"


def run(args: Namespace) -> None:
    """Run the timer command."""
    if (
        args.time is None
        and not args.pomodoro
        and not args.print_log
        and not args.edit
    ):
        args.parser.print_help()
        return

    if args.print_log:
        print_log(get_log_path())

    if args.edit:
        edit_log(get_log_path())

    if not args.time and not args.pomodoro:
        return

    duration = POMODORO_DURATION if args.pomodoro else args.time

    try:
#         Argument of type "Any | Literal['25m'] | None" cannot be assigned to parameter "value" of type "str" in function "parse_duration"
#   Type "Any | Literal['25m'] | None" is not assignable to type "str"
#     "None" is not assignable to "str"
        seconds = parse_duration(duration)
    except InvalidDurationError as exc:
        logger.error("%s", exc)
        return

    start_timer(seconds)

    logger.info("Timer started: %s", duration)
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/__init__.py

```python
"""Timer functionality shared by project-tools commands."""

from project_tools.shared.timer.duration import parse_duration
from project_tools.shared.timer.logger import configure_logger
from project_tools.shared.timer.runner import start_timer

__all__ = [
    "configure_logger",
    "parse_duration",
    "start_timer",
]
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/duration.py

```python
"""Time interval parsing for the timer."""

import re


_DURATION_PATTERN = re.compile(r"^(?P<value>\d+(?:\.\d+)?)(?P<unit>[smh])$")

_UNIT_TO_SECONDS = {
    "s": 1,
    "m": 60,
    "h": 60 * 60,
}


class InvalidDurationError(ValueError):
    """Raised when a timer duration cannot be parsed."""


def parse_duration(value: str) -> float:
    """Convert a duration such as ``5s``, ``25m`` or ``1h`` to seconds."""
    if not value:
        raise InvalidDurationError("Timer duration cannot be empty.")

    match = _DURATION_PATTERN.fullmatch(value.strip().lower())

    if match is None:
        raise InvalidDurationError(
            "Invalid timer duration. Use a value such as 5s, 25m or 1h."
        )

    number = float(match.group("value"))
    unit = match.group("unit")

    seconds = number * _UNIT_TO_SECONDS[unit]

    if seconds <= 0:
        raise InvalidDurationError("Timer duration must be greater than zero.")

    return seconds
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/events.py

```python
"""Timer log events."""

from datetime import datetime
from logging import Logger


TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M"


def current_timestamp() -> str:
    """Return the current local timestamp in the timer log format."""
    return datetime.now().strftime(TIMESTAMP_FORMAT)


def log_start(logger: Logger) -> None:
    """Log the timer start event."""
    logger.info("start %s", current_timestamp())


def log_stop(logger: Logger) -> None:
    """Log the timer stop event."""
    logger.info("stop %s", current_timestamp())
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/log.py

```python
"""Timer log file operations."""

from pathlib import Path
import subprocess


def read_log(log_path: Path) -> str:
    """Read the timer log file."""
    if not log_path.exists():
        return ""

    return log_path.read_text(encoding="utf-8")


def print_log(log_path: Path) -> None:
    """Print the timer log to stdout."""
    content = read_log(log_path)

    if content:
        print(content, end="" if content.endswith("\n") else "\n")


def edit_log(log_path: Path) -> None:
    """Open the timer log in Visual Studio Code."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.touch(exist_ok=True)

    subprocess.Popen(
        ["code", str(log_path)],
        start_new_session=True,
    )
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/logger.py

```python
"""Logging setup for the timer."""

import logging
from pathlib import Path

from project_tools.const import WORKSPACE_PATH


LOGGER_NAME = "project_tools.timer"
LOG_FILE_NAME = "timer.log"


def get_log_path() -> Path:
    """Return the timer log file path."""
    return Path(WORKSPACE_PATH) / "log" / LOG_FILE_NAME


def configure_logger() -> logging.Logger:
    """Configure console and file logging for the timer."""
    logger = logging.getLogger(LOGGER_NAME)

    if logger.handlers:
        return logger

    log_path = get_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter("%(message)s")

    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/notification.py

```python
"""Ubuntu desktop notification for timer completion."""

import shutil
import subprocess


def notify_timer_finished() -> None:
    """Display an Ubuntu notification when the timer finishes."""
    notify_send = shutil.which("notify-send")

    if notify_send is None:
        return

    subprocess.run(
        [
            notify_send,
            "Timer finished",
            "Your timer has finished.",
        ],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/runner.py

```python
"""Start timer processes in the background."""

import os
import subprocess
import sys
from pathlib import Path


def start_timer(seconds: float) -> subprocess.Popen: # type: ignore
    """Start a detached timer worker and return immediately."""
    command = [
        sys.executable,
        "-m",
        "project_tools.shared.timer.worker",
        str(seconds),
    ]

    return subprocess.Popen(
        command,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
        cwd=Path.cwd(),
        env=os.environ.copy(),
    )
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/sound.py

```python
"""Sound notification for timer completion."""

import shutil
import subprocess


_SOUND_FILE = "/usr/share/sounds/freedesktop/stereo/complete.oga"


def play_timer_finished_sound() -> None:
    """Play the standard Ubuntu completion sound."""
    paplay = shutil.which("paplay")

    if paplay is not None:
        subprocess.run(
            [paplay, _SOUND_FILE],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return

    canberra = shutil.which("canberra-gtk-play")

    if canberra is not None:
        subprocess.run(
            [canberra, "-i", "complete"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
```

## /home/atari-monk/atari-monk/project/project-tools/src/project_tools/shared/timer/worker.py

```python
"""Background timer worker."""

import argparse
import time

from project_tools.shared.timer.events import log_start, log_stop
from project_tools.shared.timer.logger import configure_logger
from project_tools.shared.timer.notification import notify_timer_finished
from project_tools.shared.timer.sound import play_timer_finished_sound


def run(seconds: float) -> None:
    """Run a timer in the background process."""
    logger = configure_logger()

    log_start(logger)

    try:
        time.sleep(seconds)
    finally:
        log_stop(logger)
        notify_timer_finished()
        play_timer_finished_sound()


def create_parser() -> argparse.ArgumentParser:
    """Create the worker argument parser."""
    parser = argparse.ArgumentParser(description="Project-tools timer worker.")
    parser.add_argument("seconds", type=float)

    return parser


def main() -> None:
    """Run the timer worker CLI."""
    parser = create_parser()
    args = parser.parse_args()

    run(args.seconds)


if __name__ == "__main__":
    main()
```

