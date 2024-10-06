from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton



main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Digital Lab')],
    [KeyboardButton(text='1121a')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='О боте')]],
        resize_keyboard=True, 
        input_field_placeholder='Выберите пункт меню...')

contacs = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Заведующий', callback_data='vlad')],
    [InlineKeyboardButton(text='Тех.поддержка', callback_data='tex')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]], resize_keyboard=True, input_field_placeholder='Выберите пункт в меню...')

back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Вернуться назад')]], resize_keyboard=True, input_field_placeholder='В меню есть кнопка возврата...')