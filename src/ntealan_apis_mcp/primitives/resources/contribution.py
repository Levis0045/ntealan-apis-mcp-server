from uuid import UUID

from fastmcp import Context

from ntealan_apis_mcp.common.http_session import run_resource_aiohttp_session
from ntealan_apis_mcp.common.utils import check_and_make_url_params
from ntealan_apis_mcp.models.common import McpResourceResponse


def add_contribution_resources_to_server(ntl_mcp_server):
    """
    Add dynamic contribution resources to the NTeALan MCP server.

    Args:
        ntl_mcp_server: The NTeALan MCP server instance.

    Returns:
        None
    """

    @ntl_mcp_server.resource(
        uri="ntealan-apis://contributions/{dictionary_id}/{contribution_id}",
        tags=["contribution-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_contribution_by_dictionary_id(
        dictionary_id: str, contribution_id: UUID, ctx: Context
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
        await ctx.report_progress(1, 3)
        url_path = f"dictionaries/articles/{dictionary_id}/contributions/{contribution_id}"
        await ctx.info(f"[{ctx.request_id}] Execute GET request: {url_path}...")
        url_path = check_and_make_url_params(url_path, "none")
        response = await run_resource_aiohttp_session(url_path)
        await ctx.report_progress(2, 3)
        await ctx.info(f"[{ctx.request_id}] Checking system status: {response}...")
        if response.status not in [200, 206]:
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
        return {"status": "OK", "data": json_response}

    @ntl_mcp_server.resource(
        uri="ntealan-apis://contributions/{article_id}",
        tags=["contribution-endpoint", "mcp-resource"],
        mime_type="application/json",
    )
    async def get_contribution_by_id(article_id: UUID, ctx: Context) -> McpResourceResponse:
        """
        Retrieve a contribution by its unique identifier.

        Args:
            article_id (UUID): The unique identifier of the article.
            ctx (Context): The context object containing request-specific information.

        Returns:
            McpResourceResponse: A placeholder response.
        """
        # Placeholder logic
        return {"status": "OK", "data": f"Hello, {article_id}!"}
