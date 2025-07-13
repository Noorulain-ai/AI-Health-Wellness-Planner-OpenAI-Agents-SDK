from agents.tool import function_tool

@function_tool
def ProgressTrackerTool(metric: str = "steps") -> str:
    return f"📊 Tracking {metric}: Keep pushing towards your daily goal!"