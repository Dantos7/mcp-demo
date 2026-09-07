"""MCP demo server with FastMCP."""

# ruff: noqa: T201 (allow print in this simple example)

import os

import ngrok
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

NGROK_DOMAIN = os.getenv("NGROK_DOMAIN")

mcp = FastMCP("mcp-demo-server")


def connect_ngrok() -> None:
    """Forward the server to ngrok to make it accessible from the internet (Groq is an external service, it can't see localhost)."""
    forwarder = ngrok.forward("localhost:8000", authtoken_from_env=True, domain=NGROK_DOMAIN)
    print(f"Available at: {forwarder.url()}")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    if NGROK_DOMAIN:
        connect_ngrok()
    mcp.run(transport="http")


# Hint: connect Claude code to this MCP server using ~/.claude.json
# Hint: see https://gofastmcp.com/integrations/fastapi for fastAPI integration
