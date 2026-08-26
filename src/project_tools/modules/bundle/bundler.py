import json
from pathlib import Path

from .model import BundleConfig


CONFIG_PATH = (
    Path(__file__).resolve().parents[4]
    / "data"
    / "bundle.json"
)


def load_config() -> BundleConfig:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return BundleConfig(**json.load(file))


def _is_ignored_folder(
    path: Path,
    config: BundleConfig,
) -> bool:
    return path.name in config.ignored_folders


def _is_ignored_file(
    path: Path,
    config: BundleConfig,
) -> bool:
    return path.name in config.ignored_files


def _is_supported_file(
    path: Path,
    config: BundleConfig,
) -> bool:
    return path.suffix.lower() in config.supported_extensions


def _collect_files(
    path: Path,
    config: BundleConfig,
) -> list[Path]:
    files: list[Path] = []

    for item in sorted(path.iterdir()):
        if item.is_dir():
            if _is_ignored_folder(item, config):
                continue

            files.extend(_collect_files(item, config))
            continue

        if _is_ignored_file(item, config):
            continue

        if _is_supported_file(item, config):
            files.append(item)

    return files


def _render_file(
    path: Path,
    config: BundleConfig,
) -> str:
    language = config.languages.get(path.suffix.lower(), "")
    content = path.read_text(encoding="utf-8")

    if path.suffix.lower() == ".md":
        fence = "````"
    else:
        fence = "```"

    return (
        f"## {path}\n\n"
        f"{fence}{language}\n"
        f"{content.rstrip()}\n"
        f"{fence}\n\n"
    )


def bundle_files(
    out: Path,
    paths: list[Path],
) -> Path:
    config = load_config()

    if not paths:
        raise ValueError("At least one path is required")

    files: list[Path] = []

    # Preserve the order supplied by the CLI.
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(path)

        if path.is_dir():
            files.extend(_collect_files(path, config))
            continue

        if _is_ignored_file(path, config):
            continue

        if _is_supported_file(path, config):
            files.append(path)

    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8") as output:
        for path in files:
            output.write(_render_file(path, config))

    return out