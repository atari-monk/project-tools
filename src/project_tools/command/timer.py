from argparse import Namespace
import logging

from project_tools.const import WORKSPACE_PATH


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    logger.info("Timer on interval: %s", args.time)
