from argparse import Namespace
import logging

from project_tools.const import WORKSPACE_PATH
from project_tools.file_system import create_folder_and_log_it


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    create_folder_and_log_it(WORKSPACE_PATH, args.project, logger)