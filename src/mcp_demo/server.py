"""MCP demo server with FastMCP."""

from fastmcp import FastMCP

mcp = FastMCP("mcp-demo-server")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Greet a person."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()


# Hint: connect Claude code to this MCP server using ~/.claude.json
# Hint: see https://gofastmcp.com/integrations/fastapi for fastAPI integration
