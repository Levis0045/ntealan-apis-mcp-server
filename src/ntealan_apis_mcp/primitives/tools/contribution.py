from uuid import UUID

from ntealan_apis_mcp.models.contribution import Contribution

# NOT COMPLETED


def add_contribution_tools_to_server(ntl_mcp_server):
    """
    Add contribution tools to the NTL MCP server.

    Args:
        ntl_mcp_server: The NTL MCP server instance.
    """

    @ntl_mcp_server.tool(
        tags=["contribution-endpoint", "mcp-tool"],
    )
    def create_contribution(contribution_id: UUID, data: Contribution) -> str:
        """
        Create a new contribution for an article in a dictionary.

        Args:
            dictionary_id (str): The ID of the dictionary.
            article_id (UUID): The ID of the article.
            data (Contribution): The contribution data to create.

        Returns:
            str: The API response as a string.
        """
        return "a + b"

    @ntl_mcp_server.tool(
        tags=["contribution-endpoint", "mcp-tool"],
    )
    def update_contribution(contribution_id: UUID, data: Contribution) -> str:
        """
        Update an existing contribution for an article in a dictionary.

        Args:
            dictionary_id (str): The ID of the dictionary.
            article_id (UUID): The ID of the article.
            contribution_id (UUID): The ID of the contribution.
            data (Contribution): The updated contribution data.

        Returns:
            str: The API response as a string.
        """
        return "a + b"

    @ntl_mcp_server.tool(
        tags=["contribution-endpoint", "mcp-tool"],
    )
    def delete_contribution(contribution_id: UUID) -> str:
        """
        Delete a contribution from an article in a dictionary.

        Args:
            dictionary_id (str): The ID of the dictionary.
            article_id (UUID): The ID of the article.
            contribution_id (UUID): The ID of the contribution.

        Returns:
            str: The API response as a string.
        """
        return "a + b"
