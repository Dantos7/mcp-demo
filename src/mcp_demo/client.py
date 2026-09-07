"""Simple client to connect to the MCP server."""

# ruff: noqa: T201 (allow print in this simple example)

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NGROK_DOMAIN = os.getenv("NGROK_DOMAIN")


def main() -> None:
    """Main function."""
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
    )

    server_url = f"https://{NGROK_DOMAIN}/mcp"

    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=[{"role": "user", "content": "Greet Veit, Alejandro and Lukasz"}],
        tools=[
            {
                "type": "mcp",
                "server_url": server_url,
                "server_label": "mcp-demo-server",
                "require_approval": "never",
            },
        ],
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
