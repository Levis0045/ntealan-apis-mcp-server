"""
Client test script for NTeALan REST API MCP Server.

This script demonstrates how to connect to the MCP server, 
list available resources, and read resources using SSE transports.

Usage:
    uv run python examples/run_resources.py

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
static_roots: RootsList = [str(Path(__file__).parent.parent)]

# --- Transport configurations: Only SSE for the moment ---

# SSETransport: for connecting to a running server via SSE
sse_url = "http://127.0.0.1:8000/sse"
headers = {"Authorization": "Bearer mytoken"}
transport_sse = SSETransport(url=sse_url, headers=headers)

# Create a client instance (default: SSE)
# Issue with roots:static_roots in the last version of fastmcp
client = Client(transport_sse)

async def get_avalaible_resources():
    """
    List all available tools and resources from the MCP server.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        resources = await client.list_resources()
        logger.info(f"Available resources: {resources}")

async def read_resource(name: str):
    """
    Read a resource by its URI or name.
    Args:
        name (str): The resource URI or name.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        result = await client.read_resource(name)
        logger.info(result)



if __name__ == "__main__":
    # Uncomment the function you want to test

    # List all tools and resources
    # asyncio.run(get_avalaible_resources())

    # Test -- Article resources calls --
    asyncio.run(read_resource("ntealan-apis://greeting/Elvis"))
    # asyncio.run(read_resource("ntealan-apis://articles?limit=2"))
    # asyncio.run(read_resource("ntealan-apis://articles/yb_fr_3031/0facf001-cb58-42c5-82b8-cd2dd2099967?none"))
    # asyncio.run(read_resource("ntealan-apis://articles/yb_fr_3031?limit=2"))
    # asyncio.run(read_resource("ntealan-apis://articles/statistics/yb_fr_3031"))
    # asyncio.run(read_resource("ntealan-apis://articles/statistics"))

    # Test -- Contribution resources calls --
    # asyncio.run(read_resource("ntealan-apis://contributions/yb_fr_3031/0facf001-cb58-42c5-82b8-cd2dd2099967"))

    # Test -- Metadata resources calls --
    # asyncio.run(read_resource("ntealan-apis://dictionaries/yb_fr_3031"))
    # asyncio.run(read_resource("ntealan-apis://dictionaries?limit=2"))
    # asyncio.run(read_resource("ntealan-apis://dictionaries/statistics/yb_fr_3031"))
    # asyncio.run(read_resource("ntealan-apis://dictionaries/statistics"))
