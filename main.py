import logging
from logging.config import fileConfig

from telethon.tl.types import UpdateNewChannelMessage
from communication.telegram_driver import TelegramDriver
from config.config import CryptoBotConfig
from patterns.pattern_parser import PatternParser

# General
config = CryptoBotConfig()
user_config = config.get_user_config()
bot_dialog_config = config.get_bot_dialogs()
pattern_config = config.get_pattern_config()
fileConfig('config/logging_config.ini')
logger = logging.getLogger()
td = TelegramDriver(user_config, bot_dialog_config)
td.log_started()


def callback(update):
    if isinstance(update, UpdateNewChannelMessage):
        msg = update.message
        logger.debug(update)
        try:
            # check if its known channel
            channel_id = msg.to_id.channel_id
            if channel_id in pattern_config:
                pattern_parser = PatternParser(pattern_config[channel_id], msg.message)
                money, buy, stop, sell = pattern_parser.parse()
                result = "Money : " + money \
                         + "\r\nBuy : " + str(buy) \
                         + "\r\nSell : " + str(sell) \
                         + "\r\nStop : " + str(stop)
                # logger.info(result)
                td.send_to_channel(user_config["crypto-bot"]["channel_id"], result)
            else:
                raise Exception("Unknown channel")
        except Exception as e:
            # logger.debug(update)
            logger.warning(e)


def main():
    td.connect()
    td.add_handler_update(callback)
    td.call_idle()
    td.disconnect()


if __name__ == '__main__':
    main()
