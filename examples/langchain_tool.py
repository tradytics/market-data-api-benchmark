"""LangChain / LangGraph tool wrapping the official Tradytics Python SDK.

Install:
    pip install tradytics langchain-core
    export TRADYTICS_API_KEY="tdy_..."
"""

import json
from langchain_core.tools import tool
from tradytics import Client

_client = Client()


@tool
def tradytics_options_flow(symbol: str, min_premium: int = 250000, limit: int = 10) -> str:
    """Fetch stitched US options flow orders (sweeps, blocks, splits with inferred side) for a ticker."""
    res = _client.options.flow(symbol=symbol.upper(), min_premium=min_premium, limit=limit)
    return json.dumps(res.get("data", []))


@tool
def tradytics_dealer_gamma(symbol: str) -> str:
    """Fetch dealer gamma exposure, gamma flip, call wall, and put wall for a US stock or ETF."""
    res = _client.options.exposure(symbol=symbol.upper(), greek="gamma")
    return json.dumps(res.get("data", {}))


@tool
def tradytics_sec_search(query: str, symbol: str = "", form: str = "10-K") -> str:
    """Run semantic passage search across SEC filings (10-K, 10-Q, 8-K) with EDGAR links."""
    params = {"q": query, "form": form, "limit": 5}
    if symbol:
        params["symbol"] = symbol.upper()
    res = _client.filings.search(**params)
    return json.dumps(res.get("data", []))


TOOLS = [tradytics_options_flow, tradytics_dealer_gamma, tradytics_sec_search]
