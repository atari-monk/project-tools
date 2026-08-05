from project_tools.const import WORKSPACE_PATH
from project_tools.file_system import create_folder
from project_tools.logger import setup_logger
from project_tools.setup_argparse import setup_argparse


def main() -> None:
    create_folder(WORKSPACE_PATH, "log")
    setup_logger(WORKSPACE_PATH / "log", "project-tools")
    setup_argparse()
