from config.config import load_config
import telebot

def main():
    config = load_config()

    bot = telebot.TeleBot(config["crypto-bot"]["token"])

    print(bot.get_updates(timeout=0.01))

    # my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
    #
    # print(my_bittrex.get_balance('BTC'))

    @bot.message_handler(commands=['herklos'])
    def send_something(message):
        bot.reply_to(message, "TEST--")

    #bot.polling()

main()