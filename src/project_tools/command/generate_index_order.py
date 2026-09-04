from argparse import Namespace
import logging
from pathlib import Path

from project_tools.modules.docs_index.docs_order import generate_docs_index_order


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    docs_path = Path(args.path)
    logger.info("Generating docs index order file for path: %s", docs_path)
    generate_docs_index_order(docs_path)