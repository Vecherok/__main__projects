#5512356002:AAGYON50uo3s2tqCkTzCfcZHNi3slFAQBC4

import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '5512356002:AAGYON50uo3s2tqCkTzCfcZHNi3slFAQBC4'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)



# print(openai.Model.list())
@dp.message_handler()
async def send(message : types.Message):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
    stop=["You:"]
    )

    await message.answer(response['choices'][0]['text'])

    executor.start_polling(dp, skip_updates=True)

