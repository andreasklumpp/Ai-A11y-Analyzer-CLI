from agents import Agent, Runner
from models.a11y_issue import A11yIssue

INSTRUCTIONS = "You are an accessibility expert making sure the application is WCAG 2.1 AA compliant."

class A11yAgent:

    def __init__(self):
        self.name = "A11yAgent"
        self.model = "gpt-5-nano"
        self.instructions = INSTRUCTIONS

        self.agent = Agent(
            name=self.name,
            model=self.model,
            instructions=self.instructions,
            output_type=list[A11yIssue]
        )

    async def run(self, content: str) -> list[A11yIssue]:
        prompt = f"Analyze the following application code for accessibility issues. Return a structured list of accessibility issues and provide recommendations to make it WCAG 2.1 AA compliant. \
            Code: {content}\n\n"

        response = await Runner.run(self.agent, prompt)
        return response.final_output