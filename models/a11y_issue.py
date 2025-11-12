from pydantic import BaseModel

class A11yIssue(BaseModel):
    title: str
    issue: str
    wcag_reference: str
    conformance_level: str
    impact: str
    recommendation: str
    issue_file_path: str
    issue_code_snippet: str
