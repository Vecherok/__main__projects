from aiogram import types, Dispatcher                           #types- для записи аннотации типов в функциях
import json
import string 
from create_bot import dp

#@dp.message_handler()                                                      #декоратор для функции, которая принимает сообщения от пользователей
#async def echo_send(message : types.Message):                              #функция для обработки сообщений от пользователя
    # if message.text.strip().lower() == "привет":                                                           #await - ждёт свободного места в потоке для выполнения команды
    # await message.answer('И тебе привет')                                 #простой ответ
    # await message.reply(message.text)                                     #ответ с цитированием входящего сообщения
    # await bot.send_message(message.from_user.id, message.text)            #ответ в личку


# @dp.message_handler()                                           
async def censor(message : types.Message):
    input_string = {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}
    cens_words = set(json.load(open('censorship.json')))
    if input_string.intersection(cens_words) != set():
        await message.reply('Маты запрещены!')
        await message.delete()

def register_handlers_general(dp: Dispatcher):
    dp.register_message_handler(censor)