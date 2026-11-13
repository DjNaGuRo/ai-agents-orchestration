import os
from pathlib import Path

from langchain.chat_models import init_chat_model

from agents.utils import make_agent

ARCHITECT_SYSTEM_PROMPT = Path(__file__).with_name("agent.md").read_text(encoding="utf-8")

model = init_chat_model(os.getenv("ARCHITECT_MODEL", "ollama:qwen3:32b"), temperature=0.1)
architect = make_agent(
        name="architect",
        prompt=ARCHITECT_SYSTEM_PROMPT,
        model=model,
        write_repo=False,
    )
