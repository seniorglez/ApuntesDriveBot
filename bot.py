import os
from telegram.ext import Updater, CommandHandler

def welcome(bot, update):


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def es_adecuado(update):
    return update.message.chat.id == -368576776

updater = Updater(os.environ["telegram_token"])

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
