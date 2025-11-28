import yfinance as yf
import pandas as pd

def fetch_bulk_daily(symbols: list[str], lookback_days: int = 250):
    """Fetch OHLCV for all tickers in one batch to increase efficiency"""
    data = yf.download(
        tickers=symbols,
        period=f"{lookback_days}d",
        interval="1d",
        group_by="ticker",
        auto_adjust=False,
        threads=True
    )
    return data
