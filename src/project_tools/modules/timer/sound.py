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