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