import os, random, 
from telegram.ext import ( Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOT = 867671952
GRUPO = -368576776
GRADOS = InlineKeyboardMarkup([
            [InlineKeyboardButton('DAM',  callback_data='DAM')],
            [InlineKeyboardButton('DAW',  callback_data='DAW')],
            [InlineKeyboardButton('ASIR', callback_data='ASIR')]
])

def welcome(bot, update):
    users=[]
    gifs_adios = [ "1msH5HVV15d9eDglxh", "LZ4YlxtpHWoIXMFLFC",
                    "yNsRn4T0w6RFhXfTuA", "11BA7hWtTxwYRl6LhT",
                    "iqsD5Adjv9xPmnY1aA", "DCOgUFTPoCWqGLoyc7",
                    "3mJq3kj56UY99L2zzJ" ]
    gifs_hola = ["zI19V0pvL7VbzQymhm", "fx8jM7DmZf1M6sAwjW",
                    "2ioxfkHEjiJ27vaAdX", "ywIkAteChv7FTMQr5H",
                    "t7Ec41alMQJ43LDxNP", "iqHvtgizgFmyO1oIwc",
                    "E1CkNbxO2PadTRQVSc"]

    for nuevoUsuario in update.message.new_chat_members:
        if nuevoUsuario['id'] != BOT: 
            users.append(nuevoUsuario['first_name'])
            print(nuevoUsuario)
        else: 
            bot.sendDocument(chat_id=update.message.chat_id,
                                document =
                                "https://media1.giphy.com/media/"+random.choice(gifs_adios)+"/giphy.gif",
                                caption = "Lo siento, no puedo seguir aquí, mi dueño me mataría.\n\n"
                            + "Si queréis verme en acción, os jodeis.")
            bot.leave_chat(update.message.chat.id)
            return False
    for user in users:
        bot.sendDocument(chat_id=update.message.chat_id,
                            document =
                            "https://media1.giphy.com/media/"+random.choice(gifs_hola)+"/giphy.gif",
                            caption = "Hola {}".format(user),
                            reply_to_message_id=update.message.message_id)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def upload(update, context):
    update.message.reply_text('Please choose:', reply_markup=CATEGORIAS)

def button(update, context):
    query = update.callback_query
    
    if query['from_user']['id'] == query.message.reply_to_message['from_user']['id']:
        query.edit_message_text(text="Selected option: {}".format(query.data), reply_markup=CATEGORIAS)
    else:
       print("Mal")        

def es_inadecuado(update):
    return update.message.chat.id != GRUPO

updater = Updater(os.environ["telegram_token"], use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('upload', upload))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
