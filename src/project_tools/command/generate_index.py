from argparse import Namespace
import logging

from project_tools.const import WORKSPACE_PATH
from project_tools.shared.docs_index.docs_index import generate_docs_index


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    docs_path = WORKSPACE_PATH / args.project / "docs"

    logger.info("Generating docs index for: %s", args.project)

    generate_docs_index(docs_path)