from agents.tool import function_tool

@function_tool
def InjurySupportAgent(injury: str = "knee pain") -> str:
    return f"🩺 For {injury}, rest, ice, and consult a physiotherapist if it persists."