from agents import Agent, Runner
from models.a11y_issue import A11yIssue

INSTRUCTIONS = "You are a senior web developer. Your sole purpose is to identify and list all dependencies used in a given codebase."

class DepsAgent:

    def __init__(self):
        self.name = "DepsAgent"
        self.model = "gpt-5-nano"
        self.instructions = INSTRUCTIONS

        self.agent = Agent(
            name=self.name,
            model=self.model,
            instructions=self.instructions,
            output_type=list[str]
        )

    async def run(self, content: str, file_path: str) -> list[str]:
        prompt = f"Analyze the following application code and extract a list of all dependencies used in the codebase. \
            Return the dependencies that are custom components only. Resolve the path using the given path for the sourcode file. \
            Code: {content}\n\n \
            File path: {file_path}\n\n"
        response = await Runner.run(self.agent, prompt)
        return response.final_output