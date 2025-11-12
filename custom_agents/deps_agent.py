from agents import Agent, Runner
from models.a11y_issue import A11yIssue
import os

INSTRUCTIONS = "You are a senior React web developer. Your sole purpose is to identify and list all dependencies and relevant files for a given piece of code. \
    Relevant files can be layout or wrapper files that affect how the given page file renders."


def list_files_recursive(path='.') -> list[str]:
    files = []
    for entry in os.listdir(path):
        if entry == 'node_modules':
            continue
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            files.extend(list_files_recursive(full_path))
        else:
            files.append(full_path)
    return files

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

    async def run(self, content: str, base_path: str, file_path: str) -> list[str]:

        prompt = f"Analyze the following application code and extract a list of all dependencies used in the codebase. \
            Return the dependencies that are custom components only. Resolve the path using the given path for the sourcode file. \
            Code: {content}\n\n \
            File path: {file_path}\n\n"
        
        files = list_files_recursive(base_path)

        prompt2 = f"""
            You are provided all filenames in the project directory. You need to identify all files that are relevant to analyse, for making an accessibility analsysis of the given code. \
            Also identify the dependencies in the provided code.  
            Return the list of file names that are relevant to be analyzed and the dependencies in the code that are custom components only. Resolve the path using the given path for the sourcode file. \

            Code: {content}\n\n 
            Given page file path: {file_path}\n\n
            File names in project directory: [{', '.join(files)}] 

            Important: Return only a list of the file paths each as string. Do not add any other formatting or information.
        """
        response = await Runner.run(self.agent, prompt2)

        return response.final_output