from agents.tool import function_tool

@function_tool
def MealPlannerTool(diet: str = "balanced") -> str:
    return f"🥗 A {diet} meal plan includes protein, fiber, fruits, and water."