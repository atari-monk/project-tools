from dataclasses import dataclass


@dataclass(frozen=True)
class BundleConfig:
    ignored_folders: list[str]
    ignored_files: list[str]
    supported_extensions: list[str]
    languages: dict[str, str]