#!/usr/bin/env python3
"""Tools & Environment — verify your environment with one safe test call.

Proves three things at once: (1) your virtual environment has the SDK,
(2) your API key loads from a hidden .env (never from code), and (3) the
key actually works. Run it locally OR on your NAIRR VM over Remote-SSH.

Setup:
    cp sample.env .env        # then put your real key in .env
    pip install python-dotenv openai
    python verify_env.py

The same idea works in Colab — read the key from Colab Secrets instead:
    from google.colab import userdata
    os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")
"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # reads .env from the repo root; keys never live in code

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise SystemExit("No OPENAI_API_KEY found. Copy sample.env to .env and add your key.")

from openai import OpenAI

client = OpenAI(api_key=key)
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in one short sentence."}],
)
print("Environment OK — model replied:")
print(resp.choices[0].message.content)
