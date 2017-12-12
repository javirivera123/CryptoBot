import json
import logging


class CryptoBotConfig:

    def __init__(self):
        self.user = None
        self.patterns = None
        self.dialogs = None
        self.logger = logging.getLogger()
        self.load_config()
        self.load_patterns()

    def load_config(self):
        try:
            with open('config/config.json') as json_data_file:
                self.user = json.load(json_data_file)
            self.logger.info("User config loaded successfully.")
        except Exception as e:
            self.logger.exception(e)

    def load_dialogs(self):
        try:
            with open('config/bot_dialog.json') as json_data_file:
                self.dialogs = json.load(json_data_file)
            self.logger.info("Bot dialog config loaded successfully.")
        except Exception as e:
            self.logger.exception(e)

    def load_patterns(self):
        try:
            with open('patterns/patterns.json') as json_data_file:
                self.patterns = json.load(json_data_file)
            self.logger.info("Pattern config loaded successfully.")
        except Exception as e:
            self.logger.exception(e)

    def format_patterns(self):
        result = {}
        for pattern in self.patterns.values():
            result[pattern["channel_id"]] = pattern
        return result

    def get_user_config(self):
        return self.user

    def get_bot_dialogs(self):
        return self.dialogs

    def get_pattern_config(self):
        return self.format_patterns()
