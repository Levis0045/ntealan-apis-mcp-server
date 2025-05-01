from ntealan_apis_mcp.models.dictionary import Dictionary

# NOT COMPLETED


def add_dictionary_tools_to_server(ntl_mcp_server):
    """
    Add dictionary tools to the NTL MCP server.

    Args:
        ntl_mcp_server: The NTL MCP server instance.
    """

    @ntl_mcp_server.tool(tags=["dictionary-endpoint", "mcp-tool"])
    def create_dictionary(dictionary_id: str, data: Dictionary) -> str:
        """
        Create a new dictionary in the NTeALan API.

        Args:
            dictionary_id (str): The unique identifier for the dictionary.
            data (Dictionary): The dictionary data to create.

        Returns:
            str: The API response as a string.
        """
        return "a + b"

    @ntl_mcp_server.tool(tags=["dictionary-endpoint", "mcp-tool"])
    def update_dictionary(dictionary_id: str, data: Dictionary) -> str:
        """
        Update an existing dictionary in the NTeALan API.

        Args:
            dictionary_id (str): The unique identifier for the dictionary.
            data (Dictionary): The updated dictionary data.

        Returns:
            str: The API response as a string.
        """
        return "a + b"

    @ntl_mcp_server.tool(tags=["dictionary-endpoint", "mcp-tool"])
    def delete_dictionary(dictionary_id: str) -> str:
        """
        Delete a dictionary from the NTeALan API.

        Args:
            dictionary_id (str): The unique identifier for the dictionary.

        Returns:
            str: The API response as a string.
        """
        return "a + b"
