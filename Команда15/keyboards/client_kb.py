from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b1 = KeyboardButton('Поиск работы')
b2 = KeyboardButton('Подать вакансию')
kb_client = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
kb_client.row(b1,b2)