from aiogram.utils import executor                              #для запуска бота
from create_bot import dp
from data_base import sqlite_db



async def on_startup(_):                                        #для подключения к базе данных и вывода служебной информации
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()

from handlers import client, admin, general

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
general.register_handlers_general(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)       #запуск бота

