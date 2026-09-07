from argparse import Namespace
import logging
from pathlib import Path

from project_tools.modules.docs.index import generate_docs_index


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    docs_path = Path(args.path)
    logger.info("Generating docs index for: %s", docs_path)
    generate_docs_index(docs_path)