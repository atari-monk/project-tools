from argparse import Namespace
import logging

from project_tools.config import WORKSPACE_PATH
from project_tools.modules.project_py_cli.data_model import set_py_cli_project
from project_tools.modules.project_py_cli.generator import create_py_cli_project


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    pycli_config = set_py_cli_project(args.project, args.description, WORKSPACE_PATH, args.cli_name)
    create_py_cli_project(pycli_config, logger)