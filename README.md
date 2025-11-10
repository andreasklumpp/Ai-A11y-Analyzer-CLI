# AI A11y Analyzer

A Python tool for automated accessibility (a11y) analysis of web projects using OpenAI.

## Features
- Automated accessibility issue detection


## Project Structure
```
main.py                # Entry point for running the analyzer
pyproject.toml         # Project metadata and dependencies
custom_agents/         # Custom agent implementations
models/                # Data models (e.g., a11y_issue)
services/              # Core services (analyze, dependencies, file reading)
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-a11y-analyzer.git
   cd ai-a11y-analyzer
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   uv sync
   ```


## Usage
Run the analyzer on your project:
```sh
uv run main.py <target_path>
```

## License
MIT

