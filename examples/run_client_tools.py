"""
Client test script for NTeALan REST API MCP Server.

This script demonstrates how to connect to the MCP server,
list available tools and call tools using SSE transports.

Usage:
    uv run python examples/run_client_tools.py

Edit the script to test specific tools or resources as needed.
"""

import argparse
import asyncio
import logging
from os import environ
from pathlib import Path

from fastmcp import Client
from fastmcp.client.roots import RootsList
from fastmcp.client.transports import SSETransport

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define static roots for the client
static_roots: RootsList = [str(Path(__file__).parent)]


async def get_avalaible_tools(client):
    """
    List all available tools and resources from the MCP server.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        tools = await client.list_tools()
        logger.info(f"Available tools: {tools}")


async def call_tool(client, name: str, payload: dict):
    """
    Call a tool by name with example data.
    Args:
        name (str): The name of the tool to call.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        # Example payload for a dictionary tool
        result = await client.call_tool(name, payload)
        logger.info(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ntealan-apis-mcp",
        description="Sample of NTeALan MCP server client",
        epilog="NTeALan Dictionary Platform - API MCP Server",
    )
    parser.add_argument("-t", "--transport", default="sse", choices=["sse", "stdio"])
    parser.add_argument("-e", "--env", default="local", choices=["local", "prod"])
    parser.add_argument("-s", "--seq", default=1, type=int, description="Sequence number to run")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    if args.transport == "sse":
        # SSETransport: for connecting to a running server via SSE
        headers = {"Authorization": "Bearer mytoken"}
        if args.env == "prod":
            host_sse_url = "https://apis.ntealan.net/ntealan/mcpserver/sse"
            environ["FASTMCP_SERVER_MESSAGE_PATH"] = "/messages/"
            environ["FASTMCP_SERVER_SSE_PATH"] = "/sse"
            environ["FASTMCP_SERVER_HOST"] = "https://apis.ntealan.net/ntealan/mcpserver"
            transport = SSETransport(url=host_sse_url, headers=headers)
        else:
            local_sse_url = "http://127.0.0.1:8000/sse"
            transport = SSETransport(url=local_sse_url, headers=headers)
    else:
        transport = "stdio"

    client = Client(transport)
    # Uncomment the function you want to test

    # List all tools
    if args.seq == 0:
        asyncio.run(get_avalaible_tools(client))

    # Call tool: "create_article"
    if args.seq == 1:
        # Example payload for creating an article
        payload = {
            "dictionary_id": "yb_fr_3031",
            "data": {
                "title": "Test Article",
                "content": "This is a test article",
                "created_at": "2023-10-01T12:00:00Z",
                "updated_at": "2023-10-01T12:00:00Z",
            },
        }
        asyncio.run(call_tool(client, "create_article"), payload)
