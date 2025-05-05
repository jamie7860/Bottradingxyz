from smartapi import SmartConnect
import pyotp

# === CONFIGURATION ===
API_KEY     = "oFe09u88"
CLIENT_CODE = "AAAJ463076"
PASSWORD    = "7860"
TOTP_SECRET = "RK2C2YUWSV74XKQETTEELQ2S6Y"
# ======================

# Generate TOTP using secret key
totp = pyotp.TOTP(TOTP_SECRET).now()

# Create SmartAPI session
obj = SmartConnect(api_key=API_KEY)

try:
    data = obj.generateSession(CLIENT_CODE, PASSWORD, totp)
    auth_token = data['data']['jwtToken']
    refresh_token = data['data']['refreshToken']
    print("Login Successful")
    
    # === PLACEHOLDER: Add your trading strategy here ===
    print("Bot is ready to trade...")
    # ==================

except Exception as e:
    print("Login Failed:", e)
