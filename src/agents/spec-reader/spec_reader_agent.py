import os
from pathlib import Path

from langchain.chat_models import init_chat_model
from mcp import mcp_client
from utils import make_agent

SYSTEM_PROMPT = Path(__file__).with_name("agent.md").read_text(encoding="utf-8")
model = init_chat_model(os.get("SPEC_READER_MODEL", "ollama:qwen3:8b"), temperature=0.1, top_p=0.9)
notion_tools = mcp_client.get_tools(server_name="notion")

spec_reader_agent = make_agent(
    name="spec-reader",
    prompt=SYSTEM_PROMPT,
    model=model,
    tools=notion_tools
)
