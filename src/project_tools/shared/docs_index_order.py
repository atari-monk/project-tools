from pathlib import Path

from project_tools.shared.docs_discovery import discover_documentation_files
from project_tools.shared.docs_order import update_order_file


def generate_docs_index(docs_path: Path) -> None:
    """Generate docs/order.txt and docs/index.md."""
    docs_path.mkdir(parents=True, exist_ok=True)

    discovered_paths = discover_documentation_files(docs_path)

    update_order_file(
        docs_path=docs_path,
        discovered_paths=discovered_paths,
    )