from mcp.server.fastmap import FastMcp 

app = FastMcp("Demo")

@app.tool()
def add(x: int, y: int) -> int:
    """Add two numbers."""
    return x + y

@app.resource("greeting://{name}") 
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"
