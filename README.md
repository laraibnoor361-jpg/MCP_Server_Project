# MCP Project (Model Context Protocol Server)

A beginner-friendly MCP server built with FastMCP, plus a demo client
that proves it works.

## What is MCP?
MCP (Model Context Protocol) is a standard way for an AI assistant to
call "tools" that live on a separate server, instead of the tools
being hardcoded inside the AI app itself. This makes tools reusable
across many different AI apps (Claude Desktop, custom agents, etc.)

## What's in this project
- `mcp_server.py` — the MCP server. It exposes 4 tools:
  - `add_numbers` — adds two numbers
  - `calculator` — evaluates a math expression
  - `get_current_time` — returns today's date and time
  - `word_counter` — counts words and characters in text
- `client_demo.py` — a script that connects to the server and calls
  every tool, printing the results, to prove the server works.

## How to run it

1. Install requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the demo client (this automatically starts the server too,
   since they run in the same process for this simple demo):
   ```
   python client_demo.py
   ```
   You should see the list of tools and each tool's result printed.

3. (Optional) Run the server on its own, so other MCP clients (like
   Claude Desktop) can connect to it:
   ```
   python mcp_server.py
   ```

## Connecting this server to Claude Desktop (optional, for submission)
Add this to your Claude Desktop MCP config file:
```json
{
  "mcpServers": {
    "student-mcp-server": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```
After restarting Claude Desktop, its 4 tools (add_numbers, calculator,
get_current_time, word_counter) become available for Claude to call.

## How it works
- `@mcp.tool` turns a normal Python function into an MCP tool —
  FastMCP automatically generates the schema from the function's
  type hints and docstring.
- `Client(mcp)` connects a client directly to the server object for
  an easy local demo. In production, a client usually connects to a
  server running as a separate process or over a network instead.
