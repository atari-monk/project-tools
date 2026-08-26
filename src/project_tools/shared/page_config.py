def get_page_title(project_name: str) -> str:
    return f"title: {project_name.replace("-", " ").replace("_", " ").title()}"