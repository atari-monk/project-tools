from argparse import Namespace
import logging
import subprocess

from project_tools.const import WORKSPACE_PATH


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    PROJECT_PATH = WORKSPACE_PATH / args.project

    logger.info("Moving project: %s to trash", PROJECT_PATH)

    if not PROJECT_PATH.exists():
        logger.info("Project does not exist: %s", PROJECT_PATH)
        return

    subprocess.run(
        ["gio", "trash", str(PROJECT_PATH)],
        check=True,
    )

    logger.info("Project moved to trash")
