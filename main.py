from time import sleep

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from config.config import load_config
import telebot
from telethon import TelegramClient

config = load_config()
dialogs = []
users = []
chats = []

last_date = None
chunk_size = 20

client = TelegramClient('some_name', config["telegram-api"]["api_id"], config["telegram-api"]["api_hash"])
client.connect()
client.is_user_authorized()
client.send_code_request(config["telegram-api"]["phone_number"])
myself = client.sign_in(config["telegram-api"]["phone_number"], input('Enter code: '))

channel = client.get_entity('https://t.me/dlavrov_tch')


while True:
    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size
             ))
    dialogs.extend(result.dialogs)
    users.extend(result.users)
    chats.extend(result.chats)
    if not result.messages:
        break
    last_date = min(msg.date for msg in result.messages)
    sleep(2)

print(result)

# def main():


    # bot = telebot.TeleBot(config["crypto-bot"]["token"])
    #
    # print(bot.get_updates(timeout=0.01))



    # my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
    #
    # print(my_bittrex.get_balance('BTC'))

    # @bot.message_handler(commands=['herklos'])
    # def send_something(message):
    #     bot.reply_to(message, "TEST--")
    #
    # bot.polling()


# main()
