from agents.tool import function_tool

@function_tool
def NutritionExpertAgent(query: str = "daily protein needs") -> str:
    return f"🥩 As a nutritionist, I'd say: Daily protein = 0.8g per kg of body weight."