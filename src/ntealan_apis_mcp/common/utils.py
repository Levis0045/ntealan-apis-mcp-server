from re import compile as re_compile

valid_path = re_compile(r"^dictionaries/[articles|core|metadata][a-z?/=&]*")


def check_and_make_url_params(url: str, params: str) -> str:
    """
    Check and make params for the request.
    """
    # Check if params is None or empty
    if not params and params == "none":
        return url

    # Check if params is a string
    if not isinstance(params, str) and not valid_path.match(url):
        raise ValueError("Params must be a string and must follow valid NTeALan pattern.")

    # Check if params is a valid query string
    url_path = url
    # url_path = quote(url.strip(), safe="/:?&")
    if params != "none":
        if "?" in url_path:
            url_path = f"{url_path}&{params.strip()}"
        else:
            url_path = f"{url_path}?{params.strip()}"

    # print(f"URL Path: {url_path}")

    # Return the params
    return url_path
