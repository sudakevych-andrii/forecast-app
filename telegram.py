import requests
from telegram_config import config
from forecast import WeatherForecast


class TelegramMessageSender:
    def __init__(self, channel_id, token):
        self._channel_id = f'@{channel_id}'
        self._token = token
        self.__url = f'https://api.telegram.org/bot{self._token}'
        self.__method = f'{self.__url}/sendMessage'

    def send_message(self, text):
        if type(text) == str and len(text):
            try:
                requests.post(self.__method, data={"chat_id": self._channel_id, "text": text})
            except requests.RequestException as e:
                print("Exception (send forecast):", e)
