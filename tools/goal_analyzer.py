from agents.tool import function_tool

@function_tool
def GoalAnalyzerTool(goal: str) -> str:
    return f"🎯 Your goal '{goal}' sounds achievable and inspiring!"