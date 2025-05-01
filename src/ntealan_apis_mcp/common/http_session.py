from asyncio import get_event_loop

from aiohttp import (
    AsyncResolver,
    ClientResponse,
    ClientSession,
    ClientTimeout,
    TCPConnector,
    TraceConfig,
)
from dotenv import load_dotenv

from ntealan_apis_mcp.models.common import (
    ConfigModel,
    HttpResourceAllowMedodsEnum,
    HttpToolAllowMedodsEnum,
)

from .cache import lru_acache

load_dotenv()

CONFIG = ConfigModel()


async def on_request_start(session, trace_config_ctx, params):
    trace_config_ctx.start = get_event_loop().time()
    print("Starting request")


async def on_request_end(session, trace_config_ctx, params):
    elapsed = get_event_loop().time() - trace_config_ctx.start
    print("Request took {}".format(elapsed))
    print("Ending request")


trace_config = TraceConfig()
trace_config.on_request_start.append(on_request_start)
trace_config.on_request_end.append(on_request_end)


@lru_acache()
async def create_aiohttp_session() -> ClientSession:
    """
    Create an AIOHTTP session for NTeALan dictionary APIs.

    Object is cached for performance.

    Returns a `ClientSession` instance.
    """
    return ClientSession(
        # Base URL for the API
        base_url=CONFIG.base_api_url,
        # Same config as default in the SDK
        auto_decompress=False,
        trust_env=True,
        # Debug
        trace_configs=[trace_config],
        # Performance
        connector=TCPConnector(
            resolver=AsyncResolver(), limit_per_host=CONFIG.api_aiohttp_connect_perhost
        ),
        # Reliability
        timeout=ClientTimeout(
            connect=CONFIG.api_aiohttp_connect_timeout, total=CONFIG.api_aiohttp_connect_total
        ),
    )


async def run_resource_aiohttp_session(
    url: str,
    method: HttpResourceAllowMedodsEnum = HttpResourceAllowMedodsEnum.GET,
    extra_config: dict = {},
) -> ClientResponse:
    """
    Run the AIOHTTP session for resource.

    This function is used to run the AIOHTTP session in a synchronous context.
    It is typically used for testing or debugging purposes.
    """
    client = await create_aiohttp_session()
    response = await client.request(method=method, url=url, **extra_config)
    # print(f"Response content: {await response.json()}\n URL: {url}")
    return response


async def run_tool_aiohttp_session(
    url: str,
    method: HttpToolAllowMedodsEnum = HttpToolAllowMedodsEnum.POST,
    extra_config: dict = {},
) -> ClientResponse:
    """
    Run the AIOHTTP session for tool.

    This function is used to run the AIOHTTP session in a synchronous context.
    It is typically used for testing or debugging purposes.
    """
    session = await create_aiohttp_session()
    response = await session.request(method=method, url=url, **extra_config)
    session.close()
    return response
