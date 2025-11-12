from custom_agents.deps_agent import DepsAgent


async def get_deps(content: str, base_path: str, file_path: str) -> list[str]:
    """Extracts and returns a list of dependencies from the given content."""

    print("Starting dependency extraction...")
    print("This may take a few moments.")
    agent = DepsAgent()
    result = await agent.run(content, base_path, file_path)

    return result