from argparse import Namespace
import logging

from project_tools.modules.project_py_cli.generator import create_project, set_py_project


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    project = set_py_project(args.project, args.description, args.cli_name)
    create_project(project, logger)