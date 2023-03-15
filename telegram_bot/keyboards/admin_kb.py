from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


button_load = KeyboardButton('/Добавить_промо')
button_delete = KeyboardButton('/Удалить_промо')
button_show_orders = KeyboardButton('/Показать_заказы')

button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_show_orders).row(button_load, button_delete)