from argparse import Namespace
import logging
from pathlib import Path

from project_tools.modules.docs.print import (
    print_docs,
    scan_docs,
)


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    """Print documentation categories."""
    docs_path = Path(args.path)

    logger.info("Printing docs categories for: %s", docs_path)

    data = scan_docs(docs_path)
    print(print_docs(data))