# guardrails.py
from pydantic import BaseModel

class GoalInput(BaseModel):
    goal_type: str  # e.g., "lose weight"
    quantity: float
    metric: str      # e.g., "kg"
    duration: str    # e.g., "2 months"

class MealPlanOutput(BaseModel):
    meals: list[str]

class WorkoutPlanOutput(BaseModel):
    plan: dict