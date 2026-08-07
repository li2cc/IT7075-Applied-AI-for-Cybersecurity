"""Configuration for the Introduction to AI demos.

Loads API keys from a hidden .env file (searched upward from here, so the
repo-root .env is found) WITHOUT printing their values, and never hard-fails:
the demos are written to run and simply skip a provider whose key is missing.

Model IDs live here in ONE place — change them here if a model is unavailable
to you, and every script/notebook that imports this stays consistent.
"""
import os
from dotenv import load_dotenv, find_dotenv

# Reads .env if present (repo root); a no-op when there is none. Real values
# stay in .env (git-ignored) — never hard-code keys in source.
load_dotenv(find_dotenv())

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

HAS_ANTHROPIC = bool(ANTHROPIC_API_KEY)
HAS_OPENAI = bool(OPENAI_API_KEY)

# Swap these if a model is not available on your account.
CLAUDE_MODEL = "claude-haiku-4-5-20251001"   # Anthropic (Claude Haiku 4.5)
OPENAI_MODEL = "gpt-5-mini"                   # OpenAI


def key_status() -> None:
    """Print which keys are present (never the key values themselves)."""
    print(f"Anthropic key: {'found' if HAS_ANTHROPIC else 'MISSING (Claude step will skip)'}")
    print(f"OpenAI key:    {'found' if HAS_OPENAI else 'MISSING (OpenAI step will skip)'}")


if __name__ == "__main__":
    key_status()
