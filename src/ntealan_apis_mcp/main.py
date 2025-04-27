import argparse

from fastmcp.server import FastMCP

# from fastmcp.client.transports import SSETransport
# import asyncio
# Get mcp resources
from ntealan_apis_mcp.primitives.resources.article import (
    get_all_articles,
    get_all_articles_with_dictionary_id,
    get_article_by_id,
    get_statistics_for_articles,
    get_statistics_for_articles_by_dictionary,
)
from ntealan_apis_mcp.primitives.resources.contribution import get_contribution_by_dictionary_id
from ntealan_apis_mcp.primitives.resources.dictionary import (
    get_all_metadata_dictionaries,
    get_metadata_dictionary_by_id,
    get_statistics_metadata_dictionaries,
    get_statistics_metadata_dictionary_by_id,
)
from ntealan_apis_mcp.primitives.tools.article import (
    create_article,
    delete_article,
    update_article,
)
from ntealan_apis_mcp.primitives.tools.contribution import (
    create_contribution,
    delete_contribution,
    update_contribution,
)

# Get mcp tools
from ntealan_apis_mcp.primitives.tools.dictionary import (
    create_dictionary,
    delete_dictionary,
    update_dictionary,
)

# ------ Create an MCP server ------

ntl_mcp_server = FastMCP(
    "NTeALan REST API MCP Server",
    "This is simple MCP server for NTeALan REST API dictionaries",
    dependencies=["ntealan_apis_mcp", "aiohttp", "pydantic", "aiodns", "python-dotenv"],
    on_duplicate_resources="error",  # Raise error on duplicates
)

# ------ Add a dynamic dictionary tools ------

ntl_mcp_server.add_tool(
    create_dictionary,
    description="Create a new dictionary",
    tags=["mcp-tool", "dictionary-endpoint"],
)
ntl_mcp_server.add_tool(
    update_dictionary,
    description="Update an existing dictionary",
    tags=["dictionary-endpoint", "mcp-tool"],
)

ntl_mcp_server.add_tool(
    delete_dictionary,
    description="Delete an existing dictionary",
    tags=["dictionary-endpoint", "mcp-tool"],
)
# Add a dynamic article tools
ntl_mcp_server.add_tool(
    create_article, description="Create a new article", tags=["article-endpoint", "mcp-tool"]
)
ntl_mcp_server.add_tool(
    update_article, description="Update an existing article", tags=["article-endpoint", "mcp-tool"]
)
ntl_mcp_server.add_tool(
    delete_article, description="Delete an existing article", tags=["article-endpoint", "mcp-tool"]
)
# Add a dynamic contribution tools
ntl_mcp_server.add_tool(
    create_contribution,
    description="Create a new contribution",
    tags=["contribution-endpoint", "mcp-tool"],
)
ntl_mcp_server.add_tool(
    update_contribution,
    description="Update an existing contribution",
    tags=["contribution-endpoint", "mcp-tool"],
)
ntl_mcp_server.add_tool(
    delete_contribution,
    description="Delete an existing contribution",
    tags=["contribution-endpoint", "mcp-tool"],
)

# ------ Add a dynamic article resources -------

ntl_mcp_server.add_resource_fn(
    lambda params: get_all_articles(params, ntl_mcp_server.get_context()),
    name="get_all_articles",
    uri="ntealan-apis://articles?{params}",
    tags=["article-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get all articles",
)
ntl_mcp_server.add_resource_fn(
    lambda dictionary_id, article_id, params: get_article_by_id(
        dictionary_id, article_id, params, ntl_mcp_server.get_context()
    ),
    name="get_article_by_id",
    uri="ntealan-apis://articles/{dictionary_id}/{article_id}?{params}",
    tags=["article-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get an article by ID",
)
ntl_mcp_server.add_resource_fn(
    lambda dictionary_id, params: get_all_articles_with_dictionary_id(
        dictionary_id, params, ntl_mcp_server.get_context()
    ),
    name="get_all_articles_with_dictionary_id",
    uri="ntealan-apis://articles/{dictionary_id}?{params}",
    tags=["article-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get all articles with dictionary ID",
)
ntl_mcp_server.add_resource_fn(
    lambda dictionary_id: get_statistics_for_articles_by_dictionary(
        dictionary_id, ntl_mcp_server.get_context()
    ),
    name="get_statistics_for_articles_by_dictionary",
    uri="ntealan-apis://articles/statistics/{dictionary_id}",
    tags=["article-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get articles by dictionary count",
)
# ntealan API Token required
ntl_mcp_server.add_resource_fn(
    lambda: get_statistics_for_articles(ntl_mcp_server.get_context()),
    name="get_statistics_for_articles",
    uri="ntealan-apis://articles/statistics",
    tags=["article-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get articles count",
)

# ------ Add a dynamic contribution resources ------

ntl_mcp_server.add_resource_fn(
    lambda dictionary_id, contribution_id: get_contribution_by_dictionary_id(
        dictionary_id, contribution_id, ntl_mcp_server.get_context()
    ),
    name="get_contribution_by_dictionary_id",
    uri="ntealan-apis://contributions/{dictionary_id}/{contribution_id}",
    tags=["contribution-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get contributions by dictionary",
)

# ------ Add a dynamic dictionary metadata resources ------

ntl_mcp_server.add_resource_fn(
    lambda dictionary_id: get_metadata_dictionary_by_id(
        dictionary_id, ntl_mcp_server.get_context()
    ),
    name="get_metadata_dictionary_by_id",
    uri="ntealan-apis://dictionaries/{dictionary_id}",
    tags=["dictionary-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get metadata dictionary by ID",
)
ntl_mcp_server.add_resource_fn(
    lambda params: get_all_metadata_dictionaries(params, ntl_mcp_server.get_context()),
    name="get_all_metadata_dictionaries",
    uri="ntealan-apis://dictionaries?{params}",
    tags=["dictionary-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get all metadata dictionaries",
)
ntl_mcp_server.add_resource_fn(
    lambda: get_statistics_metadata_dictionaries(ntl_mcp_server.get_context()),
    name="get_statistics_metadata_dictionaries",
    uri="ntealan-apis://dictionaries/statistics",
    tags=["dictionary-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get metadata dictionaries statistics",
)
ntl_mcp_server.add_resource_fn(
    lambda dictionary_id: get_statistics_metadata_dictionary_by_id(
        dictionary_id, ntl_mcp_server.get_context()
    ),
    name="get_statistics_metadata_dictionary_by_id",
    uri="ntealan-apis://dictionaries/statistics/{dictionary_id}",
    tags=["dictionary-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get metadata dictionary statistics by ID",
)

# ------ Add a dynamic greeting resource ------

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
