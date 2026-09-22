import asyncio
from fastmcp import Client
from mcp_server import mcp

# ---------------------------------------------------
# Simple MCP Client - Demo
# Beginner friendly version - easy to read and edit
#
# This connects to our own mcp_server.py (in the same process,
# for an easy demo) and calls each tool, printing the result.
#
# In real use, a client usually connects to a server running
# separately (another process, or over the network) - but
# connecting directly like this is the simplest way to prove
# the server and its tools actually work.
# ---------------------------------------------------


async def main():
    # Client(mcp) connects straight to our FastMCP server object
    async with Client(mcp) as client:

        print("--- Available tools on the server ---")
        tools = await client.list_tools()
        for t in tools:
            print(f"- {t.name}: {t.description}")

        print("\n--- Calling add_numbers(5, 7) ---")
        result = await client.call_tool("add_numbers", {"a": 5, "b": 7})
        print("Result:", result.data)

        print("\n--- Calling calculator('12 * 3 + 4') ---")
        result = await client.call_tool("calculator", {"expression": "12 * 3 + 4"})
        print("Result:", result.data)

        print("\n--- Calling get_current_time() ---")
        result = await client.call_tool("get_current_time", {})
        print("Result:", result.data)

        print("\n--- Calling word_counter('MCP projects are fun to build') ---")
        result = await client.call_tool(
            "word_counter", {"text": "MCP projects are fun to build"}
        )
        print("Result:", result.data)


if __name__ == "__main__":
    asyncio.run(main())
