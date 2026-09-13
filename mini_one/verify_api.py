import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


project_root = Path(__file__).resolve().parent.parent
load_dotenv(project_root / ".env")

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY was not loaded. Add it to IT7075/.env and run again."
    )

client = OpenAI()
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Reply with exactly: Local API test successful.",
)

print(response.output_text)