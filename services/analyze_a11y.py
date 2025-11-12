from custom_agents.a11y_agent import A11yAgent
from models.a11y_issue import A11yIssue

async def analyze_a11y(content: str) -> list[A11yIssue]:
    """Analyzes the given content for accessibility issues and returns recommendations."""

    print("################ This may take a few moments. ################")
    print(" ")
    print(" ")
    agent = A11yAgent()
    result = await agent.run(content)

    return result