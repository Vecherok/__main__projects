#

import telebot
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

token = 'key'

soup1 = BeautifulSoup('<a>...</a>', 'lxml')
print(soup1)

bot = telebot.TeleBot(token)
command_list = {
    '/start' : 'to get the list of commands',
    '/id': 'to get your ID',

}

@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f'<b>Hello, {message.from_user.username}!</b> \nThis Bot can do next list of commands:\n {[i for i in command_list]}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['usd'])
def update_message(message):
    
    html = urlopen ("https://kurs.onliner.by/")
    soup = BeautifulSoup(html)

    tag_list = soup.find_all('p', {'class':'value fall'})

    buy = tag_list[0].text
    sell = tag_list[1].text
    bot.send_message(message.chat.id, 'банк покупает ='+ buy +', банк продает=' + sell)

@bot.message_handler()
def get_user_text(message):
    if message.text.lower() == '/id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')


bot.polling()
