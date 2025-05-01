import argparse

from fastmcp.server import FastMCP

# Get mcp resources
from ntealan_apis_mcp.primitives.resources.article import add_article_resources_to_server
from ntealan_apis_mcp.primitives.resources.contribution import add_contribution_resources_to_server
from ntealan_apis_mcp.primitives.resources.dictionary import add_dictionary_resources_to_server

# Get mcp tools
from ntealan_apis_mcp.primitives.tools.article import add_article_tools_to_server
from ntealan_apis_mcp.primitives.tools.contribution import add_contribution_tools_to_server
from ntealan_apis_mcp.primitives.tools.dictionary import add_dictionary_tools_to_server

# ------ Create an MCP server ------

ntl_mcp_server = FastMCP(
    "NTeALan REST API MCP Server",
    "This is simple MCP server for NTeALan REST API dictionaries",
    dependencies=["ntealan_apis_mcp", "aiohttp", "pydantic", "aiodns", "python-dotenv"],
    on_duplicate_resources="error",  # Raise error on duplicates
)

# Add a dynamic dictionary tools
add_dictionary_tools_to_server(ntl_mcp_server)

# Add a dynamic article tools
add_article_tools_to_server(ntl_mcp_server)

# Add a dynamic contribution tools
add_contribution_tools_to_server(ntl_mcp_server)

# Add a dynamic article resources
add_article_resources_to_server(ntl_mcp_server)

# Add a dynamic contribution resources
add_contribution_resources_to_server(ntl_mcp_server)

# Add a dynamic dictionary metadata resources
add_dictionary_resources_to_server(ntl_mcp_server)

# Add a dynamic greeting resource
ntl_mcp_server.add_resource_fn(
    lambda name: f"Hello, {name} from NTeALan!",
    name="greeting",
    uri="ntealan-apis://greeting/{name}",
    description="Get a personalized greeting with default value",
    tags=["default-endpoint", "mcp-resource"],
    mime_type="text/plain",
)


# ------ Run NTeALan API MCP Server ------


def run_mcp_server():
    """
    Run the MCP server with the specified transport.
    """
    parser = argparse.ArgumentParser(
        prog="ntealan-apis-mcp",
        description="""
                    A modular, extensible MCP (Model Context Protocol)
                    server for NTeALan REST APIs dictionaries and contributions.
                    This project provides a unified interface for managing
                    dictionary data, articles, and user contributions, and
                    is designed for easy integration and extension.
                    """,
        epilog="NTeALan Dictionary Platform - API MCP Server",
    )
    parser.add_argument("-t", "--transport", default="sse", choices=["sse", "stdio"])
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    # sse_url = "http://localhost:8000/sse"
    # headers = {"Authorization": "Bearer mytoken"}
    # transport = SSETransport(url=sse_url, headers=headers)

    ntl_mcp_server.run(transport=args.transport)


if __name__ == "__main__":
    run_mcp_server()
