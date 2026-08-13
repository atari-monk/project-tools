from pathlib import Path
from typing import Final

WORKSPACE_PATH: Final[Path] = Path("/home/atari-monk/atari-monk/project")
DEL_LOG_CMD: Final[str] = "del_log"
DEL_PROJ_CMD: Final[str] = "del_proj"
INIT_CLI_CMD: Final[str] = "init_cli"
GEN_IDX_ORDER_CMD: Final[str] = "gen_idx_order"
GEN_IDX_CMD: Final[str] = "gen_idx"

PYRIGHT_CONFIG: Final[dict[str, object]] = {
    "typeCheckingMode": "strict",
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
}

INIT_MAIN: Final[str] = """def main() -> None:
    print("Hello World")
"""


def get_page_title(project_name: str) -> str:
    return f"title: {project_name.replace("-", " ").replace("_", " ").title()}"
