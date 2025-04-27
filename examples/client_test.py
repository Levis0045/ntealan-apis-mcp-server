"""
Client test script for NTeALan REST API MCP Server.

This script demonstrates how to connect to the MCP server, 
using different transports (stdio, uvx, SSE).

Usage:
    uv run python client_test.py

Edit the script to test specific tools or resources as needed.
"""

import logging
from pathlib import Path

from fastmcp import Client
from fastmcp.client.roots import RootsList
from fastmcp.client.transports import PythonStdioTransport, SSETransport, UvxStdioTransport

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define static roots for the client
static_roots: RootsList = [str(Path(__file__).parent)]

# --- Transport configurations ---

# UvxStdioTransport: for running as a package tool
transport_uvx = UvxStdioTransport(
    tool_name="ntealanmcp",
    from_package="ntealan_apis_mcp",  # Optionally specify package if tool name differs
    with_packages=["aiohttp", "lxml"],  # Add dependencies if needed
    tool_args=["--config-file", "prod.yaml"]  # Pass args to the tool itself
)

# PythonStdioTransport: for running a script directly

# Server script or tool name for different transports
server_script = "../src/ntealan_apis_mcp/main.py"  # For PythonStdioTransport

transport_stdio = PythonStdioTransport(
    script_path=server_script,
    python_cmd=".venv/bin/python3.11",  # Specify python version
    args=[],  # Pass args to the script
    env={
        "NTEALAN_BASE_API_URL": "https://apis.ntealan.net/ntealan",
        "NTEALAN_API_TIMEOUT": 30,
        "NTEALAN_API_RETRIES": 3,
        "NTEALAN_API_RETRY_DELAY": 5
    },  # Set environment variables
    cwd=static_roots[0]  # Set working directory
)

# SSETransport: for connecting to a running server via SSE
sse_url = "http://127.0.0.1:8000/sse"
headers = {"Authorization": "Bearer mytoken"}
transport_sse = SSETransport(url=sse_url, headers=headers)

# Create a client instance (default: SSE)
client = Client(transport_sse, roots=static_roots)
print(dir(client))
print(client.transport)
print(client.transport.url)
print(client.transport.headers)
print(client.transport._session)
