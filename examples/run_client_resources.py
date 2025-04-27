"""
Client test script for NTeALan REST API MCP Server.

This script demonstrates how to connect to the
MCP server, list available resources, and read
resources using SSE transports.

Usage:
    uv run python examples/run_resources.py

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
static_roots: RootsList = [str(Path(__file__).parent.parent)]


async def get_avalaible_resources(client):
    """
    List all available tools and resources from the MCP server.
    """
    async with client:
        logger.info(f"Client connected: {client.is_connected()}")
        resources = await client.list_resources()
        logger.info(f"Available resources: {resources}")


async def read_resource(client, name: str):
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
    parser = argparse.ArgumentParser(
        prog="ntealan-apis-mcp",
        description="Sample of NTeALan MCP server client",
        epilog="NTeALan Dictionary Platform - API MCP Server",
    )
    parser.add_argument("-t", "--transport", default="sse", choices=["sse", "stdio"])
    parser.add_argument("-e", "--env", default="local", choices=["local", "prod"])
    parser.add_argument("-s", "--seq", default=1, type=int)
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

    # Create a client instance (default: SSE)
    # Issue with roots:static_roots in the last version of fastmcp
    client = Client(transport)

    # List all tools and resources
    if args.seq == 0:
        asyncio.run(get_avalaible_resources(client))

    # Test -- Article resources calls --
    if args.seq == 1:
        asyncio.run(read_resource(client, "ntealan-apis://greeting/Elvis"))
    if args.seq == 2:
        asyncio.run(read_resource(client, "ntealan-apis://articles?limit=2"))
    if args.seq == 3:
        asyncio.run(
            read_resource(
                client,
                "ntealan-apis://articles/yb_fr_3031/0facf001-cb58-42c5-82b8-cd2dd2099967?none",
            )
        )
    if args.seq == 4:
        asyncio.run(read_resource(client, "ntealan-apis://articles/yb_fr_3031?limit=2"))
    if args.seq == 5:
        asyncio.run(read_resource(client, "ntealan-apis://articles/statistics/yb_fr_3031"))
    if args.seq == 6:
        asyncio.run(read_resource(client, "ntealan-apis://articles/statistics"))

    # Test -- Contribution resources calls --
    if args.seq == 7:
        asyncio.run(
            read_resource(
                client,
                "ntealan-apis://contributions/yb_fr_3031/0facf001-cb58-42c5-82b8-cd2dd2099967",
            )
        )

    # Test -- Metadata resources calls --
    if args.seq == 8:
        asyncio.run(read_resource(client, "ntealan-apis://dictionaries/yb_fr_3031"))
    if args.seq == 9:
        asyncio.run(read_resource(client, "ntealan-apis://dictionaries?limit=2"))
    if args.seq == 10:
        asyncio.run(read_resource(client, "ntealan-apis://dictionaries/statistics/yb_fr_3031"))
    if args.seq == 11:
        asyncio.run(read_resource(client, "ntealan-apis://dictionaries/statistics"))
