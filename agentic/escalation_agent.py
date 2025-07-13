from agents.tool import function_tool

@function_tool
def EscalationAgent(issue: str = "emergency") -> str:
    return f"🚨 Your issue '{issue}' may need a doctor. Please seek immediate help."