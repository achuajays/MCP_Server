import requests
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    raise ValueError("RAPID_API_KEY is not set in the .env file")

mcp = FastMCP("fun_facts")

@mcp.tool()
def get_fun_facts() -> dict:
    """Fetch a list of fun facts from the RapidAPI Fun Facts API."""
    url = "https://fun-facts1.p.rapidapi.com/api/fun-facts"
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "fun-facts1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    mcp.run()
