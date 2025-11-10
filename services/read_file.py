def read_file(path: str) -> str:
    """Reads the content of a file and returns it as a string."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{path}' not found.")
    except Exception as e:
        raise Exception(f"Error reading file: {e}")