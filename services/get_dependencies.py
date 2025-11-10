from custom_agents.deps_agent import DepsAgent


async def get_deps(content: str, file_path: str) -> list[str]:
    """Extracts and returns a list of dependencies from the given content."""

    print("Starting dependency extraction...")
    print("This may take a few moments.")
    agent = DepsAgent()
    result = await agent.run(content, file_path)

    return result