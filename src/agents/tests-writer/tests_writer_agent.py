import os
from pathlib import Path

from langchain.chat_models import init_chat_model

from agents.utils import make_agent

SYSTEM_PROMPT = Path(__file__).with_name("agent.md").read_text(encoding="utf-8")
model = init_chat_model(os.get("TESTS_WRITER_MODEL", "ollama:qwen3-coder:30b"), temperature=0.1, top_p=0.9)

tests_writer = make_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    name="tests-writer"
)
