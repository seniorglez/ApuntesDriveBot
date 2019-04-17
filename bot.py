import os, random
from telegram.ext import ( Updater, CommandHandler, MessageHandler, Filters )

BOT = 867671952
GRUPO = -368576776

def welcome(bot, update):
    print(update.message.chat.id)
    for nuevoUsuario in update.message.new_chat_members:
        print(nuevoUsuario)
        soyYo = nuevoUsuario['id'] == BOT

    if soyYo and es_inadecuado(update):
        gifs = [ "9VcGZPbijSieHIGSj3",
                 "Bq7yz8gBShy5a", "yRXnlNNC9U7FC",
                 "cLJdDcAWTkW6k", "12ttoBXEqixfmo",
                 "c6DIpCp1922KQ", "jSxK33dwEMbkY",
                 "vkwAeqMEUSaoU", "106i22nkWV58SA" ]
        bot.sendDocument(chat_id=update.message.chat_id,
                            document = "https://media1.giphy.com/media/"+random.choice(gifs)+"/giphy.gif",
                            caption = "Lo siento, no puedo seguir aquí, mi dueño me mataría.\n\n"
                        + "Si queréis verme en acción, os jodeis.");
        bot.leave_chat(update.message.chat.id)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


def es_inadecuado(update):
    return update.message.chat.id != GRUPO

updater = Updater(os.environ["telegram_token"])

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

updater.start_polling()
updater.idle()
