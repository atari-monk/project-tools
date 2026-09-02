from string import Template


def t(content: str, **variables: str) -> str:
    return Template(content).substitute(**variables)