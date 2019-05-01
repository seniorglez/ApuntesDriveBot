from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def generate_keyboard(folders):
    buttons = []
    counter = 0
    length = len(folders)
    iterator = 0
    columns = [[],[]]

    for folder in folders:

        counter += 1
        iterator = 1 if counter % 2 == 0 else 0

        if length % 2 == 0:
            if not columns[1]:
                columns[iterator].append(InlineKeyboardButton(folder['name'], callback_data=folder['id']))
            else:
                buttons.append(columns)
                columns = [[],[]]
            print(columns)
        else:
            if folder == folders[-1]:
                buttons.append([InlineKeyboardButton(folder['name'], callback_data=folder['id'])])
            else:
                if not columns[1]:
                    columns[iterator].append([InlineKeyboardButton(folder['name'], callback_data=folder['id'])])
                else:
                    buttons.append(columns)

    
    buttons.append([InlineKeyboardButton("^", callback_data="17gQDopZVzc--Ivto9pA_U0ybF3DX_oJy")])
    print(buttons)
    return InlineKeyboardMarkup(buttons)