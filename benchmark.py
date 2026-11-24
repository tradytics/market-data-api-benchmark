"""Reproducible latency and payload benchmark across stock market data APIs.

Zero external dependencies (Python 3.8+ stdlib only). Set env vars for any
providers you want to test and run:

    export TRADYTICS_API_KEY="tdy_..."
    python benchmark.py --symbol NVDA --runs 5
"""

from __future__ import annotations

import argparse
import json
import os
import statistics
import time
import urllib.error
import urllib.request


def build_targets(symbol: str) -> list[tuple[str, str, str]]:
    targets = []
    if k := os.getenv("TRADYTICS_API_KEY"):
        targets.append(("Tradytics (quotes)", f"https://tradytics.com/api/public/v1/stocks/quotes?symbol={symbol}&apiKey={k}", ""))
        targets.append(("Tradytics (options flow)", f"https://tradytics.com/api/public/v1/options/flow?symbol={symbol}&limit=5&apiKey={k}", ""))
        targets.append(("Tradytics (dealer gamma)", f"https://tradytics.com/api/public/v1/options/exposure?symbol={symbol}&greek=gamma&apiKey={k}", ""))
        targets.append(("Tradytics (SEC search)", f"https://tradytics.com/api/public/v1/filings/search?q=revenue+growth&symbol={symbol}&limit=3&apiKey={k}", ""))
    if k := os.getenv("MASSIVE_API_KEY") or os.getenv("POLYGON_API_KEY"):
        targets.append(("Massive/Polygon (prev bar)", f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?apiKey={k}", ""))
    if k := os.getenv("ALPHAVANTAGE_API_KEY"):
        targets.append(("Alpha Vantage (quote)", f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={k}", ""))
    if k := os.getenv("FMP_API_KEY"):
        targets.append(("FMP (quote)", f"https://financialmodelingprep.com/stable/quote?symbol={symbol}&apikey={k}", ""))
    if k := os.getenv("FINNHUB_API_KEY"):
        targets.append(("Finnhub (quote)", f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={k}", ""))
    return targets


def probe(url: str, auth_header: str = "") -> tuple[int, float, int]:
    headers = {"User-Agent": "market-data-api-benchmark/1.0"}
    if auth_header:
        headers["Authorization"] = auth_header
    req = urllib.request.Request(url, headers=headers)
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read()
            ms = (time.perf_counter() - t0) * 1000.0
            json.loads(body.decode("utf-8", errors="replace"))
            return resp.status, ms, len(body)
    except urllib.error.HTTPError as exc:
        return exc.code, (time.perf_counter() - t0) * 1000.0, 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark stock market APIs.")
    parser.add_argument("--symbol", default="NVDA", help="Ticker symbol (default: NVDA)")
    parser.add_argument("--runs", type=int, default=5, help="Requests per endpoint (default: 5)")
    args = parser.parse_args()

    targets = build_targets(args.symbol.upper())
    if not targets:
        print("Set at least one API key env var (e.g. TRADYTICS_API_KEY, MASSIVE_API_KEY, ALPHAVANTAGE_API_KEY, FMP_API_KEY, FINNHUB_API_KEY).")
        return

    print(f"| Endpoint | Status | Median (ms) | P95 (ms) | Payload (bytes) |")
    print(f"| :--- | :---: | :---: | :---: | :---: |")
    for name, url, auth in targets:
        latencies, statuses, sizes = [], [], []
        for _ in range(args.runs):
            st, ms, sz = probe(url, auth)
            statuses.append(st)
            latencies.append(ms)
            sizes.append(sz)
        ok_count = sum(1 for s in statuses if s == 200)
        med = statistics.median(latencies)
        p95 = sorted(latencies)[max(0, int(len(latencies) * 0.95) - 1)]
        avg_sz = int(statistics.mean(sizes))
        print(f"| {name} | {ok_count}/{args.runs} HTTP 200 | {med:.0f} | {p95:.0f} | {avg_sz:,} |")


if __name__ == "__main__":
    main()
