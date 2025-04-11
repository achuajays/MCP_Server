# Example Linkedin Profile MCP  
A simple example of an MCP (Message Command Protocol) server that returns anime titles.  

## How to Use  
This MCP server is configured to return  Linkedin data based on a url.   

## Setting Up the Server  
To install and run the Linkedin Profile MCP server, follow these steps:  

```bash 
git clone https://github.com/achuajays/MCP_Server.git
cd MCP_Server/Linkedin_Profile_Mcp
```

Create a .env file and set up 
```bash
RAPID_API_KEY
```

## Running the MCP Server  

### Installing and Running in Claude Desktop  
If you're using Claude Desktop, you can install and run the server with:  
```sh
mcp install Linkedin_Profile_mcp.py
```  

To test the server using the MCP Inspector:  
```sh
mcp dev Linkedin_Profile_mcp.py
```  

### Running the Standalone MCP Development Tools  
To run the `mcp` command with `uv`:  
```sh
uv run mcp
```  

## Example `mcpServers` Configuration  
Here’s an example configuration to run the Anime MCP server:  
```json
{
  "mcpServers": {
    "anime_mcp": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "D:\\mcp\\Linkedin_Profile_mcp.py"
      ]
    }
  }
}
```  
    
