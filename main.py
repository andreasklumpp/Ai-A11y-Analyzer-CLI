import asyncio
from services.analyze_a11y import analyze_a11y
from services.get_dependencies import get_deps
from services.read_file import read_file
import typer
from rich import print
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

load_dotenv(override=True)

app = typer.Typer(no_args_is_help=True)

console = Console()


async def _analyze_a11y(base_path: str, page_path: str):
    print(
        "#############################################################################"
    )
    print(
        "##################### Starting accessibility analysis. #####################"
    )
    print(
        "#############################################################################"
    )
    print(
        "Analyzing accessibility for: ",
        page_path,
    )
    print(" ")
    print(" ")

    file_content = read_file(page_path)

    print(
        "################# Identifying dependencies and relevant files. #################"
    )
    deps = await get_deps(file_content, base_path, page_path)
    print(f"Found {len(deps)} relevant files.")
    for dep in deps:
        print(f"- {dep}")
    print(" ")
    print(" ")

    code = f"# {page_path} \n\n" + file_content

    for dep in deps:
        dep_content = read_file(dep)
        code += f"\n\n# {dep} \n\n" + dep_content

    accessibility_report = await analyze_a11y(code)

    print(
        "#############################################################################"
    )
    print(
        "##################### Accessibility analysis completed. #####################"
    )
    print(
        "#############################################################################"
    )
    print("[bold green]Accessibility Analysis Report:[/bold green]")

    table = Table(
        "Title",
        "Issue",
        "WCAG Reference",
        "Conformance level",
        "Impact",
        "Recommendation",
        "File path",
        "Code snippet",
    )
    for issue in accessibility_report:
        table.add_row(
            issue.title,
            issue.issue,
            issue.wcag_reference,
            issue.conformance_level,
            issue.impact,
            issue.recommendation,
            issue.issue_file_path,
            issue.issue_code_snippet,
        )

    console.print(table)
    print("[italic] Disclaimer: No gurantee for 100% accuracy of the report. [/italic]")


@app.command()
def main():
    print("Hello from ai-a11y-analyzer!")


@app.command()
def analyze(base_path:str, page_path: str):
    asyncio.run(_analyze_a11y(base_path, page_path))


if __name__ == "__main__":
    app()
