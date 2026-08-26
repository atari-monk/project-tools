import logging
from argparse import Namespace


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    logger.info("Creating new game project with atom engine: %s", args.project)
    