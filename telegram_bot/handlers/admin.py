from aiogram.dispatcher import FSMContext                           #для указания того, что handler используется в машине состояний
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb

ID = None

class FSMAdmin(StatesGroup):
    promo_name = State()
    promo_photo = State()

async def download_rights(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Права доступа подтверждены', reply_markup=admin_kb.button_case_admin)
    await message.delete()

#Начало диалога                  
async def promo_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.promo_name.set()
        await message.reply('Введи название акции')

#Ловим первый ответ и пишем в словарь                                          
async def load_promo_name(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['promo_name'] = message.text
        await FSMAdmin.next()
        await message.reply('Загрузи промо-фото')

#Ловим второй ответ
# @dp.message_handler(state=FSMorder.name)                                           
async def load_promo_photo(message : types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id

        await sqlite_db.sql_add_promo(state)

        await state.finish()

#Выход из состояний
# @dp.message_handler(state='*', commands=['отмена'])
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_promo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('ок')

# @dp.message_handler(commands=['Показать_заказы'])                                           
async def command_show_orders(message : types.Message):
    if message.from_user.id == ID:
        await sqlite_db.sql_read_order(message)

def register_handlers_admin(dp:Dispatcher):

    dp.register_message_handler(promo_start, commands=['Добавить_промо'], state=None)
    dp.register_message_handler(cancel_promo, state="*", commands=['стоп'])
    dp.register_message_handler(cancel_promo, Text(equals='стоп', ignore_case=True), state="*") 
    dp.register_message_handler(load_promo_name, state=FSMAdmin.promo_name)  
    dp.register_message_handler(load_promo_photo, content_types=["photo"], state=FSMAdmin.promo_photo)
    dp.register_message_handler(download_rights, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(command_show_orders, commands=['Показать_заказы'], state=None)