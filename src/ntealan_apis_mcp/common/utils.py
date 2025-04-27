
def check_and_make_url_params(url: str, params: str) -> str:
    """
    Check and make params for the request.
    """
    # Check if params is None or empty
    if not params:
        return url

    # Check if params is a string
    if not isinstance(params, str):
        raise ValueError("Params must be a string.")

    # Check if params is a valid query string
    url_path = url.strip()
    if params != "none":
        url_path = f"{url_path}?{params.strip()}"

    # Return the params
    return url_path
