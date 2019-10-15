import requests


class ForecastBot:
    def __init__(self):
        self.token = "843960086:AAE_5xQIej-qzgqQ6EkPhbe-DhYjg8HRp1U"
        self.url = "https://api.telegram.org/bot" + self.token
        self.channel_id = "@forecastkharkivtest"
        self.method = self.url + "/sendMessage"

    def send_forecast(self, text):
        requests.post(self.method, data={"chat_id": self.channel_id, "text": text})

