import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient({
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

    
    jira_tools = await client.get_tools(server_name="jira")

    print(f"\n\nNumber of tools: {len(jira_tools)}")
    JIRA_WRITE_HINTS = ("create", "update", "transition", "comment", "edit", "add", "delete")
    jira_write = [t for t in jira_tools if any(h in t.name.lower() for h in JIRA_WRITE_HINTS)]
    jira_read = [t for t in jira_tools if t not in jira_write]
    
    print("\nRead-only Jira tools")
    for tool in jira_read:
        print("\n", "="*10, tool.name, "="*10, "\n") 
        print(tool.description)
    
    print("\nWrite Jira tools")
    for tool in jira_write:
        print("\n", "="*10, tool.name, "="*10, "\n") 
        print(tool.description)
    
    


if __name__ == "__main__":
    asyncio.run(main())
