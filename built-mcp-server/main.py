from mcp.server.fastmcp import FastMCP


app = FastMCP("Demo")

@app.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

@app.resource("greeting://{name}") 
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"

@app.prompt()
def greet_user(name: str, style: str = "friendly") -> str:

    """ Get a greeting promptly based on the style specified. """
    styles = {
        "friendly": "Please write a warm ,friendly greeting.",
        "formal": "please write a formal,professional greeting.",

        "casual": "please write a casual, relaxed greeting."
    }
    return f"{styles.get(style, styles['friendly'])} for someone named {name}."