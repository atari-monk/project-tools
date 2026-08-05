import logging
import subprocess

from project_tools.const import WORKSPACE_PATH


LOGGER = logging.getLogger(__name__)

LOG_PATH = WORKSPACE_PATH / "log" / "project-tools.log"


def run() -> None:
    LOGGER.info("Moving log: %s to trash", LOG_PATH)

    if not LOG_PATH.exists():
        LOGGER.info("Log file does not exist: %s", LOG_PATH)
        return

    subprocess.run(
        ["gio", "trash", str(LOG_PATH)],
        check=True,
    )

    LOGGER.info("Log file moved to trash")