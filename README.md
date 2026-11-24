# Stock Market Data API & MCP Benchmark (2026)

Open, reproducible comparison of US stock market, options, dark pool, SEC filings, and prediction-market APIs and MCP servers for Python, JavaScript, and AI agents.

Maintained by [Tradytics](https://tradytics.com/docs) with transparent methodology and runnable benchmark code. Corrections and PRs from any provider are welcome.

---

## 1. Dataset Coverage Matrix (November 2026)

| Provider | Quotes & Bars | Options Chains | Stitched Options Flow | Dealer GEX / Vanna / Charm | Ranked Dark Pools | Fundamentals & Segments | SEC Semantic Search & Transcripts | 13F / Insiders / Congress | Prediction Markets | Stock Perpetuals | Official MCP Server | Free Tier |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **[Tradytics](https://tradytics.com/docs)** | Yes | Yes | Yes (since Jan 2022) | Yes | Yes (12m rank) | Yes | Yes | Yes | Kalshi + Polymarket | Yes | Hosted OAuth + `tradytics-mcp` | 50/day (all datasets, no card) |
| **Massive (Polygon.io)** | Yes (ticks/WS) | Yes | Raw ticks only | No | Raw prints only | Basic XBRL | No | No | No | No | Yes | 5/min delayed |
| **Alpha Vantage** | Yes (global/FX) | Paid | No | No | No | Core statements | No | No | No | No | Yes | 25/day |
| **Financial Modeling Prep** | Yes (global) | No | No | No | No | Deep global | Filings + transcripts | Yes | No | No | Yes | Limited free |
| **Finnhub** | Yes (global) | No | No | No | No | Yes | Filings + transcripts | Insiders | No | No | Community | 60/min basic |
| **Financial Datasets** | Yes (US) | No | No | No | No | Yes | Sections only | Insiders + 13F | No | No | Yes | Pay-per-call |
| **Unusual Whales** | Limited | Yes | Yes (1-2y) | Paid | Prints (no 12m rank) | No | No | Yes | Polymarket only | No | Yes | No free API |
| **Quiver Quantitative** | Limited | No | No | No | Off-exchange totals | No | No | Yes | Yes | No | Yes | Limited |
| **Databento** | Institutional L2/L3 | Raw OPRA | Raw only | No | Raw only | No | No | No | No | No | No | $125 credit |
| **EODHD** | Yes (global) | EOD | No | No | No | Deep global | No | Insiders | No | No | Yes | Limited free |
| **`yfinance` (unofficial)** | Delayed | Current only | No | No | No | Basic summary | No | No | No | No | Community | Unmetered (no SLA) |

---

## 2. Entry Pricing & Agent Economics

| Provider | Free Tier | Entry Paid API | High-Volume / Pro Tier | Pay-Per-Call (No Account) |
| :--- | :--- | :--- | :--- | :--- |
| **Tradytics** | 50 calls/day (5/min) | Plus: $39/mo or $299/yr (1,000/day) | Pro: $69/mo or $499/yr (50,000/day, app included) | x402 USDC on Base |
| **Massive (Polygon.io)** | 5 calls/min (delayed) | $29/mo per asset class | $79-$199+/mo per asset class | No |
| **Alpha Vantage** | 25 calls/day | $49.99/mo (75 req/min) | $149.99+/mo | No |
| **FMP** | Limited free | ~$22-$59/mo | $149+/mo | No |
| **Unusual Whales** | None (separate from app) | $99/mo (25k/mo, 1y flow) | $150-$375/mo | No |

---

## 3. Run the Live Latency & Schema Benchmark

Supply API keys for any providers you want to benchmark and run `benchmark.py` (uses Python standard library only, zero dependencies):

```bash
export TRADYTICS_API_KEY="tdy_..."
# Optional rival keys to compare side-by-side:
# export MASSIVE_API_KEY="..."
# export ALPHAVANTAGE_API_KEY="..."
# export FMP_API_KEY="..."
# export FINNHUB_API_KEY="..."

python benchmark.py --symbol NVDA --runs 5
```

---

## 4. Agent Framework Examples (`examples/`)

Drop-in 15-line examples wiring popular AI agent frameworks to live market data over MCP (`https://tradytics.com/mcp` or `npx -y tradytics-mcp`) or the Python SDK (`pip install tradytics`):

- [`examples/openai_agents_mcp.py`](examples/openai_agents_mcp.py): OpenAI Agents SDK with hosted Streamable HTTP MCP
- [`examples/langchain_tool.py`](examples/langchain_tool.py): LangChain / LangGraph tool wrapping `tradytics` SDK
- [`examples/crewai_tool.py`](examples/crewai_tool.py): CrewAI custom tool for options flow, dealer gamma, and SEC filings
- [`examples/agno_toolkit.py`](examples/agno_toolkit.py): Agno (Phidata) toolkit for multi-dataset equity & options research

## License

MIT. Contributions, benchmark corrections, and PRs adding new providers are welcome.
