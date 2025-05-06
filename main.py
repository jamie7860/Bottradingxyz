
import pandas as pd
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator

# Dummy close price data for example
df = pd.DataFrame({
    "close": [150, 152, 153, 151, 150, 155, 158, 160, 157, 159, 162, 165]
})

# Calculate EMA indicators
df["EMA9"] = EMAIndicator(df["close"], window=9).ema_indicator()
df["EMA21"] = EMAIndicator(df["close"], window=21).ema_indicator()

# Calculate MACD indicators
macd = MACD(df["close"])
df["MACD"] = macd.macd()
df["MACD_SIGNAL"] = macd.macd_signal()

# Calculate RSI
df["RSI"] = RSIIndicator(df["close"]).rsi()

print(df.tail())
from fastapi import FastAPI
import threading
from fastapi import FastAPI
import threading

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Bot is running"}

def run_bot():
    # Yahan se tumhara pura trading bot ka code chalega
    import your_bot_logic  # replace this with actual logic or move code here

threading.Thread(target=run_bot).start()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Bot is running"}

def run_bot():
    # Yahan se tumhara pura trading bot ka code chalega
    import your_bot_logic  # replace this with actual logic or move code here

threading.Thread(target=run_bot).start()
