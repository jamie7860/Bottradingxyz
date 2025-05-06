import pandas as pd
import numpy as np
from smartapi import SmartConnect
import pyotp
import time
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator

# Angel One Credentials
api_key = "oFe09u88"
client_id = "AAAJ463076"
pwd = "7860"
totp_key = "RK2C2YUWSV74XKQETTEELQ2S6Y"
smartApi = SmartConnect(api_key=api_key)
token = pyotp.TOTP(totp_key).now()
session = smartApi.generateSession(client_id, pwd, token)
refreshToken = session["data"]["refreshToken"]
feedToken = smartApi.getfeedToken()

# Helper function to check for spike and indicators
def check_trade_conditions(df):
    df["EMA9"] = EMAIndicator(close=df["close"], window=9).ema_indicator()
    df["EMA21"] = EMAIndicator(close=df["close"], window=21).ema_indicator()
    macd = MACD(close=df["close"])
    df["MACD"] = macd.macd()
    df["MACD_SIGNAL"] = macd.macd_signal()
    rsi = RSIIndicator(close=df["close"])
    df["RSI"] = rsi.rsi()
    latest = df.iloc[-1]

    if (
        latest["EMA9"] > latest["EMA21"] and
        latest["MACD"] > latest["MACD_SIGNAL"] and
        latest["RSI"] > 50
    ):
        return "BUY"
    elif (
        latest["EMA9"] < latest["EMA21"] and
        latest["MACD"] < latest["MACD_SIGNAL"] and
        latest["RSI"] < 50
    ):
        return "SELL"
    return "HOLD"

# Dummy market data (replace with live data)
data = {"close": [150, 152, 153, 155, 157, 160, 157, 159, 162, 165]}
df = pd.DataFrame(data)
signal = check_trade_conditions(df)
print("Trade Signal:", signal)

if signal == "BUY":
    print("Buying Option... (Auto-entry)")
elif signal == "SELL":
    print("Selling Option... (Auto-entry)")
else:
    print("No trade condition met.")