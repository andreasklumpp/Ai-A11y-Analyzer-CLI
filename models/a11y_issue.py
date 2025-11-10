from pydantic import BaseModel

class A11yIssue(BaseModel):
    title: str
    issue: str
    wcag_reference: str
    impact: str
    recommendation: str