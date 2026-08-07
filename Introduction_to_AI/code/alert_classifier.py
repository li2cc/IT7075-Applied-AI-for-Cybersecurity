"""Security Alert Classifier — the same alert, two cloud LLMs, side by side.

Sends one security alert to Claude (Anthropic) and to OpenAI and prints their
verdicts next to each other. Each call is GUARDED: if a key is missing the demo
prints a notice for that provider and keeps going, so it runs with one key, both,
or (as a dry run) neither.

Run:  python alert_classifier.py
Keys: put ANTHROPIC_API_KEY / OPENAI_API_KEY in a repo-root .env (see config.py).
"""
import textwrap
from config import (
    ANTHROPIC_API_KEY, OPENAI_API_KEY, HAS_ANTHROPIC, HAS_OPENAI,
    CLAUDE_MODEL, OPENAI_MODEL, key_status,
)

PROMPT = "Classify this security alert as benign or suspicious and explain in one sentence: {alert}"


def classify_with_claude(alert: str) -> str:
    """Classify the alert with Claude; skip cleanly if no key is set."""
    if not HAS_ANTHROPIC:
        return "[skipped — no ANTHROPIC_API_KEY set]"
    from anthropic import Anthropic
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    msg = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=150,
        messages=[{"role": "user", "content": PROMPT.format(alert=alert)}],
    )
    return msg.content[0].text.strip()


def classify_with_openai(alert: str) -> str:
    """Classify the alert with OpenAI; skip cleanly if no key is set."""
    if not HAS_OPENAI:
        return "[skipped — no OPENAI_API_KEY set]"
    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": PROMPT.format(alert=alert)}],
    )
    return response.choices[0].message.content.strip()


def _panel(title: str, body: str) -> None:
    print("-" * 64)
    print(title)
    print("-" * 64)
    print("\n".join(textwrap.wrap(body, width=64)) or body)
    print()


def main() -> None:
    alert = "5 failed logins for 'admin' from 203.0.113.7 in 20s, then 1 success"

    print("=" * 64)
    print("SECURITY ALERT CLASSIFIER  —  the same alert, two models")
    print("=" * 64)
    key_status()
    print(f"\nAlert: {alert}\n")

    _panel(f"Claude  ({CLAUDE_MODEL})", classify_with_claude(alert))
    _panel(f"OpenAI  ({OPENAI_MODEL})", classify_with_openai(alert))

    print("Compare: do the two models agree? Is either more specific or better "
          "justified? Remember to verify — treat each verdict as a draft, not a fact.")


if __name__ == "__main__":
    main()
