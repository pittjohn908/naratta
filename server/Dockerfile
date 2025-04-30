FROM library/ubuntu:24.10 AS builder

COPY --from=ghcr.io/astral-sh/uv:0.6.0 /uv /uvx /bin/

RUN apt-get update && apt-get install -y ca-certificates git libgomp1 && rm -rf /var/lib/apt/lists/*

WORKDIR /server

RUN uv venv /server/.venv
ENV VIRTUAL_ENV=/server/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# COPY .python-version pyproject.toml uv.lock .env /server/
COPY .python-version pyproject.toml uv.lock /server/
COPY app /server/app

RUN uv sync --frozen

EXPOSE 8000

CMD [".venv/bin/fastapi", "run", "app/server.py", "--port", "8000", "--host", "0.0.0.0"]

