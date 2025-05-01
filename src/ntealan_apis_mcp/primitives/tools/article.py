from uuid import UUID

from ntealan_apis_mcp.models.article import Article

# NOT COMPLETED


def add_article_tools_to_server(ntl_mcp_server):
    """
    Add article tools to the NTL MCP server.

    Args:
        ntl_mcp_server: The NTL MCP server instance.
    """

    @ntl_mcp_server.tool(tags=["article-endpoint", "mcp-tool"])
    def create_article(dictionary_id: str, data: Article) -> str:
        """
        Create a new article in a dictionary.

        Args:
            dictionary_id (str): The ID of the dictionary.
            data (Article): The article data to create.

        Returns:
            str: The API response as a string.
        """
        return "a + b"

    @ntl_mcp_server.tool(tags=["article-endpoint", "mcp-tool"])
    def update_article(dictionary_id: str, article_id: UUID, data: Article) -> str:
        """
        Update an existing article in a dictionary.

        Args:
            dictionary_id (str): The ID of the dictionary.
            article_id (UUID): The ID of the article.
            data (Article): The updated article data.

        Returns:
            str: The API response as a string.
        """
        return "a + b"

    @ntl_mcp_server.tool(tags=["article-endpoint", "mcp-tool"])
    def delete_article(article_id: UUID, data: Article) -> str:
        """
        Delete an article from a dictionary.

        Args:
            dictionary_id (str): The ID of the dictionary.
            article_id (UUID): The ID of the article.

        Returns:
            str: The API response as a string.
        """
        return "a + b"
