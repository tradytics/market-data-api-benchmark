"""Agno (Phidata) toolkit for Tradytics US stock, options, dark pool, and SEC filings data.

Install:
    pip install tradytics agno
    export TRADYTICS_API_KEY="tdy_..."
"""

import json
from agno.tools import Toolkit
from tradytics import Client


class TradyticsTools(Toolkit):
    def __init__(self, api_key: str | None = None):
        super().__init__(name="tradytics")
        self.client = Client(api_key=api_key) if api_key else Client()
        self.register(self.get_options_flow)
        self.register(self.get_dealer_gamma)
        self.register(self.get_dark_pool)
        self.register(self.search_sec_filings)

    def get_options_flow(self, symbol: str, min_premium: int = 250000, limit: int = 10) -> str:
        """Get stitched US options flow orders for a ticker."""
        return json.dumps(self.client.options.flow(symbol=symbol.upper(), min_premium=min_premium, limit=limit).get("data", []))

    def get_dealer_gamma(self, symbol: str) -> str:
        """Get dealer gamma exposure, gamma flip, call wall, and put wall."""
        return json.dumps(self.client.options.exposure(symbol=symbol.upper(), greek="gamma").get("data", {}))

    def get_dark_pool(self, symbol: str, limit: int = 10) -> str:
        """Get ranked dark pool block prints for a ticker."""
        return json.dumps(self.client.darkpool.prints(symbol=symbol.upper(), limit=limit).get("data", []))

    def search_sec_filings(self, query: str, symbol: str = "", form: str = "10-K") -> str:
        """Search SEC filings semantically and return matching passages with EDGAR URLs."""
        params = {"q": query, "form": form, "limit": 5}
        if symbol:
            params["symbol"] = symbol.upper()
        return json.dumps(self.client.filings.search(**params).get("data", []))
