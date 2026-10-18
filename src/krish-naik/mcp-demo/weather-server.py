from fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    return f"The current weather in {city} is raining with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8001)