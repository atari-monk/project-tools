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