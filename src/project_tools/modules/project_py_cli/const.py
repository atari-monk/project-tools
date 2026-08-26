from typing import Final

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