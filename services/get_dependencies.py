def get_dependencies(file_content: str) -> list:
    """Extracts and returns a list of dependencies from the given file content."""
    dependencies = []
    for line in file_content.splitlines():
        line = line.strip()
        if line.startswith("import ") or line.startswith("from "):
            dependencies.append(line)
    return dependencies