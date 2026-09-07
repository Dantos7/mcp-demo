# mcp-demo

<p>
    <a href="https://www.repostatus.org/#wip"><img src="https://www.repostatus.org/badges/latest/wip.svg" alt="Project Status: WIP – Initial development is in progress."/></a>
    <a href="https://github.com/Dantos7/mcp-demo"><img alt="Version" src="https://img.shields.io/github/v/release/Dantos7/mcp-demo"></a>
</p>

A demo project to test out MCP.

## 🚀 Getting started

Requires Python 3.14 and [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uv sync
uv run prek install
```

Common tasks:

```bash
uv run poe test        # run the test suite
uv run poe format      # format the code
uv run poe lint        # lint and autofix
uv run poe typecheck   # type-check the code
uv run poe check       # all of the above
```

## 📁 Layout

```text
src/mcp_demo/server_stdio.py   # FastMCP server over stdio (for local MCP clients)
src/mcp_demo/server_http.py    # FastMCP server over HTTP, self-tunnelled with ngrok
src/mcp_demo/client.py         # OpenAI-SDK client pointed at Groq, calling the HTTP server as a remote MCP tool
.env.example                   # template for the required environment variables
tests/unit/                    # unit tests
tests/integration/             # integration tests
```

Both servers expose the same two demo tools:

| Tool    | Signature                  | Returns             |
| ------- | -------------------------- | ------------------- |
| `add`   | `add(a: int, b: int)`      | `a + b`             |
| `greet` | `greet(name: str)`         | `"Hello, {name}!"`  |

## ⚙️ Configuration

Copy [.env.example](.env.example) to `.env` and fill in the three values — both `client.py` and
`server_http.py` load it automatically via `python-dotenv`:

```bash
cp .env.example .env
```

| Variable          | Used by             | Where to get it                                             |
| ----------------- | ------------------- | ----------------------------------------------------------- |
| `GROQ_API_KEY`    | `client.py`         | <https://console.groq.com/keys>                              |
| `NGROK_AUTHTOKEN` | `server_http.py`    | <https://dashboard.ngrok.com>                                |
| `NGROK_DOMAIN`    | both                | a reserved domain on your ngrok account, e.g. `your-domain.ngrok-free.dev` (no scheme) |

`NGROK_DOMAIN` is the piece that ties the two together: the server tunnels itself to that domain,
and the client builds its `server_url` as `https://$NGROK_DOMAIN/mcp` — so they always agree.

All three values are only needed for Usage A below. `server_http.py` opens the tunnel only when
`NGROK_DOMAIN` is set, so the local-only path in Usage B runs fine with no `.env` at all.

## ▶️ Usage A — Groq calling the server as a remote MCP tool

This is the main demo: Groq's hosted models call your local MCP server over the internet.

### 1. Start the server (and its tunnel)

```bash
uv run python -m mcp_demo.server_http
```

This serves MCP at `http://127.0.0.1:8000/mcp` and prints the public URL it's reachable at.

Why the tunnel: `client.py` registers the server with Groq's `responses` API as a **remote** tool
(`type: "mcp"`), and Groq's servers fetch the tool list by calling `server_url` themselves — so
`localhost` is not reachable from their side and gets rejected. `connect_ngrok()` in
[server_http.py](src/mcp_demo/server_http.py) solves this using the
[`ngrok`](https://pypi.org/project/ngrok/) Python SDK, installed as a project dependency by
`uv sync`. **No ngrok CLI or system install is needed** — just `NGROK_AUTHTOKEN`.

> The tunnel uses the reserved domain from `NGROK_DOMAIN`, which must exist on your ngrok
> account. While the tunnel is up, anyone with the URL can reach your local server, so only run
> it while testing.

### 2. Run the client

```bash
uv run python -m mcp_demo.client
```

It sends a prompt ("Greet Veit, Alejandro and Lukasz") to `openai/gpt-oss-120b` on Groq, which
calls back into your tunnelled server at `https://{$NGROK_DOMAIN}/mcp`, invokes `greet` once per
name, and prints the final text. A full example response object is saved in
[output/response.txt](output/response.txt).

## ▶️ Usage B — connecting a local MCP client

To use the tools from a local MCP client such as Claude Code instead, register either server in
your client config:

```jsonc
{
  "mcpServers": {
    // stdio: the client spawns the server itself — nothing to start manually
    "mcp-demo-server-stdio": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "/absolute/path/to/mcp-demo/src/mcp_demo/server_stdio.py"]
    },
    // http: requires `uv run python -m mcp_demo.server_http` to be running
    "mcp-demo-server-http": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

Neither ngrok nor a Groq key is needed for this path — the client talks to the server directly.

## 🏷️ Versioning

The package version is derived from git tags by
[uv-dynamic-versioning](https://github.com/ninoseki/uv-dynamic-versioning). Tag a release to
publish a new version:

```bash
git tag 0.1.0
```

---

Generated from the [python-project-template](https://github.com/Dantos7/python-project-template) Copier template.
Run `uvx copier update` to pull in later template changes.
