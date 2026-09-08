from argparse import Namespace
import logging
from pathlib import Path

from project_tools.modules.docs.new import create_doc


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    """Create a new documentation file from clipboard content."""
    docs_path = Path(args.path)

    logger.info(
        "Creating new doc: path=%s, category=%s, name=%s",
        docs_path,
        args.category,
        args.name,
    )

    doc_path = create_doc(
        docs_path=docs_path,
        category=args.category,
        name=args.name,
    )

    logger.info("Created documentation file: %s", doc_path)