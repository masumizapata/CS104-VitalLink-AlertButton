import os
import time
import requests
import RPi.GPIO as GPIO
from dotenv import load_dotenv

# Cargar las variables ocultas
load_dotenv()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Leer las credenciales de forma segura
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

while True:
    if GPIO.input(7) == GPIO.HIGH:
        print("Someone pressed the alert button!")
        
        data = {
            "chat_id": chat_id,
            "text": "Someone pressed the alert button!"
        }
        requests.post(url, json=data)
        
        time.sleep(2)
        
    time.sleep(0.1)
