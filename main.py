import os
import pandas as pd
from dotenv import load_dotenv

from modules.data_fetcher import fetch_bulk_daily
from modules.strategies import STRATEGIES
from modules.notifier import send
from modules.storage import init_db, recently_alerted, save_alert

load_dotenv()
init_db()

def run():
    watch = pd.read_csv("watchlist.csv")
    symbols = list(watch["symbol"].values)
    data = fetch_bulk_daily(symbols)
    
    for _, row in watch.iterrows():
        sym = row["symbol"]
        strategy = row["strategy"]
        # print(f"\nProcessing symbol: {sym} with strategy: {strategy}")
        df = data[sym].copy()
        df.columns = [c.lower() for c in df.columns]

        signals = STRATEGIES[strategy](df, sym)
        # print(f"Signals generated for {sym}: {signals}")

        for sig in signals:
            if not recently_alerted(sym, strategy):
                msg = f"{sig['type']} SIGNAL\n{sym}\nReason: {sig['reason']}\nPrice: {sig['price']}"
                print(f"Sending notification: {msg}")
                send(msg)
                save_alert(sym, strategy)
            else:
                print(f"Notification for {sym} ({strategy}) already sent recently. Skipping.")


if __name__ == "__main__":
    run()
