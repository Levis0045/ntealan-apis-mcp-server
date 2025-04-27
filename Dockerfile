FROM python:3.13-slim

LABEL maintainer="NTEALAN <Elvis Mboning>"
LABEL description="A Dockerfile for the NTEALAN APIS MCP Server"
LABEL version="1.0"
LABEL repository="https://github.com/Levis0045/ntealan-apis-mcp-server"

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends git curl ca-certificates

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
ENV UV_LINK_MODE=copy

# Copy the project into the image
RUN git clone --depth 1 https://github.com/Levis0045/ntealan-apis-mcp-server.git /app

# Defined env for the fastmcp server
ENV FASTMCP_SERVER_SSE_PATH=/sse
ENV FASTMCP_SERVER_MESSAGE_PATH=/messages/
ENV FASTMCP_SERVER_HOST=0.0.0.0
ENV FASTMCP_SERVER_PORT=8000
ENV NTEALAN_BASE_API_URL="https://apis.ntealan.net/ntealan/"
ENV NTEALAN_API_VERSION=v1
ENV NTEALAN_API_AIOHTTP_TIMEOUT=30
ENV NTEALAN_API_AIOHTTP_RETRIES=3
ENV NTEALAN_API_AIOHTTP_RETRY_DELAY=5

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked --no-cache-dir 
# RUN uv sync --locked --no-cache-dir  --compile-bytecode

ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000

CMD ["uv", "run", "ntealanmcp", "-t", "stdio"]