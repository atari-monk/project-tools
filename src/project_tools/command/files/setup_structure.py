from argparse import Namespace
import logging

from project_tools.modules.setup_structure.orchestrator import create_project


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    create_project(args.project, logger)