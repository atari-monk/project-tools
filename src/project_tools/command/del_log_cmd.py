from argparse import Namespace
import logging
import subprocess

from project_tools.const import WORKSPACE_PATH


logger = logging.getLogger(__name__)

LOG_PATH = WORKSPACE_PATH / "log" / "project-tools.log"


def run(_: Namespace) -> None:
    logger.info("Moving log: %s to trash", LOG_PATH)

    if not LOG_PATH.exists():
        logger.info("Log file does not exist: %s", LOG_PATH)
        return

    subprocess.run(
        ["gio", "trash", str(LOG_PATH)],
        check=True,
    )

    logger.info("Log file moved to trash")