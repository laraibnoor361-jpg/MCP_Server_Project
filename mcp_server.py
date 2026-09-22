from fastmcp import FastMCP
from datetime import datetime

# ---------------------------------------------------
# Simple MCP Server using FastMCP
# Beginner friendly version - easy to read and edit
#
# What is MCP?
# MCP (Model Context Protocol) is a standard way for an AI
# assistant to call "tools" that live on a separate server.
# This file IS that server - it exposes a few simple tools
# that any MCP-compatible client (like Claude Desktop, or
# our own client_demo.py) can call.
# ---------------------------------------------------

mcp = FastMCP("My Student MCP Server")


@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@mcp.tool
def calculator(expression: str) -> str:
    """Evaluate a simple math expression, e.g. '25 * 4 + 10'."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Could not calculate that: {e}"


@mcp.tool
def get_current_time() -> str:
    """Get the current date and time."""
    return datetime.now().strftime("%A, %d %B %Y - %I:%M %p")


@mcp.tool
def word_counter(text: str) -> str:
    """Count the number of words and characters in the given text."""
    words = len(text.split())
    characters = len(text)
    return f"Words: {words}, Characters: {characters}"


# This makes the server run when you do: python mcp_server.py
if __name__ == "__main__":
    mcp.run()
