from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboards():
    def __init__(self):
        self.CATEGORIAS = [[[InlineKeyboardButton('Programacion', callback_data='programacion') , InlineKeyboardButton('Seguridad', callback_data='seguridad')],
                            [InlineKeyboardButton('Editores', callback_data='editores'), InlineKeyboardButton('Herramientas', callback_data='herramientas')],
                            [InlineKeyboardButton('Sistemas', callback_data='sistemas'), InlineKeyboardButton('Otros', callback_data='otros')]],
                           [[InlineKeyboardButton('Programacion', callback_data='programacion') , InlineKeyboardButton('Otros', callback_data='otros')],
                           [InlineKeyboardButton('Programacion', callback_data='programacion'), InlineKeyboardButton('Otros', callback_data='otros')],
                           [InlineKeyboardButton('Programacion', callback_data='programacion'), InlineKeyboardButton('Otros', callback_data='otros')]
                          ]]

    def get_main_menu_keyboard(self):
        CATEGORIAS_ACTUALES = self.CATEGORIAS[0].copy()
        CATEGORIAS_ACTUALES.append([InlineKeyboardButton('>', callback_data='>')])
        return InlineKeyboardMarkup(CATEGORIAS_ACTUALES)

    def get_secondary_main_menu_keyboard(self):
        CATEGORIAS_ACTUALES = self.CATEGORIAS[1].copy()
        CATEGORIAS_ACTUALES.append([InlineKeyboardButton('<', callback_data='<')])
        return InlineKeyboardMarkup(CATEGORIAS_ACTUALES)