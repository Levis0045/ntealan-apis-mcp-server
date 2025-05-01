from fastmcp import Context

from ntealan_apis_mcp.common.http_session import run_resource_aiohttp_session
from ntealan_apis_mcp.common.utils import check_and_make_url_params
from ntealan_apis_mcp.models.common import McpResourceResponse


def add_dictionary_resources_to_server(ntl_mcp_server):
    """
    Add dictionary resources to the NTeALan MCP server.

    This function registers various dictionary-related resources
    with the NTeALan MCP server, allowing for retrieval of metadata,
    statistics, and other information related to dictionaries.

    Args:
        ntl_mcp_server (MCPServer): The NTeALan MCP server instance.

    Returns:
        None
    """

    @ntl_mcp_server.resource(
        uri="ntealan-apis://dictionaries/metadata/{dictionary_id}",
        tags=["dictionary-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_metadata_dictionary_by_id(
        dictionary_id: str, ctx: Context
    ) -> McpResourceResponse:
        """
        Retrieve metadata for a dictionary by its unique identifier.

        Args:
            dictionary_id (str): The unique identifier of the dictionary.
            ctx (Context): The context object with request-specific information.

        Returns:
            McpResourceResponse: A dictionary containing the status
            of the operation,the retrieved metadata, error information
            (if any), and context metadata.

        Example:
            result = await get_metadata_dictionary_by_id(some_uuid, ctx)
            print(result)
        """
        await ctx.report_progress(1, 3)
        url_path = f"dictionaries/metadata/{dictionary_id}"
        url_path = check_and_make_url_params(url_path, "none")
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        response = await run_resource_aiohttp_session(url_path)
        await ctx.report_progress(2, 3)
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        if response.status != 200:
            await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
            return {
                "status": "ERROR",
                "data": None,
                "error_code": response.status,
                "error_message": response.reason,
            }
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        await ctx.report_progress(3, 3)
        json_response = await response.json()
        return {"status": "OK", "data": json_response.get("metadata", [])}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://dictionaries?{params}",
        tags=["dictionary-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_all_metadata_dictionaries(params: str, ctx: Context) -> McpResourceResponse:
        """
        Retrieve all metadata dictionaries.

        Args:
            params (str): Additional URL parameters for the request.
            ctx (Context): The context object with request-specific information.

        Returns:
            McpResourceResponse: A dictionary containing the status
            of the operation, the retrieved metadata list, error information
            (if any), and context metadata.

        Example:
            result = await get_all_metadata_dictionaries("limit=10", ctx)
            print(result)
        """
        await ctx.report_progress(1, 3)
        url_path = check_and_make_url_params("dictionaries/metadata", params)
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        response = await run_resource_aiohttp_session(url_path)
        await ctx.report_progress(2, 3)
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        if response.status != 200:
            await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
            return {
                "status": "ERROR",
                "data": None,
                "error_code": response.status,
                "error_message": response.reason,
            }
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        await ctx.report_progress(3, 3)
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        return {"status": "OK", "data": json_response.get("metadata", [])}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://dictionaries/statistics",
        tags=["dictionary-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
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
        await ctx.report_progress(1, 3)
        url_path = "dictionaries/metadata"
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        response = await run_resource_aiohttp_session(url_path)
        await ctx.report_progress(2, 3)
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        if response.status != 200:
            await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
            return {
                "status": "ERROR",
                "data": None,
                "error_code": response.status,
                "error_message": response.reason,
            }
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        await ctx.report_progress(3, 3)
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        results = []
        for metadata in json_response.get("metadata", []):
            stats = {}
            stats["dictionary_id"] = metadata.get("id_dico")
            stats["short_name"] = metadata.get("short_name")
            stats["statistics"] = metadata.get("statistics")
            results.append(stats)
        return {"status": "OK", "data": results}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://dictionaries/statistics/{dictionary_id}",
        tags=["dictionary-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_statistics_metadata_dictionary_by_id(
        dictionary_id: str, ctx: Context
    ) -> McpResourceResponse:
        """
        Fetches the statistics metadata for a dictionary by its ID.

        This asynchronous function retrieves metadata statistics for a specific dictionary
        using its unique identifier. It reports progress at various stages, logs information
        about the request and response, and handles errors appropriately.

        Args:
            dictionary_id (str): The unique identifier of the dictionary.
            ctx (Context): The context object containing request and logging utilities.

        Returns:
            McpResourceResponse: A dictionary containing the status of the operation,
            the retrieved data (if successful), or error details in case of failure.
        """
        await ctx.report_progress(1, 3)
        url_path = f"dictionaries/metadata/{dictionary_id}"
        url_path = check_and_make_url_params(url_path, "none")
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        response = await run_resource_aiohttp_session(url_path)
        await ctx.report_progress(2, 3)
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        if response.status != 200:
            await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
            return {
                "status": "ERROR",
                "data": None,
                "error_code": response.status,
                "error_message": response.reason,
            }
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        json_response = await response.json()
        await ctx.report_progress(3, 3)
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        return {"status": "OK", "data": json_response.get("metadata").get("statistics")}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://dictionaries/search?q={search_term}&{params}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def search_metadata_in_all_dictionaries(
        search_term: str, params: str, ctx: Context
    ) -> McpResourceResponse:
        """
        Find metadata for a dictionary by its content.

        Args:
            search_term (str): The search term to find articles.
            params (str, optional): Additional URL parameters for the request.
            ctx (Context): The context object with request-specific information.

        Returns:
            McpResourceResponse: A dictionary containing the status
            of the operation,the retrieved metadata, error information
            (if any), and context metadata.

        Example:
            result = await search_in_all_dictionaries(word_key, params, ctx)
            print(result)
        """
        await ctx.report_progress(1, 3)
        url_path = f"dictionaries/metadata?search={search_term}"
        url_path = check_and_make_url_params(url_path, params)
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        response = await run_resource_aiohttp_session(url_path)
        await ctx.report_progress(2, 3)
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        if response.status != 200:
            await ctx.error(f"[{ctx.request_id}] Error: {response.status}")
            return {
                "status": "ERROR",
                "data": None,
                "error_code": response.status,
                "error_message": response.reason,
            }
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        await ctx.report_progress(3, 3)
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        return {"status": "OK", "data": json_response.get("metadata", [])}
