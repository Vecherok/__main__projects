#два типа кнопок: 1.кнопки клавиатуры , 2.инлайн кнопки

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, WebAppInfo

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Сделать_заказ')
b3 = KeyboardButton('/Ассортимент товаров')
b4 = KeyboardButton('/Поделиться номером', request_contact=True)
# b5 = KeyboardButton('/Перейти на сайт', web_app=WebAppInfo('https://new-garden.by/'))

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)                   #для замещения обычной клавиатуры
#one_time_keyboard=True    -  для сворачивания клавиатуры


# kb_client.add(b1).add(b2).insert(b3)
kb_client.add(b3).row(b1,b2,b4)