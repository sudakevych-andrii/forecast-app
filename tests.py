import unittest

from telegram_config import config
from forecast import Forecast
from telegram import TelegramMessageSender


class TestForecast(unittest.TestCase):
    def setUp(self) -> None:
        self.forecast = Forecast("Kharkiv")
        self.success_status_code = 200

    def test_get_forecast_response_success(self):
        response = Forecast("Kharkiv").get_forecast()
        self.assertEqual(response.status_code, self.success_status_code)

    def test_get_forecast_response_fail(self):
        response = Forecast("Kharkivdsf").get_forecast()
        self.assertNotEqual(response.status_code, self.success_status_code)


class TestTelegramMessageSender(unittest.TestCase):
    def setUp(self) -> None:
        self.token = config['token']
        self.channel_id = "@" + config['channel_id']
        self.success_status_code = 200

    def test_send_message_response_success(self):
        pass


if __name__ == "__main__":
    unittest.main()
