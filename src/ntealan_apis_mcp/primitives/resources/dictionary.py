from uuid import UUID

from fastmcp import Context

from ntealan_apis_mcp.common.http_session import run_resource_aiohttp_session
from ntealan_apis_mcp.common.utils import check_and_make_url_params
from ntealan_apis_mcp.models.common import McpResourceResponse


# Add a dynamic greeting resource
async def get_metadata_dictionary_by_id(
    dictionary_id: UUID,
    ctx: Context
) -> McpResourceResponse:
    """
    Retrieve metadata for a dictionary by its unique identifier.

    Args:
        dictionary_id (UUID): The unique identifier of the dictionary.
        ctx (Context): The context object containing request-specific information.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation,
        the retrieved metadata, error information (if any), and context metadata.

    Example:
        result = await get_metadata_dictionary_by_id(some_uuid, ctx)
        print(result)
    """
    # Report initial progress
    await ctx.report_progress(1, 3) # Report completion
    # Build the URL path for the metadata request
    url_path = f"dictionaries/metadata/{dictionary_id}"
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3) # Report completion
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
    await ctx.report_progress(3, 3) # Report completion
    # Parse the JSON response
    json_response = await response.json()
    # Return the metadata in a standardized response format
    return {
        "status": "OK",
        "data": json_response.get("metadata", [])
    }

async def get_all_metadata_dictionaries(params: str, ctx: Context) -> McpResourceResponse:
    """
    Retrieve all metadata dictionaries.

    Args:
        params (str): Additional URL parameters for the request.
        ctx (Context): The context object containing request-specific information.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation,
        the retrieved metadata list, error information (if any), and context metadata.

    Example:
        result = await get_all_metadata_dictionaries("limit=10", ctx)
        print(result)
    """
    # Report initial progress
    await ctx.report_progress(1, 3) # Report completion
    # Build the URL path for the metadata dictionaries request
    url_path = check_and_make_url_params(
        "dictionaries/metadata",
        params
    )
    # Log the request execution
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    # Perform the HTTP GET request
    response = await run_resource_aiohttp_session(url_path)
    # Report progress after request
    await ctx.report_progress(2, 3) # Report completion
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
    await ctx.report_progress(3, 3) # Report completion
    # Parse the JSON response
    json_response = await response.json()
    # Return the metadata list in a standardized response format
    return {
        "status": "OK",
        "data": json_response.get("metadata", [])
    }

async def get_statistics_metadata_dictionaries(ctx: Context) -> McpResourceResponse:
    """
    Fetches metadata dictionaries statistics from the system.

    This asynchronous function performs a GET request to retrieve metadata dictionaries
    statistics. It reports progress at various stages, logs information, and handles
    errors appropriately.

    Args:
        ctx (Context): The context object containing request-specific information
            and utility methods for logging and progress reporting.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation,
            the retrieved data (if successful), or error details in case of failure.
    """

    await ctx.report_progress(1, 3) # Report completion
    url_path = "dictionaries/metadata"
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    response = await run_resource_aiohttp_session(url_path)
    await ctx.report_progress(2, 3) # Report completion
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    if response.status != 200:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Perform checks
    await ctx.report_progress(3, 3) # Report completion
    json_response = await response.json()
    return {
        "status": "OK",
        "data": json_response
    }

async def get_statistics_metadata_dictionary_by_id(
    dictionary_id: UUID,
    ctx: Context
) -> McpResourceResponse:
    """
    Fetches the statistics metadata for a dictionary by its ID.

    This asynchronous function retrieves metadata statistics for a specific dictionary
    using its unique identifier. It reports progress at various stages, logs information
    about the request and response, and handles errors appropriately.

    Args:
        dictionary_id (UUID): The unique identifier of the dictionary.
        ctx (Context): The context object containing request and logging utilities.

    Returns:
        McpResourceResponse: A dictionary containing the status of the operation, 
        the retrieved data (if successful), or error details in case of failure.
    """
    await ctx.report_progress(1, 3) # Report completion
    url_path = f"dictionaries/metadata/{dictionary_id}"
    await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
    response = await run_resource_aiohttp_session(url_path)
    await ctx.report_progress(2, 3) # Report completion
    await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
    if response.status != 200:
        await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
        return {
            "status": "ERROR",
            "data": None,
            "error_code": response.status,
            "error_message": response.reason
        }
    await ctx.info(f"[{ctx.request_id}] System status is OK.")
    # Perform checks
    json_response = await response.json()
    await ctx.report_progress(3, 3) # Report completion
    return {
        "status": "OK",
        "data": json_response.get("metadata").get("statistics")
    }
