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
td = TelegramDriver(user_config)


def callback(update):
    if isinstance(update, UpdateNewChannelMessage):
        # todo check specified channel
        msg = update.message
        try:
            pattern_parser = PatternParser(pattern_config["DLavrov"], msg.message)
            money, buy, stop, sell = pattern_parser.parse()
            result = "Money : " + money + "\r\nBuy : " + str(buy) + "\r\nSell : " + str(sell) + "\r\nStop : " + str(stop)
            # logger.info(result)
            td.send_to_channel(user_config["my_config"]["my_signal_channel"], result)
        except AttributeError as e:
            logger.exception(e)

        except Exception as e:
            logger.warning(e)


def main():
    td.connect()
    td.add_handler_update(callback)
    td.call_idle()
    td.disconnect()


if __name__ == '__main__':
    main()
