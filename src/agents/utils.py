from pathlib import Path
import logging

from deepagents import create_deep_agent
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend  # backend fichiers local
from langchain.chat_models import init_chat_model

REPO_PATH = Path(__file__).resolve().parents[2]
logger = logging.getLogger(__name__)

def make_agent(name: str, prompt: str, model, tools: list | None = None,
               subagents: list | None = None, write_repo: bool = False):
    """Un Deep Agent = planning + filesystem + sous-agents.
    `write_repo=False` : on restreint le backend au scratch dir (lecture du repo
    via les outils dédiés), `True` : le backend pointe sur le repo."""
    backend = FilesystemBackend(root_dir=REPO_PATH if write_repo else "./.scratch",
                                virtual_mode=True)
    agent = create_deep_agent(
        model=model,
        system_prompt=prompt,
        tools=tools or [],
        subagents=subagents or [],
        backend=backend,
        name=name,
    )
    logger.info(f"Agent {name} is created!")
    return agent
