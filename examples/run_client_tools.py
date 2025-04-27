"""
Client test script for NTeALan REST API MCP Server.

This script demonstrates how to connect to the MCP server, list available tools 
and call tools using SSE transports.

Usage:
    uv run python examples/run_tools.py

Edit the script to test specific tools or resources as needed.
"""

import asyncio
import logging
from pathlib import Path

from fastmcp import Client
from fastmcp.client.roots import RootsList
from fastmcp.client.transports import SSETransport

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define static roots for the client
static_roots: RootsList = [str(Path(__file__).parent)]

# --- Transport configurations: Only SSE for the moment ---

# SSETransport: for connecting to a running server via SSE
sse_url = "http://127.0.0.1:8000/sse"
headers = {"Authorization": "Bearer mytoken"}
transport_sse = SSETransport(url=sse_url, headers=headers)

# Create a client instance (default: SSE)
# Issue with roots:static_roots in the last version of fastmcp
client = Client(transport_sse)

async def get_avalaible_tools():
    """
    List all available tools and resources from the MCP server.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        tools = await client.list_tools()
        logger.info(f"Available tools: {tools}")

async def call_tool(name: str, payload:dict):
    """
    Call a tool by name with example data.
    Args:
        name (str): The name of the tool to call.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        # Example payload for a dictionary tool
        result = await client.call_tool(
            name,
            payload
        )
        logger.info(result)


if __name__ == "__main__":
    # Uncomment the function you want to test

    # List all tools
    asyncio.run(get_avalaible_tools())

    # Call tool: "create_article"
    """
    payload = {
        "dictionary_id": "yb_fr_3031",
        "data": {
            "name": "Test Dictionary",
            "description": "This is a test dictionary",
            "created_at": "2023-10-01T12:00:00Z",
            "updated_at": "2023-10-01T12:00:00Z"
        }
    }
    asyncio.run(call_tool("create_article"), payload)
    """
