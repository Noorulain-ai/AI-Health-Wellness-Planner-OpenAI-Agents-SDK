# hooks.py
from agents import RunHooks
from datetime import datetime

class MyHooks(RunHooks):
    def on_tool_start(self, tool_name, input, context):
        print(f"[{datetime.now()}] ✅ Tool started: {tool_name} with input: {input}")

    def on_tool_end(self, tool_name, output, context):
        print(f"[{datetime.now()}] 🛑 Tool ended: {tool_name} with output: {output}")

    def on_agent_start(self, agent_name, input, context):
        print(f"[{datetime.now()}] 🤖 Agent started: {agent_name} with user input: {input}")

    def on_agent_end(self, agent_name, output, context):
        print(f"[{datetime.now()}] 🎉 Agent finished: {agent_name} with output: {output}")

    def on_handoff(self, from_agent, to_agent, input, context):
        print(f"[{datetime.now()}] 🔁 Handoff from {from_agent} to {to_agent} with input: {input}")
        if hasattr(context, "handoff_logs"):
            context.handoff_logs.append(f"Handoff from {from_agent} to {to_agent} at {datetime.now()}")