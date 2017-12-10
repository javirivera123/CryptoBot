from telegram.ext import Updater, MessageHandler, Filters, ConversationHandler, CommandHandler, RegexHandler

from config.config import load_config

SIGNAL, OTHER = range(2)

def start(bot, update):
    print("BEGIN")
    return SIGNAL


def echo(bot, update):
    print(update.message.text)
    # update.message.reply_text(update.message.text)
    return SIGNAL


def cancel(bot, update):
    print("STOP")
    return ConversationHandler.END


def main():
    config = load_config()

    # my_bittrex = Bittrex(config["bittrex-key"]["key"], config["bittrex-key"]["secret"], api_version=API_V2_0)
    #
    # print(my_bittrex.get_balance('BTC'))

    updater = Updater(config["crypto-bot"]["token"])

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, start)],

        states={
            SIGNAL: [MessageHandler(Filters.text, echo)]
        },

        fallbacks=[MessageHandler(Filters.text, cancel)]
    )
    #
    # GENDER: [RegexHandler('^(Boy|Girl|Other)$', gender)],
    #
    # PHOTO: [MessageHandler(Filters.photo, photo),
    #         CommandHandler('skip', skip_photo)],
    #
    # LOCATION: [MessageHandler(Filters.location, location),
    #            CommandHandler('skip', skip_location)],
    #
    # BIO: [MessageHandler(Filters.text, bio)]

    dp.add_handler(conv_handler)

    # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    # updater.bot.getChat("https://t.me/dlavrov_tch")

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
