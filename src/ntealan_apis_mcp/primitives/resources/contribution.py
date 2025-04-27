from uuid import UUID

from fastmcp import Context

from ntealan_apis_mcp.common.http_session import run_resource_aiohttp_session
from ntealan_apis_mcp.models.common import McpResourceResponse


# Add a dynamic contribution resource
async def get_contribution_by_dictionary_id(
    dictionary_id: str,
    contribution_id: UUID,
    ctx: Context = None
) -> McpResourceResponse:
    """
    Retrieve a contribution by its unique identifier within a specific dictionary.

    Args:
        dictionary_id (str): The unique identifier of the dictionary.
        contribution_id (UUID): The unique identifier of the contribution.
        ctx (Context): The context object containing request-specific information.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation, 
                             system load, and client-specific information.

    Example:
        result = await get_contribution_by_dictionary_id("12345", UUID("abcd-1234"), ctx)
        print(result)
    """
    # Report initial progress
    await ctx.report_progress(1, 3)
    url_path = f"dictionaries/articles/{dictionary_id}/contributions/{contribution_id}"
    await ctx.info(f"[{ctx.request_id}] Execute GET request: {url_path}...")

    # Make the HTTP request
    response = await run_resource_aiohttp_session(url_path)

    # Report intermediate progress
    await ctx.report_progress(2, 3)
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")

    # Handle non-successful responses
    if response.status not in [200, 206]:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }

    # Log successful status
    await ctx.info(f"[{ctx.request_id}] System status is OK.")

    # Report final progress
    await ctx.report_progress(3, 3)

    # Parse the JSON response
    json_response = await response.json()
    return {
        "status": "OK",
        "data": json_response
    }


# Placeholder functions for other contribution-related operations
def get_contribution_by_id(article_id: UUID, ctx: Context = None) -> str:
    """
    Retrieve a contribution by its unique identifier.

    Args:
        article_id (UUID): The unique identifier of the article.
        ctx (Context): The context object containing request-specific information.

    Returns:
        str: A placeholder response.
    """
    return f"Hello, {article_id}!"


def get_contributions_by_dictionary(article_id: UUID) -> str:
    """
    Retrieve all contributions for a specific dictionary.

    Args:
        article_id (UUID): The unique identifier of the article.

    Returns:
        str: A placeholder response.
    """
    return f"Hello, {article_id}!"


def get_contributions_by_article() -> str:
    """
    Retrieve all contributions for a specific article.

    Returns:
        str: A placeholder response.
    """
    return "Hello, contributions by article!"


def get_contributions_by_dictionary_and_article(dictionary_id: UUID) -> str:
    """
    Retrieve contributions for a specific dictionary and article.

    Args:
        dictionary_id (UUID): The unique identifier of the dictionary.

    Returns:
        str: A placeholder response.
    """
    return f"Hello, {dictionary_id}!"


def get_all_contributions(dictionary_id: UUID) -> str:
    """
    Retrieve all contributions for a specific dictionary.

    Args:
        dictionary_id (UUID): The unique identifier of the dictionary.

    Returns:
        str: A placeholder response.
    """
    return f"Hello, {dictionary_id}!"


def get_statistics_for_contributions_by_dictionary() -> str:
    """
    Retrieve statistics for contributions grouped by dictionary.

    Returns:
        str: A placeholder response.
    """
    return "Hello, statistics for contributions by dictionary!"


def get_statistics_for_contributions_by_article() -> str:
    """
    Retrieve statistics for contributions grouped by article.

    Returns:
        str: Retrieve statistics for contributions grouped by article.

    """
    return "Hello, statistics for contributions by article!"
