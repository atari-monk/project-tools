from project_tools.config import WORKSPACE_PATH
from project_tools.shared.file_system import create_folder
from project_tools.shared.logger import setup_logger
from project_tools.argparse_setup import setup_argparse


def main() -> None:
    create_folder(WORKSPACE_PATH, "log")
    setup_logger(WORKSPACE_PATH / "log", "project-tools")
    setup_argparse()