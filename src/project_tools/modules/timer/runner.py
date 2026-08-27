import os
import subprocess
import sys
from pathlib import Path


def start_timer(
    seconds: float,
    duration: str,
) -> subprocess.Popen[bytes]:
    """Start a detached timer worker and return immediately."""
    command = [
        sys.executable,
        "-m",
        "project_tools.modules.timer.worker",
        str(seconds),
        duration,
    ]

    return subprocess.Popen(
        command,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
        cwd=Path.cwd(),
        env=os.environ.copy(),
    )