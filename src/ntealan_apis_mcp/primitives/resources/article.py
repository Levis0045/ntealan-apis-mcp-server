from uuid import UUID

from fastmcp import Context

from ntealan_apis_mcp.common.http_session import run_resource_aiohttp_session
from ntealan_apis_mcp.common.utils import check_and_make_url_params
from ntealan_apis_mcp.models.common import McpResourceResponse


# Add article resources to the NTeALan MCP server
# This function is called to add article resources to the server
# It defines various endpoints for retrieving articles, statistics,
# and searching articles in dictionaries
# Each endpoint is associated with a specific function that handles
# the request and returns the appropriate response
# The endpoints are defined using the add_resource_fn method of the
# NTeALan MCP server instance
# Each endpoint has a unique URI, name, tags, MIME type, and description
# The functions defined here are used to handle the requests
def add_article_resources_to_server(ntl_mcp_server):
    """
    Add article resources to the NTeALan MCP server.

    Args:
        ntl_mcp_server (NTeALanMCPServer): The NTeALan MCP server instance.

    Returns:
        None
    """

    # Add article resources to the server
    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles?{params}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_all_articles(ctx: Context, params: str = "none") -> McpResourceResponse:
        """
        Retrieve all articles.

        Args:
            params (str, optional): Additional URL parameters for the request.
            ctx (Context, optional): The context object containing
            client and request information.

        Returns:
            McpResourceResponse: A dictionary containing the status,
            articles data, error information (if any), and context
            metadata.
        """
        # Report initial progress
        await ctx.report_progress(1, 3)
        # Build the URL path for the articles request
        url_path = check_and_make_url_params("dictionaries/articles", params)
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
                "error_message": response.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the articles data in a standardized response format
        return {"status": "OK", "data": json_response.get("articles")}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles/metadata/{dictionary_id}/{article_id}?{params}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_article_by_id(
        dictionary_id: str, article_id: UUID, ctx: Context, params: str = "none"
    ) -> McpResourceResponse:
        """
        Retrieve an article by its unique identifier.

        Args:
            dictionary_id (str): The unique identifier of the dictionary containing the article.
            article_id (UUID): The unique identifier of the article to retrieve.
            params (str, optional): Additional URL parameters for the request.
            ctx (Context, optional): The context object containing request-specific information.

        Returns:
            McpResourceResponse: A dictionary containing the status of
            the operation, the article data, error information (if any)
            , and context metadata.

        Example:
            result = await get_article_by_id("12345", some_article_uuid, ctx=ctx)
            print(result)
        """
        # Report initial progress
        await ctx.report_progress(1, 3)
        # Build the URL path for the article request
        url_path = check_and_make_url_params(
            f"dictionaries/articles/{dictionary_id}/{article_id}", params
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
                "error_message": response.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the article data in a standardized response format
        return {"status": "OK", "data": json_response.get("article")}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles/metadata/{dictionary_id}?{params}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_all_articles_with_dictionary_id(
        dictionary_id: str, params: str = "none", ctx: Context = None
    ) -> McpResourceResponse:
        """
        Retrieve all articles associated with a specific dictionary ID.

        Args:
            dictionary_id (str): The unique identifier of the dictionary.
            params (str, optional): Additional URL parameters for the request.
            ctx (Context, optional): The context object containing request metadata .

        Returns:
            McpResourceResponse: A dictionary containing the status of the operation,
            the retrieved articles, error information (if any), and context metadata.
        """
        # Report initial progress
        await ctx.report_progress(1, 3)
        # Build the URL path for the articles request
        url_path = check_and_make_url_params(f"dictionaries/articles/{dictionary_id}", params)
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
                "error_message": response.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the articles data in a standardized response format
        return {"status": "OK", "data": json_response.get("articles")}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles/statistics/{dictionary_id}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_statistics_for_articles_by_dictionary(
        dictionary_id: str, ctx: Context
    ) -> McpResourceResponse:
        """
        Retrieve statistics for articles associated with a specific dictionary by its ID.

        Args:
            dictionary_id (str): The unique identifier of the dictionary.
            ctx (Context, optional): The context object containing client and request metadata.

        Returns:
            McpResourceResponse: A response object containing the status,
            statistics data, error details (if any), and metadata such
            as client_id and request_id.
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
                "error_message": response.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the statistics data in a standardized response format
        return {"status": "OK", "data": json_response.get("metadata", {}).get("statistics")}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles/statistics",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_statistics_for_articles(ctx: Context) -> McpResourceResponse:
        """
        Retrieve statistics for all articles.

        Args:
            ctx (Context, optional): The context object
            containing client and request information.

        Returns:
            McpResourceResponse: A dictionary containing the status,
            statistics data, error details, client ID, and request ID.
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
                "error_message": response.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the statistics data in a standardized response format
        return {"status": "OK", "data": json_response}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles/dictionaries/search/{dictionary_id}?q={search_term}&{params}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def search_articles_in_dictionary(
        dictionary_id: str, search_term: str, params: str = "none", ctx: Context = None
    ) -> McpResourceResponse:
        """
        Find articles in all existing dictionaries.

        Args:
            dictionary_id (str): The unique identifier of the dictionary.
            search_term (str): The search term to find articles.
            params (str, optional): Additional URL parameters for the request.
            ctx (Context, optional): The context object containing
            client and request information.

        Returns:
            McpResourceResponse: A dictionary containing the status,
            articles data, error information (if any), and context
            metadata.
        """
        # Report initial progress
        await ctx.report_progress(1, 3)
        # Build the URL path for the articles request
        url = f"dictionaries/articles/{dictionary_id}?search={search_term}"
        url_path = check_and_make_url_params(url, params)
        # Log the request execution
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        # Perform the HTTP GET request
        response_search = await run_resource_aiohttp_session(url_path)
        # Report progress after request
        await ctx.report_progress(2, 3)
        # Handle non-200 responses as errors
        if response_search.status not in [200, 206]:
            await ctx.error(f"Error: {response_search.status}")
            return {
                "status": "ERROR",
                "data": None,
                "error_code": response_search.status,
                "error_message": response_search.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response_search.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the articles data in a standardized response format
        return {"status": "OK", "data": json_response.get("search", [])}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://articles/search?q={search_term}&{params}",
        tags=["article-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def search_articles_in_all_dictionaries(
        search_term: str, params: str = "none", ctx: Context = None
    ) -> McpResourceResponse:
        """
        Find articles in all dictionaries.

        Args:
            search_term (str): The search term to find articles.
            params (str, optional): Additional URL parameters for the request.
            ctx (Context, optional): The context object containing
            client and request information.

        Returns:
            McpResourceResponse: A dictionary containing the status,
            articles data, error information (if any), and context
            metadata.
        """
        # Report initial progress
        await ctx.report_progress(1, 3)
        # Build the URL path for the articles request
        url = f"dictionaries/articles?search={search_term}"
        url_path = check_and_make_url_params(url, params)
        # Log the request execution
        await ctx.info(f"[{ctx.request_id}] Execute get request: {url_path}...")
        # Perform the HTTP GET request
        response = await run_resource_aiohttp_session(url_path)
        # Report progress after request
        await ctx.report_progress(2, 3)
        # Log the response status
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        # Handle non-200 responses as errors
        if response.status not in [200, 206]:
            await ctx.error(f"Error: {response.status}")
            return {
                "status": "ERROR DATA",
                "data": None,
                "error_code": response.status,
                "error_message": response.reason,
            }
        # Log successful status
        await ctx.info(f"[{ctx.request_id}] System status is OK.")
        # Final progress report
        await ctx.report_progress(3, 3)
        # Parse the JSON response
        json_response = await response.json()
        await ctx.info(f"[{ctx.request_id}] System response: {json_response}")
        # Return the articles data in a standardized response format
        return {"status": "OK", "data": json_response.get("search", [])}
