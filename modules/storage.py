import sqlite3
from datetime import datetime, timedelta
import os

DB = "database.db"

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS alerts(
                symbol TEXT,
                strategy TEXT,
                timestamp TEXT
            )
        """)

def recently_alerted(symbol, strategy, days=5):
    with sqlite3.connect(DB) as conn:
        cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()
        row = conn.execute("SELECT MAX(timestamp) FROM alerts WHERE symbol=? AND strategy=?",
                           (symbol, strategy)).fetchone()
        last_alert = row[0]
        if last_alert is None:
            return False
        last_alert_dt = datetime.fromisoformat(last_alert)
        return (datetime.utcnow() - last_alert_dt).days < days

def save_alert(symbol, strategy):
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO alerts VALUES(?, ?, ?)",
                     (symbol, strategy, datetime.utcnow().isoformat()))
