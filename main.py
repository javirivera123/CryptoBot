import logging
from logging.config import fileConfig
from telethon import TelegramClient
from telethon.tl.types import UpdateNewChannelMessage

from config.config import CryptoBotConfig
from patterns.pattern_parser import PatternParser

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
        + " Stop : " + str(pattern_parser.get_stop_value()) + " Target : " + str(pattern_parser.get_target_value()))
        # logger.info("Message : " + str(result.message))


def first_connection(client, config):
    client.send_code_request(config["telegram-api"]["phone_number"])
    myself = client.sign_in(config["telegram-api"]["phone_number"], input('Enter code: '))
    logger.info(myself.stringify())


def main():
    # my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
    #
    # print(my_bittrex.get_balance('BTC'))

    client = TelegramClient("Test", user_config["telegram-api"]["api_id"], user_config["telegram-api"]["api_hash"],
                            update_workers=1, spawn_read_thread=False)

    #
    client.connect()
    if client.is_connected():

        if not client.is_user_authorized():
            first_connection(client, user_config)

            logger.info("Client connected to Telegram.")
        client.add_update_handler(callback)
        client.idle()
        client.disconnect()
    else:
        logger.error("Client not connected")


if __name__ == '__main__':
    main()
