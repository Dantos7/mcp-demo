# 🕰️ Changelog

All notable changes to this project are documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/).


## [0.2.0] - 2026-09-07

### ✨ Features

- MCP demo server exposing `add` and `greet` tools, over stdio (`server_stdio.py`) and over HTTP (`server_http.py`)
- `server_http.py` self-tunnels with the `ngrok` Python SDK when `NGROK_DOMAIN` is set, so hosted models can reach it
- Demo client (`client.py`) that registers the tunnelled server with Groq's `responses` API as a remote MCP tool
- `.env.example` template for `GROQ_API_KEY`, `NGROK_AUTHTOKEN` and `NGROK_DOMAIN`


## [0.1.0] - 2026-09-06

### ✨ Features

- Initial project scaffold generated from the `mcp-demo` template
