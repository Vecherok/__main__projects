#два режима LongPolling(для тестирования) & Webhook(для деплоя на сервер)

from aiogram import Bot                                         
from aiogram.dispatcher import Dispatcher                       #для улавливания всех команд отправленных пользователями

import os                                                        #для чтения токена из среды окружения
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

token = os.getenv("token")                                      #забираем токен 
bot = Bot(token)                                                #инициализация бота
dp = Dispatcher(bot, storage=storage)                                            #инициализация диспетчера

