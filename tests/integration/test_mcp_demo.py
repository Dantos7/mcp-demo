"""High-level tests for mcp_demo package."""


def test_package() -> None:
    """Test importing the mcp_demo package."""
    import mcp_demo  # noqa: PLC0415

    assert mcp_demo.__name__ == "mcp_demo"
