<div align="center">

<span style="font-size: 28px;font-weight: bold">🦜 NTeALan REST APIs MCP Server</span>

A modular, extensible <a href="https://modelcontextprotocol.io/"> Model Context Protocol (MCP) </a> server for [NTeALan REST APIs dictionaries](https://apis.ntealan.net/ntealan) and contributions. This project provides a unified interface for managing dictionary data, articles, and user contributions, and is designed for easy integration and extension.

The project is deployed at [https://apis.ntealan.net/ntealan/mcpserver](https://apis.ntealan.net/ntealan/mcpserver). Only resource actions is available now (this dev endpoint could be unavailable sometimes).

[![smithery badge](https://smithery.ai/badge/@Levis0045/ntealan-apis-mcp-server)](https://smithery.ai/server/@Levis0045/ntealan-apis-mcp-server)

[![PyPI][pypi-badge]][pypi-url]
[![MIT licensed][mit-badge]][mit-url]
[![Documentation][docs-badge]][docs-url]

</div>

---

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Server](#running-the-server)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Resources](#resources)
  - [Tools](#tools)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Dictionary Management**: Create, update, delete, and retrieve dictionaries and their metadata.
- **Article Management**: Manage articles within dictionaries, including statistics and filtering.
- **Contribution Management**: Track and manage user contributions to articles and dictionaries.
- **Extensible MCP Server**: Easily add new resources and tools.
- **Async Support**: Built on top of `fastmcp` and `aiohttp` for high performance.
- **OpenAPI-like Resource Registration**: Register resources and tools with URIs and tags.

---

## Getting Started

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)
- [aiohttp](https://docs.aiohttp.org/)
- [pydantic](https://docs.pydantic.dev/)
- [fastmcp](https://gofastmcp.com/getting-started/welcome) (or your fork)
- [aiodns](https://github.com/saghul/aiodns)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

### Installation


#### Installing via pip

Clone the repository and install dependencies:

```bash
git clone https://github.com/Levis0045/ntealan-apis-mcp-server.git
cd ntealan-apis-mcp-server
pip install .
```

#### (Optional) Install and use [uv](https://github.com/astral-sh/uv) for faster dependency management

If you want faster installs and modern Python packaging, you can use [uv](https://github.com/astral-sh/uv) in the `ntealan-apis-mcp-server` directory:

```bash
uv sync
```

### Running the Server

To start the MCP server:

```bash
python -m ntealanmcp -t stdio
```

Or, if you have [uv](https://github.com/astral-sh/uv) installed, you can run server command:

```bash
ntealanmcp -t stdio
```

The server will run using the `Server-Sent Events (sse)` transport by default at this endpoint `http://127.0.0.1:8000/sse`. You can modify the transport in `main.py` if needed.

---

## Project Structure

```
ntealan-api/
├── src/
│   └── ntealan_apis_mcp/
│       ├── main.py
│       ├── models/
│       │   ├── article.py
│       │   ├── contribution.py
│       │   ├── dictionary.py
│       │   └── common.py
│       ├── primitives/
│       |    ├── resources/
│       │    │   ├── article.py
│       │    │   ├── contribution.py
│       │    │   └── dictionary.py
│       |    └── tools/
│       |        ├── article.py
│       |        ├── contribution.py
│       |        └── dictionary.py
│       └── common/
│           ├── utils.py
│           ├── cache.py
│           └── http_session.py
├── examples/
├── tests/
├── pyproject.toml
└── requirements.txt
```

---

## Usage

### Primitive resources

Resources are asynchronous functions that expose public Data from NTeALan API endpoints for  dictionaries, articles, and contributions. They are registered with the MCP server and can be called via their custom URIs.

Example resource registration (see `src/ntealan_apis_mcp/main.py`):

```python
ntl_mcp_server.add_resource_fn(
    lambda dictionary_id, article_id, params: get_article_by_id(
        dictionary_id, article_id, params, ntl_mcp_server.get_context()
    ),
    name="get_article_by_id",
    uri="ntealan-apis://articles/{dictionary_id}/{article_id}?{params}",
    tags=["article-endpoint", "mcp-resource"],
    mime_type="application/json",
    description="Get an article by ID"
)
```

List of existings resources and status:

| Name / URI Pattern                                               | Description                                      | Parameters                                      | Development Status   |
|------------------------------------------------------------------|--------------------------------------------------|-------------------------------------------------|---------------------|
| `ntealan-apis://dictionaries/{dictionary_id}`                    | Get dictionary metadata by ID                     | `dictionary_id`                                 | Stable              |
| `ntealan-apis://dictionaries?{params}`                           | Get all dictionaries metadata                     | `params` (e.g., `limit=10`)                     | Stable              |
| `ntealan-apis://dictionaries/statistics/{dictionary_id}`         | Get statistics for a specific dictionary          | `dictionary_id`                                 | Stable              |
| `ntealan-apis://dictionaries/statistics`                         | Get statistics for all dictionaries               | None                                            | Stable              |
| `ntealan-apis://articles/{dictionary_id}/{article_id}?{params}`  | Get article by ID                                 | `dictionary_id`, `article_id`, `params`         | Stable              |
| `ntealan-apis://articles?{params}`                               | Get all articles                                  | `params` (e.g., `limit=10`)                     | Stable              |
| `ntealan-apis://articles/{dictionary_id}?{params}`               | Get all articles for a dictionary                 | `dictionary_id`, `params`                       | Stable              |
| `ntealan-apis://articles/statistics/{dictionary_id}`             | Get article statistics for a dictionary           | `dictionary_id`                                 | Stable              |
| `ntealan-apis://articles/statistics`                             | Get statistics for all articles                   | None                                            | Not stable              |
| `ntealan-apis://contributions/{dictionary_id}/{contribution_id}` | Get contribution by ID                            | `dictionary_id`, `contribution_id`              | Stable              |


### Primitive tools

Tools are utility functions for creating, updating, and deleting dictionaries, articles, and contributions.

Example tool registration:

```python
ntl_mcp_server.add_tool(
    create_dictionary,
    description="Create a new dictionary",
    tags=["mcp-tool", "dictionary-endpoint"]
)
```

List of existings tools and status (NOT YET IMPLEMENTED):


| Tool Name              | Description                        | Required Payload Fields                                      | Development Status   |
|------------------------|------------------------------------|-------------------------------------------------------------|---------------------|
| `create_dictionary`    | Create a new dictionary            | `data` (dictionary fields)                                  | Not started              |
| `update_dictionary`    | Update an existing dictionary      | `dictionary_id`, `data` (fields to update)                  | Not started              |
| `delete_dictionary`    | Delete a dictionary                | `dictionary_id`                                             | Not started              |
| `create_article`       | Create a new article               | `dictionary_id`, `data` (article fields)                    | Not started              |
| `update_article`       | Update an article                  | `dictionary_id`, `article_id`, `data` (fields to update)    | Not started              |
| `delete_article`       | Delete an article                  | `dictionary_id`, `article_id`                               | Not started              |
| `create_contribution`  | Create a new contribution          | `dictionary_id`, `article_id`, `data` (contribution fields) | Not started              |
| `update_contribution`  | Update a contribution              | `dictionary_id`, `article_id`, `contribution_id`, `data`    | Not started              |
| `delete_contribution`  | Delete a contribution              | `dictionary_id`, `article_id`, `contribution_id`            | Not started              |


### Run examples

Check `examples/` folder to run and test some samples.

```bash
# for all resources
uv run examples/run_client_resources.py
# for all tools
uv run examples/run_client_tools.py
```

### Deploying with Docker

You can deploy the MCP server using Docker and serve it behind an Nginx reverse proxy for production environments.

#### 1. Build the Docker image

Build the Docker image manually:

```bash
docker build -t ntealan-mcp-server .
```

#### 2. Or automatically build and start the service

- Get and check the latest version of compose and Docker. You will get in response `Docker Compose version v2.35.1`.

```bash
docker compose version
```
- Build and start the service

```bash
docker compose up --build -d
```

- Your MCP server will now be accessible at this address `http://0.0.0.0:8000` or your configured domain.

- Connect with MCP Client at `http://127.0.0.1:8000/sse` or your configured domain.


### Connect with Smithery

- Install mcp cli 

```bash
uv add "mcp[cli]"
```

- Connect with MCP client 

```python
import mcp
from mcp.client.websocket import websocket_client
import json
import base64

smithery_api_key = "your-api-key"
url = f"wss://server.smithery.ai/@Levis0045/ntealan-apis-mcp-server/ws?api_key={smithery_api_key}"

async def main():
    # Connect to the server using websocket client
    async with websocket_client(url) as streams:
        async with mcp.ClientSession(*streams) as session:
            # Initialize the connection
            await session.initialize()
            # List available tools
            tools_result = await session.list_tools()
            print(f"Available tools: {', '.join([t.name for t in tools_result.tools])}")

            # Example of calling a tool:
            # result = await session.call_tool("tool-name", arguments={"arg1": "value"})

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

---

## Contributing

Get more informations in this file: [CONTRIBUTION.md](CONTRIBUTION.md)


## Contact

- **Project Lead**: Elvis Mboning@[NTeALan](https://ntealan.org/)
- **NTeALan APIs documentation**: [https://apis.ntealan.net/ntealan](https://apis.ntealan.net/ntealan)
- **GitHub Issues**: [https://github.com/Levis0045/ntealan-apis-mcp-server/issues](https://github.com/Levis0045/ntealan-apis-mcp-server/issues)
- **Email**: contact@ntealan.org


[pypi-badge]: https://img.shields.io/pypi/v/mcp.svg
[pypi-url]: https://pypi.org/project/ntealan_apis_mcp/
[mit-badge]: https://img.shields.io/pypi/l/mcp.svg
[mit-url]: https://github.com/Levis0045/ntealan-apis-mcp-server/blob/v1/LICENSE
[docs-badge]: https://img.shields.io/badge/docs-modelcontextprotocol.io-blue.svg
[docs-url]: https://raw.githubusercontent.com/Levis0045/ntealan-apis-mcp-server/refs/heads/v1/README.md
[spec-url]: https://github.com/Levis0045/ntealan-apis-mcp-server/blob/v1/README.md
[python-url]: https://www.python.org/downloads/
