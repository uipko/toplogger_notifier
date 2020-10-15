"""
Module for interaction with Telegram bot.
"""
import requests


# pylint: disable=too-few-public-methods
class Telegram:
    """
    Handle communication with Telegram bot.
    """

    def __init__(self, token, chat_id):
        # TODO: move token to config file
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{token}"

    def send_message(self, message):
        """
        Send a message to the telegram bot.
        """
        payload = {
            'chat_id': self.chat_id,
            'text': message,
            'parse_mode': 'HTML'
        }

        return requests.post(f"{self.api_url}/sendMessage", data=payload).content
