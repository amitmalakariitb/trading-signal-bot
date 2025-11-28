import pandas as pd
import numpy as np

def stochastic_buy(df, symbol, periodK=4, smoothK=3, periodD=3):
    signals = []
    # Calculate Stochastic %K
    lowest_low = df['low'].rolling(window=periodK, min_periods=periodK).min()
    highest_high = df['high'].rolling(window=periodK, min_periods=periodK).max()
    k = 100 * (df['close'] - lowest_low) / (highest_high - lowest_low)
    k = k.rolling(window=smoothK, min_periods=smoothK).mean()
    # Calculate Stochastic %D
    d = k.rolling(window=periodD, min_periods=periodD).mean()

    # Entry condition: both k and d below 20
    long_condition = (k < 20) & (d < 20)

    # Only consider the latest bar for buy signal
    if long_condition.iloc[-1]:
        signals.append({
            "symbol": symbol,
            "type": "BUY",
            "reason": "Stochastic %K and %D below 20",
            "price": df['close'].iloc[-1]
        })
    return signals

STRATEGIES = {
    "stochastic_buy": stochastic_buy
}