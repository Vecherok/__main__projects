from aiogram import types, Dispatcher                       #types- для записи аннотации типов в функциях
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

from aiogram.dispatcher import FSMContext                           #для указания того, что handler используется в машине состояний
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db


# @dp.message_handler(commands=['start', 'help'])                                           
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, "New Garden приветствует вас.\nЯ помогу вам оформить заказ.", reply_markup=kb_client)
    except:
        await message.reply('New Garden приветствует вас.\nЯ БОТ и я помогу вам оформить заказ.\nНапишите мне в ЛС: https://t.me/VecherokBot_bot')
        await message.delete()

# @dp.message_handler(commands=['Режим_работы'])                                           
async def command_working_hours(message : types.Message):
    mess = "Мы открыты 25 часов в сутки\\7 дней в неделю для Вас.\n''Сон для слабаков.'' ©"
    try:
        await bot.send_message(message.from_user.id, mess)
    except:
        await message.reply(mess)
        await message.delete()


# @dp.message_handler(commands=['Сделать_заказ'])                                           
async def command_make_order(message : types.Message):
    mess = "Оформить заказ Вы можете так-то ..."
    try:
        await bot.send_message(message.from_user.id, mess) #reply_markup=ReplyKeyboardRemove() удаление клавиатуры
    except:
        await message.reply(mess)
        await message.delete()

#____________________make order________________________________

class FSMorder(StatesGroup):
    product = State()
    name = State()
    contact = State()
    details = State()

#Начало диалога
# @dp.message_handler(commands=['Заказ'], state=None)                                           
async def start_order(message : types.Message):
    await FSMorder.product.set()
    await message.reply('Напишите что бы Вы хотели купить')


#Ловим первый ответ и пишем в словарь
# @dp.message_handler(state=FSMorder.product)                                           
async def load_product(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['product'] = message.text
    await FSMorder.next()
    await message.reply('Как к Вам обращаться?')

#Ловим второй ответ
# @dp.message_handler(state=FSMorder.name)                                           
async def load_name(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMorder.next()
    await message.reply('Ваш контактный номер телефона: ')

#Ловим третий ответ
# @dp.message_handler(state=FSMorder.contact)                                           
async def load_contact(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text
    await FSMorder.next()
    await message.reply('Укажите дополнительную информацию к заказу: ')

#Ловим последний ответ и используем полученные данные
# @dp.message_handler(state=FSMorder.details)                                           
async def load_delails(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
        data['details'] = message.text
    
    # async with state.proxy() as data:
    #     await message.reply(str(data))
    await sqlite_db.sql_add_order(state)

    await state.finish()

#Выход из состояний
# @dp.message_handler(state='*', commands=['отмена'])
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_order(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Очень жаль, что вы отменили заказ!\nДля повторного оформления заказа нажмите "Заказ"')


    
#регистрация хэндлеров
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_working_hours, commands=['Режим_работы'])
    # dp.register_message_handler(command_make_order, commands=['Сделать_заказ'])

    dp.register_message_handler(start_order, commands=['Сделать_заказ'], state=None)
    dp.register_message_handler(cancel_order, state="*", commands=['отмена'])
    dp.register_message_handler(cancel_order, Text(equals='отмена', ignore_case=True), state="*") 
    dp.register_message_handler(load_product, state=FSMorder.product)
    dp.register_message_handler(load_name, state=FSMorder.name)
    dp.register_message_handler(load_contact, state=FSMorder.contact)
    dp.register_message_handler(load_delails, state=FSMorder.details)                  
