from project_tools.modules.project_py_cli.data_model import PythonProjectConfig
from project_tools.modules.project_shared.types import Files
from project_tools.modules.project_shared.utils import t


def get_files(config: PythonProjectConfig) -> Files:
    return {
    "pyrightconfig.json": """"typeCheckingMode": "strict",
        "reportMissingImports": True,
        "reportMissingTypeStubs": True,
        "reportUnknownParameterType": True,
        "reportUnknownVariableType": True,
        "reportUntypedFunctionDecorator": True,
        "reportUntypedClassDecorator": True,
        "reportUntypedBaseClass": True,
        "reportUnknownMemberType": True,
        "reportUnknownArgumentType": True,
        "reportGeneralTypeIssues": True,
        "reportOptionalMemberAccess": True,
        "reportOptionalSubscript": True,
        "reportOptionalCall": True,
""",
    "cli.py": """def main() -> None:
    print("Hello World")
""",
    "pyproject.toml": t("""[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "$name"
version = "1.0.0"
description = "$description"
requires-python = ">=3.11"

[project.scripts]
$cli_name = "cli:main"

[tool.setuptools.packages.find]
where = ["src"]
""", name = config.name, description = config.description, cli_name = config.cli_name),
    ".gitignore": t(""".venv/
.ruff_cache/
$package_name.egg-info/
pycache/
""", package_name = config.package_name)
}