# 🧠 Trading Signal Bot

Automated **daily stock signal scanner** that analyzes **End-Of-Day (EOD)** market data using technical indicator strategies (EMA crossover, RSI, MACD planned, Volume breakout planned) and sends **BUY / WATCH (near-signal)** alerts via **Telegram**.  
Runs automatically at **4:00 PM IST** every trading day using **GitHub Actions**.

---

## ✨ Features

| Feature | Status |
|---------|--------|
Daily EOD analysis | ✔
Runs automatically every trading day at 4 PM IST | ✔
Telegram notifications | ✔
BUY + WATCH (near-buy) alerts | ✔
SQLite alert history & duplicate prevention | ✔
Efficient multi-ticker download | ✔ (`yfinance` batching)
Pluggable strategy engine | ✔
GitHub Actions automation | ✔

---

## 🏛 System Architecture



Watchlist.csv (Symbols + Strategy Mapping)
↓
GitHub Actions Scheduler (4 PM IST)
↓
Efficient Data Fetcher (yfinance multi-symbol batching)
↓
Strategy Engine (EMA / RSI / MACD / Volume etc.)
↓
Signal Classification (BUY or WATCH)
↓
SQLite History (prevent duplicate alerts)
↓
Telegram Notification Delivery


## 📦 Installation & Local Testing

### 1️⃣ Clone the repository
```bash
git clone https://github.com/amitmalakariitb/trading-signal-bot.git
cd trading-signal-bot
````

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
# OR
venv\Scripts\activate        # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `config.env` file:

```env
TELEGRAM_BOT_TOKEN=xxxxx
TELEGRAM_CHAT_ID=xxxxx
DEFAULT_INTERVAL=1d
LOOKBACK_DAYS=250
NEAR_THRESHOLD_PERCENT=1.5
ALERT_COOLDOWN_DAYS=1
```

### 5️⃣ Add your stock watchlist

Create or edit `watchlist.csv`:

```csv
symbol,strategy
RELIANCE.NS,ema_crossover
TCS.NS,ema_rsi_combo
HDFCBANK.NS,rsi_dip
```

### 6️⃣ Run locally to test

```bash
python main.py
```

---

## 🚀 GitHub Actions Automation (Daily 4 PM IST)

Workflow file:

```
.github/workflows/daily_scan.yml
```

Scheduler config:

```yaml
on:
  schedule:
    - cron: "30 10 * * 1-5"   # 10:30 UTC = 4 PM IST
```

### Set GitHub Secrets:

```
Repo Settings → Secrets → Actions →
  TELEGRAM_BOT_TOKEN
  TELEGRAM_CHAT_ID
```

---

## 🔔 Telegram Alert Format

### BUY Signal Example

```
🚀 BUY SIGNAL
Symbol: RELIANCE.NS
Price: 2715.50
Strategy: EMA Crossover
Reason: EMA20 crossed above EMA50 (Bullish)
Timeframe: Daily
```

### WATCH Signal Example

```
👀 WATCHLIST ALERT
Symbol: TCS.NS
Price: 4120.10
Reason: EMA crossover likely soon (0.85% away)
Timeframe: Daily
```

---

## 🧠 Included Strategies

| Strategy        | Description                           |
| --------------- | ------------------------------------- |
| `ema_crossover` | EMA20 > EMA50 bullish crossover       |
| `rsi_dip`       | RSI bounce from oversold zone         |
| `ema_rsi_combo` | EMA crossover + RSI < 60 confirmation |

### Coming Soon

* MACD crossover
* Volume breakout
* Swing-high breakout

---

## 🛠 Technologies Used

| Component     | Tool                          |
| ------------- | ----------------------------- |
| Language      | Python 3.10                   |
| Market data   | `yfinance` batch multi-ticker |
| Indicators    | `ta` library                  |
| Scheduling    | GitHub Actions                |
| Notifications | Telegram Bot API              |
| History       | SQLite                        |

---

## 🧭 Roadmap

* [ ] Add MACD Strategy
* [ ] Add Volume Surge & Breakout Strategy
* [ ] Web Dashboard UI
* [ ] ML-based ranking & scoring
* [ ] P&L simulation & backtesting

---

## 📄 License

MIT License — Free to use & modify.

---

## ⭐ Support

If you find this project useful:

* ⭐ Star this repo
* 🐛 Report issues
* 🤝 Contribute pull requests

---

## 👤 Author

**Amit Malakar — IIT Bombay** 
AI Engineer • Algo Trading • Quant • ML • Full-Stack

---
