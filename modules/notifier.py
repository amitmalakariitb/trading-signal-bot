import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send(msg):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": msg}
    requests.post(url, json=payload)

# Demo block for direct testing
if __name__ == "__main__":
    send("Demo: Telegram notification test from notifier.py.")
