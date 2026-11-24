"""Connect the OpenAI Agents SDK directly to Tradytics hosted MCP (Streamable HTTP).

Install:
    pip install openai-agents
    export OPENAI_API_KEY="sk-..."
    export TRADYTICS_API_KEY="tdy_..."
"""

import asyncio
import os
from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp


async def main() -> None:
    api_key = os.environ["TRADYTICS_API_KEY"]
    async with MCPServerStreamableHttp(
        name="Tradytics",
        params={
            "url": "https://tradytics.com/mcp",
            "headers": {"Authorization": f"Bearer {api_key}"},
        },
    ) as mcp:
        analyst = Agent(
            name="Market Analyst",
            instructions="Use Tradytics MCP tools to answer with exact, dated market data.",
            mcp_servers=[mcp],
        )
        result = await Runner.run(
            analyst,
            "Summarize NVDA's top options flow, dealer gamma flip/walls, and top ranked dark pool levels.",
        )
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
