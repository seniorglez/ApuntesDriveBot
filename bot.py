import os, random
from telegram.ext import ( Updater, CommandHandler, MessageHandler, Filters )

BOT = 867671952
GRUPO = -368576776

def welcome(bot, update):
    users=[]
    for nuevoUsuario in update.message.new_chat_members:
        if nuevoUsuario['id'] != BOT: 
            users.append(nuevoUsuario['first_name'])
            print(nuevoUsuario)
        elif nuevoUsuario['id'] == BOT: 
            gifs_adios = [ "9VcGZPbijSieHIGSj3",
                     "Bq7yz8gBShy5a", "yRXnlNNC9U7FC",
                     "cLJdDcAWTkW6k", "12ttoBXEqixfmo",
                     "c6DIpCp1922KQ", "jSxK33dwEMbkY",
                     "vkwAeqMEUSaoU", "106i22nkWV58SA" ]
            bot.sendDocument(chat_id=update.message.chat_id,
                                document =
                                "https://media1.giphy.com/media/"+random.choice(gifs_adios)+"/giphy.gif",
                                caption = "Lo siento, no puedo seguir aquí, mi dueño me mataría.\n\n"
                            + "Si queréis verme en acción, os jodeis.");
            bot.leave_chat(update.message.chat.id)
            return False
    for user in users:
        gifs_hola = ["zI19V0pvL7VbzQymhm"]
        bot.sendDocument(chat_id=update.message.chat_id,
                            document =
                            "https://media1.giphy.com/media/"+random.choice(gifs_hola)+"/giphy.gif",
                            caption = "Hola {}".format(user),
                            reply_to_message_id=update.message.message_id);

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
