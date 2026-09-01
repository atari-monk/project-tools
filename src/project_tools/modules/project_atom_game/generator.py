from logging import Logger
from pathlib import Path

from project_tools.config import WORKSPACE_PATH
from project_tools.modules.project_atom_game.files import get_files
from project_tools.modules.project_shared.data_model import ProjectConfig
from project_tools.modules.project_shared.generator import create_docs
from project_tools.shared.file_system import copy_file_with_logging, create_file_with_logging, create_folder_with_logging


def create_atom_engine_game_project(config: ProjectConfig, logger: Logger):
    create_folder_with_logging(WORKSPACE_PATH, config.name, logger)
    create_folder_with_logging(config.path, "src", logger)
    create_folder_with_logging(config.path, "public", logger)
    create_folder_with_logging(config.path, "sounds", logger)
    files = get_files(config)
    package = "package.json"
    index = "index.html"
    tsconfig = "tsconfig.json"
    vite_config = "vite.config.js"
    gitignore = ".gitignore"
    create_file_with_logging(config.path, package, files[package], logger)
    create_file_with_logging(config.path, index, files[index], logger)
    create_file_with_logging(config.path, tsconfig, files[tsconfig], logger)
    create_file_with_logging(config.path, vite_config, files[vite_config], logger)
    create_file_with_logging(config.path, gitignore, files[gitignore], logger)
    style = "style.css"
    rect = "rect.ts"
    game = "game.ts"
    main = "main.ts"
    create_file_with_logging(config.path / "src", style, files[style], logger)
    create_file_with_logging(config.path / "src" / "shared", rect, files[rect], logger)
    create_file_with_logging(config.path / "src", game, files[game], logger)
    create_file_with_logging(config.path / "src", main, files[main], logger)
    create_docs(config, logger)
    copy_file_with_logging(Path("/home/atari-monk/atari-monk/assets/favicon/favicon-atom.png"), config.path / "public", logger)