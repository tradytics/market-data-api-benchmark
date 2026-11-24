"""CrewAI tool wrapping Tradytics market data (options flow, dark pools, dealer gamma, SEC search).

Install:
    pip install tradytics crewai
    export TRADYTICS_API_KEY="tdy_..."
"""

import json
from crewai.tools import BaseTool
from tradytics import Client


class TradyticsMarketDataTool(BaseTool):
    name: str = "tradytics_market_snapshot"
    description: str = (
        "Fetch options flow, dealer gamma flip/walls, and top ranked dark pool prints for a US ticker."
    )

    def _run(self, symbol: str) -> str:
        client = Client()
        sym = symbol.strip().upper()
        payload = {
            "quote": client.stocks.quotes(symbol=sym).get("data"),
            "options_flow": client.options.flow(symbol=sym, min_premium=250000, limit=5).get("data"),
            "dealer_gamma": client.options.exposure(symbol=sym, greek="gamma").get("data"),
            "dark_pool": client.darkpool.prints(symbol=sym, limit=5).get("data"),
        }
        return json.dumps(payload)
