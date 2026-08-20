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