# 🧠 AI Health & Wellness Planner | OpenAI Agents SDK

A smart, conversational assistant that helps users set fitness goals, receive personalized meal and workout plans, track progress, and hand off to expert agents like a nutritionist or injury support coach — powered by the **OpenAI Agents SDK** and **Pydantic guardrails**.

---

## 🚀 Features

- ✅ Multi-turn health goal conversations
- 🥗 Personalized meal planning
- 🏋️‍♀️ Custom workout routines
- 📊 Progress tracking with context memory
- 🔀 Handoff to expert agents (nutrition, injury support, escalation)
- 🔐 Input/output validation with Pydantic models
- ⚡ Real-time streaming responses
- 🛡️ Guardrails to filter unrelated queries (e.g., jokes, poetry)

---

## 🧩 Tech Stack

- Python 3.10+
- OpenAI Agents SDK
- Pydantic
- Async/Await
- CLI-based chat interface (Streamlit optional)

---

## 📁 Folder Structure

health_wellness_agent/
├── main.py
├── agent.py
├── context.py
├── guardrails.py
├── tools/
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── scheduler.py
│ └── tracker.py
├── agents/
│ ├── escalation_agent.py
│ ├── nutrition_expert_agent.py
│ └── injury_support_agent.py
├── utils/
│ └── streaming.py
└── README.md


