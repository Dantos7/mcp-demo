"""Simple client to connect to the MCP server."""

# ruff: noqa: T201 (allow print in this simple example)

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()  # read API key from .env file

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        },
    ],
    model="openai/gpt-oss-120b",
)

print(chat_completion.choices[0].message.content)
