from uuid import UUID

from fastmcp import Context

from ntealan_apis_mcp.common.http_session import run_resource_aiohttp_session
from ntealan_apis_mcp.common.utils import check_and_make_url_params
from ntealan_apis_mcp.models.common import McpResourceResponse


# Add a dynamic greeting resource
async def get_article_by_id(
    dictionary_id: str,
    article_id: UUID,
    params: str="none",
    ctx: Context=None
) -> McpResourceResponse:
    """
    Retrieve an article by its unique identifier.

    Args:
        dictionary_id (str): The unique identifier of the dictionary containing the article.
        article_id (UUID): The unique identifier of the article to retrieve.
        params (str, optional): Additional URL parameters for the request.
        ctx (Context, optional): The context object containing request-specific information.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation, the article data,
        error information (if any), and context metadata.

    Example:
        result = await get_article_by_id("12345", some_article_uuid, ctx=ctx)
        print(result)
    """
    # Report initial progress
    await ctx.report_progress(1, 3)
    # Build the URL path for the article request
    url_path = check_and_make_url_params(
        f"dictionaries/articles/{dictionary_id}/{article_id}",
        params
    )
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3)
    # Log the response status
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    # Handle non-200 responses as errors
    if response.status != 200:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    # Log successful status
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Final progress report
    await ctx.report_progress(3, 3)
    # Parse the JSON response
    json_response = await response.json()
    # Return the article data in a standardized response format
    return {
        "status": "OK",
        "data": json_response.get("article", [])
    }

async def get_all_articles(
    params: str="none",
    ctx: Context=None
) -> McpResourceResponse:
    """
    Retrieve all articles.

    Args:
        params (str, optional): Additional URL parameters for the request.
        ctx (Context, optional): The context object containing client and request information.

    Returns:
        McpResourceResponse: A dictionary containing the status, articles data,
        error information (if any), and context metadata.
    """
    # Report initial progress
    await ctx.report_progress(1, 3)
    # Build the URL path for the articles request
    url_path = check_and_make_url_params(
        "dictionaries/articles",
        params
    )
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3)
    # Log the response status
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    # Handle non-200 responses as errors
    if response.status != 200:
        await ctx.error(f"Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    # Log successful status
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Final progress report
    await ctx.report_progress(3, 3)
    # Parse the JSON response
    json_response = await response.json()
    # Return the articles data in a standardized response format
    return {
        "status": "OK",
        "data": json_response.get("articles", [])
    }

async def get_all_articles_with_dictionary_id(
    dictionary_id: str,
    params: str="none",
    ctx: Context=None
) -> McpResourceResponse:
    """
    Retrieve all articles associated with a specific dictionary ID.

    Args:
        dictionary_id (str): The unique identifier of the dictionary whose articles are to be retrieved.
        params (str, optional): Additional URL parameters for the request.
        ctx (Context, optional): The context object containing metadata such as client ID and request ID.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation, the retrieved articles,
        error information (if any), and context metadata.
    """
    # Report initial progress
    await ctx.report_progress(1, 3)
    # Build the URL path for the articles request
    url_path = check_and_make_url_params(
        f"dictionaries/articles/{dictionary_id}",
        params
    )
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3)
    # Log the response status
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    # Handle non-200 responses as errors
    if response.status != 200:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    # Log successful status
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Final progress report
    await ctx.report_progress(3, 3)
    # Parse the JSON response
    json_response = await response.json()
    # Return the articles data in a standardized response format
    return {
        "status": "OK",
        "data": json_response.get("articles", [])
    }

async def get_statistics_for_articles_by_dictionary(
    dictionary_id: UUID,
    ctx: Context=None
) -> McpResourceResponse:
    """
    Retrieve statistics for articles associated with a specific dictionary by its ID.

    Args:
        dictionary_id (UUID): The unique identifier of the dictionary.
        ctx (Context, optional): The context object containing client and request metadata.

    Returns:
        McpResourceResponse: A response object containing the status, statistics data, 
        error details (if any), and metadata such as client_id and request_id.
    """
    # Report initial progress
    await ctx.report_progress(1, 3)
    # Build the URL path for the statistics request
    url_path = f"dictionaries/metadata/{dictionary_id}"
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3)
    # Log the response status
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    # Handle non-200 responses as errors
    if response.status != 200:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    # Log successful status
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Final progress report
    await ctx.report_progress(3, 3)
    # Parse the JSON response
    json_response = await response.json()
    # Return the statistics data in a standardized response format
    return {
        "status": "OK",
        "data": json_response.get("metadata", {}).get("statistics")
    }

async def get_statistics_for_articles(
    ctx: Context=None
) -> McpResourceResponse:
    """
    Retrieve statistics for all articles.

    Args:
        ctx (Context, optional): The context object containing client and request information.

    Returns:
        McpResourceResponse: A dictionary containing the status, statistics data, error details, 
        client ID, and request ID.
    """
    # Report initial progress
    await ctx.report_progress(1, 3)
    # Build the URL path for the statistics request
    url_path = "dictionaries/core/statistics"
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3)
    # Log the response status
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    # Handle non-200 responses as errors
    if response.status != 200:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    # Log successful status
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Final progress report
    await ctx.report_progress(3, 3)
    # Parse the JSON response
    json_response = await response.json()
    # Return the statistics data in a standardized response format
    return {
        "status": "OK",
        "data": json_response
    }
