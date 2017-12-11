import logging
from logging.config import fileConfig
from telethon.tl.types import UpdateNewChannelMessage
from config.config import CryptoBotConfig
from patterns.pattern_parser import PatternParser
from telegram.telegram_driver import TelegramDriver

# General

config = CryptoBotConfig()
user_config = config.get_user_config()
pattern_config = config.get_pattern_config()
fileConfig('config/logging_config.ini')
logger = logging.getLogger()


def callback(update):
    if isinstance(update, UpdateNewChannelMessage):
        msg = update.message
        pattern_parser = PatternParser(pattern_config["Crypto_Experts"], msg.message)

        # todo check specified channel

        logger.info(update)
        logger.info("Buy : " + str(pattern_parser.get_buy_value()) + " Sell : " + str(pattern_parser.get_sell_value())
                    + " Stop : " + str(pattern_parser.get_stop_value()) + " Target : " + str(
            pattern_parser.get_target_value()))
        # logger.info("Message : " + str(result.message))


def main():
    td = TelegramDriver(config)
    td.connect()
    td.add_handler_update(callback)
    td.call_idle()
    td.disconnect()


if __name__ == '__main__':
    main()
