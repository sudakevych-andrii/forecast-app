import requests
from datetime import datetime


class Forecast:
    def __init__(self, city):
        self.city = city
        self.app_id = "905db094e4f5be359d649e0ce6bfa2cd"

    def get_forecast(self):
        try:
            return requests.get(
                "http://api.openweathermap.org/data/2.5/weather",
                params={'q': self.city, 'units': 'metric', 'lang': 'en', 'APPID': self.app_id}
            )
        except requests.RequestException as e:
            print("Exception (weather):", e)

    def display_forecast(self):
        data = self.get_forecast().json()
        return f"City: {data['name']}\n" \
               f"Time: {datetime.today().strftime('%H:%M:%S %d-%m-%Y')}\n" \
               f"Conditions: {data['weather'][0]['description']}\n" \
               f"Temp: {data['main']['temp']}"
