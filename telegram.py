import requests
from telegram_config import config
from forecast import Forecast


class TelegramMessageSender:
    def __init__(self, token, channel_id):
        self.channel_id = "@" + channel_id
        self.token = token
        self.url = "https://api.telegram.org/bot" + self.token
        self.method = self.url + "/sendMessage"

    def send_message(self, text):
        if type(text) == str and len(text):
            try:
                requests.post(self.method, data={"chat_id": self.channel_id, "text": text})
            except requests.RequestException as e:
                print("Exception (send forecast):", e)

