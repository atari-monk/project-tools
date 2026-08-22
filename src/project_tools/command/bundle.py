from argparse import Namespace
import logging

from project_tools.shared.bundle.bundler import bundle_files


logger = logging.getLogger(__name__)


def run(args: Namespace) -> None:
    bundle_files(args.out, args.paths)