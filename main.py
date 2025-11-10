import asyncio
from services.analyze_a11y import analyze_a11y
from services.get_dependencies import get_deps
from services.read_file import read_file
import typer
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

load_dotenv(override=True)

app = typer.Typer(no_args_is_help=True)

console = Console()

async def _analyze_a11y(path: str):
    print("Analyzing accessibility for: ", path,)

    file_content = read_file(path)

    deps = await get_deps(file_content, path)
    print(f"Found {len(deps)} dependencies.")
    for dep in deps:
        print(f"- {dep}")
    
    accessibility_report = await analyze_a11y(file_content)
    print("Accessibility Analysis Report:")
    
    table = Table("Title", "Issue", "WCAG Reference", "Impact", "Recommendation")
    for issue in accessibility_report:
        table.add_row(
            issue.title,
            issue.issue,
            issue.wcag_reference,
            issue.impact,
            issue.recommendation
        )

    console.print(table)


@app.command()
def main():
    print("Hello from ai-a11y-analyzer!")
    
@app.command()
def analyze(path: str):
    asyncio.run(_analyze_a11y(path))


if __name__ == "__main__":
    app()
