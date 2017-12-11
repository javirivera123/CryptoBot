import logging

from telethon import TelegramClient


class TelegramDriver:
    def __init__(self, config):
        self.config = config
        self.client = None
        self.logger = logging.getLogger()

    def first_connection(self):
        self.client.send_code_request(self.config["telegram-api"]["phone_number"])
        myself = self.client.sign_in(self.config["telegram-api"]["phone_number"], input('Enter code: '))
        self.logger.info(myself.stringify())

    def connect(self):
        self.client = TelegramClient("User", self.config["telegram-api"]["api_id"],
                                     self.config["telegram-api"]["api_hash"],
                                     update_workers=1,
                                     spawn_read_thread=False)

        self.client.connect()
        if self.client.is_connected():

            if not self.client.is_user_authorized():
                self.first_connection()
                self.logger.info("Client connected to Telegram.")
        else:
            self.logger.error("Client not connected")

    def send_to_channel(self, channel_id, msg):
        self.client.send_message(channel_id, msg)

    def add_handler_update(self, callback):
        self.client.add_update_handler(callback)

    def call_idle(self):
        self.client.idle()

    def disconnect(self):
        self.client.disconnect()
