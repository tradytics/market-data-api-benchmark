<p align="center">
  <a href="https://tradytics.com/compare/best-stock-market-api"><img src="https://tradytics.com/api/v2/og/sdk.png?v=4" alt="Stock Market Data API & MCP Benchmark" width="100%"></a>
</p>

# Stock Market Data API & MCP Benchmark (2026)

Open, reproducible comparison of US stock market, options flow, dark pool, dealer gamma, SEC filings, and prediction-market APIs and MCP servers for Python, JavaScript, and AI agents.

[![Benchmark](https://img.shields.io/badge/providers-11%20compared-168eff)](https://tradytics.com/compare/best-stock-market-api)
[![Python](https://img.shields.io/badge/python-3.8%2B%20stdlib-16171a)](benchmark.py)
[![MCP](https://img.shields.io/badge/MCP-tradytics--mcp-16171a)](https://github.com/tradytics/tradytics-mcp)
[![License](https://img.shields.io/badge/license-MIT-16171a)](LICENSE)

Maintained by [Tradytics](https://tradytics.com/docs) with runnable latency probes and copy-paste agent framework integrations. Corrections and PRs from any provider are welcome.

## Dataset coverage matrix (November 2026)

| Provider | Quotes & Bars | Options Chains | Stitched Options Flow | Dealer GEX / Vanna / Charm | Ranked Dark Pools | Fundamentals & Segments | SEC Search & Transcripts | 13F / Insiders / Congress | Prediction Markets | Stock Perpetuals | Official MCP | Free Tier |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **[Tradytics](https://tradytics.com/docs)** | Yes | Yes | Yes (since Jan 2022) | Yes | Yes (12m rank) | Yes | Yes | Yes | Kalshi + Polymarket | Yes | Hosted + stdio | 50/day (all datasets) |
| **Massive (Polygon.io)** | Ticks / WS | Yes | Raw only | No | Raw only | Basic XBRL | No | No | No | No | Yes | 5/min delayed |
| **Alpha Vantage** | Global / FX | Paid | No | No | No | Core | No | No | No | No | Yes | 25/day |
| **FMP** | Global | No | No | No | No | Deep global | Filings + calls | Yes | No | No | Yes | Limited free |
| **Finnhub** | Global | No | No | No | No | Yes | Filings + calls | Insiders | No | No | Community | 60/min basic |
| **Financial Datasets** | US | No | No | No | No | Yes | Sections | Insiders + 13F | No | No | Yes | Pay-per-call |
| **Unusual Whales** | Limited | Yes | Yes (1-2y) | Paid | No 12m rank | No | No | Yes | Polymarket | No | Yes | No free API |
| **Quiver Quantitative** | Limited | No | No | No | Totals | No | No | Yes | Yes | No | Yes | Limited |
| **Databento** | L2 / L3 | Raw OPRA | Raw only | No | Raw only | No | No | No | No | No | No | $125 credit |
| **EODHD** | Global | EOD | No | No | No | Deep global | No | Insiders | No | No | Yes | Limited free |
| **`yfinance`** | Delayed | Current | No | No | No | Summary | No | No | No | No | Community | Unmetered (no SLA) |

## Run the latency & schema benchmark

Zero external dependencies (Python 3.8+ standard library). Export keys for whichever providers you want to measure:

```bash
export TRADYTICS_API_KEY="tdy_..."
# Optional side-by-side rivals:
# export MASSIVE_API_KEY="..."
# export ALPHAVANTAGE_API_KEY="..."
# export FMP_API_KEY="..."
# export FINNHUB_API_KEY="..."

python benchmark.py --symbol NVDA --runs 5
```

## Agent framework examples (`examples/`)

Drop-in examples connecting major AI agent frameworks to live market data over MCP (`https://tradytics.com/mcp` / `npx -y tradytics-mcp`) or the Python SDK (`pip install tradytics`):

| Framework | Example | Integration |
| :--- | :--- | :--- |
| **OpenAI Agents SDK** | [`examples/openai_agents_mcp.py`](examples/openai_agents_mcp.py) | `MCPServerStreamableHttp` -> `https://tradytics.com/mcp` |
| **LangChain / LangGraph** | [`examples/langchain_tool.py`](examples/langchain_tool.py) | `@tool` functions wrapping `tradytics` SDK |
| **CrewAI** | [`examples/crewai_tool.py`](examples/crewai_tool.py) | `BaseTool` pulling quotes, flow, dealer gamma and dark pools |
| **Agno (Phidata)** | [`examples/agno_toolkit.py`](examples/agno_toolkit.py) | `Toolkit` for options flow, gamma, dark pools and SEC search |

## Full write-ups & packages

- [Best stock market API (2026)](https://tradytics.com/compare/best-stock-market-api)
- [Best stock market MCP servers (2026)](https://tradytics.com/compare/best-stock-market-mcp-servers)
- [Tradytics MCP server](https://github.com/tradytics/tradytics-mcp) (`npx -y tradytics-mcp` | `uvx tradytics-mcp`)
- [Python & JS SDKs](https://tradytics.com/docs/libraries) (`pip install tradytics` | `npm install tradytics`)

MIT License.
