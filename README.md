# mcp-demo

<p>
    <a href="https://www.repostatus.org/#wip"><img src="https://www.repostatus.org/badges/latest/wip.svg" alt="Project Status: WIP – Initial development is in progress."/></a>
    <a href="https://github.com/Dantos7/mcp-demo"><img alt="Version" src="https://img.shields.io/github/v/release/Dantos7/mcp-demo"></a>
</p>

A demo project to test out MCP.

## 🧰 Tooling

- [uv](https://docs.astral.sh/uv/) for project management and packaging
- [ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [ty](https://docs.astral.sh/ty/) for type checking
- [prek](https://prek.j178.dev/) for managing hooks
- [pytest](https://docs.pytest.org/en/stable/index.html) and [coverage](https://coverage.readthedocs.io/en/stable/) for testing and code coverage
- [poethepoet](https://poethepoet.natn.io/) for task management
- [typos](https://github.com/crate-ci/typos) for spell checking
- [EditorConfig](https://editorconfig.org/) for maintaining consistent coding styles

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
src/mcp_demo/         # package source code
tests/unit/           # unit tests
tests/integration/    # integration tests
```

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
