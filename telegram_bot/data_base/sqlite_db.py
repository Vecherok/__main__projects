import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('newgarden.db')
    cur = base.cursor()
    if base:
        print('**Data base connected successfully**')
    

async def sql_add_order(state):
    async with state.proxy() as data:
        base.execute('CREATE TABLE IF NOT EXISTS orders(product TEXT, name TEXT PRIMARY KEY, contact TEXT, details TEXT)')
        #что делать с primary key ????????
        base.commit()
        
        cur.execute('INSERT INTO orders VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_add_promo(state):
    async with state.proxy() as data:
        base.execute('CREATE TABLE IF NOT EXISTS promo(promo_name TEXT PRIMARY KEY, promo_photo TEXT)')
        base.commit()
        
        cur.execute('INSERT INTO promo VALUES (?, ?)', tuple(data.values()))
        base.commit()


async def sql_read_order(message):
    for ret in cur.execute('SELECT * FROM orders').fetchall():
        await bot.send_message(message.from_user.id, f'Позиция: {ret[0]}\nИмя: {ret[1]}\nКонтакт: {ret[2]}\nДоп.инфо: {ret[3]}\n')