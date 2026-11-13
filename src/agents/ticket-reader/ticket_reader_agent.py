import os
from pathlib import Path

from langchain.chat_models import init_chat_model
from mcp import mcp_client
from utils import make_agent

SYSTEM_PROMPT = Path(__file__).with_name("agent.md").read_text(encoding="utf-8")
model = init_chat_model(os.get("TICKET_READER_MODEL", "ollama:qwen3:8b"))
jira_tools = mcp_client.get_tools(server_name="jira")

ticker_reader = make_agent(
    name="ticket-reader",
    prompt=SYSTEM_PROMPT,
    tools=jira_tools
)
