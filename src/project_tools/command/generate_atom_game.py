import logging
from argparse import Namespace

from project_tools.config import WORKSPACE_PATH
from project_tools.modules.project_atom_game.generator import create_atom_engine_game_project
from project_tools.modules.project_shared.data_model import set_project


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    logger.info("Creating new game project with atom engine: %s", args.project)
    config = set_project(args.project, args.description, WORKSPACE_PATH)
    create_atom_engine_game_project(config, logger)