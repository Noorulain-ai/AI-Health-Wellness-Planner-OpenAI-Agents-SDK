import os
from dotenv import load_dotenv
from agent import health_agent
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not set in .env")

# Gemini setup
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=client,
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

# Terminal chat loop
print("🤖 Health & Wellness AI Agent Ready!")
print("Type 'exit' to quit.\n")

history = []

while True:
    user_input = input("🧑 You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    history.append({"role": "user", "content": user_input})

    try:
        result = Runner.run_sync(health_agent, history, run_config=config)
        reply = result.final_output
        print(f"🤖 Agent: {reply}")
        history.append({"role": "assistant", "content": reply})
    except Exception as e:
        print(f"❌ Error: {str(e)}")


