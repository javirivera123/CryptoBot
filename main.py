import logging
from logging.config import fileConfig

from telethon import TelegramClient

from config.config import load_config


def callback(update):
    logger = logging.getLogger()

    print(type(update))
    if "UpdateNewChannelMessage" in update:
        logger.info(update)
    else:
        logger.debug("other...")
    logger.debug(update)


def first_connection(client, config):
    client.send_code_request(config["telegram-api"]["phone_number"])
    myself = client.sign_in(config["telegram-api"]["phone_number"], input('Enter code: '))
    # print(myself.stringify())


def main():
    config = load_config()
    fileConfig('logging_config.ini')
    logger = logging.getLogger()

    # my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
    #
    # print(my_bittrex.get_balance('BTC'))

    client = TelegramClient("Test", config["telegram-api"]["api_id"], config["telegram-api"]["api_hash"],
                            update_workers=1, spawn_read_thread=False)

    #
    client.connect()
    if client.is_connected():

        if not client.is_user_authorized():
            first_connection(client, config)

            logger.debug("Client connected to Telegram.")
        client.add_update_handler(callback)
        client.idle()
        client.disconnect()
    else:
        logger.error("Client not connected")


if __name__ == '__main__':
    main()
