import os, random
from keyboards import generate_keyboard
from googleFileManager import GoogleFileManager
from telegram.ext import ( Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

BOT = 867671952
GRUPO = -368576776
file_manager = GoogleFileManager()

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

# Testing
def list_files(update, context):
    # print(file_manager.list_files())
    # update.message.reply_text(
    #    'Hello {}'.format(update.message.from_user.first_name))
    # files = file_manager.list_files_in("ApuntesDriveBot")
    files = file_manager.list_files_in(update.message.text[4:])
    mes = "Nada por aquí" if not files else "Archivos:"

    for f in files:
        mes += u'\n- [{file_name}]({file_link})({file_type})'.format(file_name=f['name'],
                                                        file_link="https://drive.google.com/file/d/"+f['id'],
                                                        file_type=f['type'])
    # print(mes)
    update.message.reply_text(mes, parse_mode="MARKDOWN", disable_web_page_preview="true")

def button(update, context):
    query = update.callback_query
    files = file_manager.list_files_in(query.data)
    standard_files = ""
    folders = []

    if query['from_user']['id'] == query.message.reply_to_message['from_user']['id']:
        for file in files:
            if file['type'] == 'folder':
                folders.append(file)
            else:
                standard_files += "\n- [{file_name}]({file_link})".format(file_name=file['name'],
                                                                          file_link="https://drive.google.com/file/d/"+file['id'])

        query.edit_message_text(text='Archivos:'+standard_files, parse_mode="MARKDOWN", disable_web_page_preview="true", reply_markup=generate_keyboard(folders))
    else:
       print("Mal")

def upload(update, context):
    update.message.reply_text('Please choose:', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('Archivos', callback_data="17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy")]]))
    PARENT = "17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy"

def es_inadecuado(update):
    return update.message.chat.id != GRUPO

updater = Updater(os.environ["telegram_token"], use_context=True)

updater.dispatcher.add_handler(CommandHandler('ls', list_files))
updater.dispatcher.add_handler(CommandHandler('upload', upload))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
