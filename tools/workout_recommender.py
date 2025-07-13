from agents.tool import function_tool

@function_tool
def WorkoutRecommenderTool(goal: str = "general fitness") -> str:
    return f"💪 For {goal}, include 30 mins walk and 20 mins strength daily."