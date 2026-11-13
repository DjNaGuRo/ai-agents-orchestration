from langchain_mcp_adapters.client import MultiServerMCPClient

mcp_client = MultiServerMCPClient({
    "notion": {
        "transport": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "mcp-remote",
            "https://mcp.notion.com/mcp",
        ],
    },
    "jira": {
        "transport": "stdio",
        "command": "npx",
        "args": [
            "-y",
            "mcp-remote",
            "https://mcp.atlassian.com/v2/mcp?tools=all"
        ]
    }
})