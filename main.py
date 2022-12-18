from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


import config
import sqlite3
import random

connect = sqlite3.connect('users.db')
cur = connect.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS users(
    username VARCHAR(255),
    id INTEGER,
    created DATE
    );
    """)
connect.commit()

connect_admin = sqlite3.connect('admin.db')
curr  = connect_admin.cursor()
curr.execute("""CREATE TABLE IF NOT EXISTS admin(
    id INTEGER
    );
    """)
connect_admin.commit()

bot = Bot(config.token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start', 'go'])
async def start(message : types.Message):
    cur = connect.cursor()
    cur.execute(f'SELECT id FROM users WHERE id == {message.from_user.id};')
    result = cur.fetchall()
    if result == []:
        cur.execute(f"INSERT INTO users VALUES ('{message.from_user.username}', {message.from_user.id}, '2022-12-10');")
        connect.commit()
    await message.answer(f"Здраствуйте {message.from_user.full_name}!\nДобро пожаловать в наш бот!\nВведите комманду /help - чтобы узнать что может делать этот бот {result}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Я могу вам предложить игру << Рандомное число >>\nПравила игры:\n1) Я угадываю число от 1 до 3 вы должны его отгадать\n2) Не писать текст <<Эчтеке чыкпайт>>\nМои Комманды:\n/start - Запустить бота.\n/help - Помощь.\n/startplay - Начать игру.\n/users - Пользователи")
@dp.message_handler(commands=['users'])
async def get_users(message: types.Message):
    cur = connect.cursor()
    cur.execute("SELECT * FROM users;")
    res = cur.fetchall()
    if res != []:
        await message.answer(res)
    else:
        await message.answer("Список пуст")
        
@dp.message_handler(commands=['startplay'])
async def startplay(message: types.Message):
    await message.answer("Ты в игре. Я загадаю число от 1 до 3, Попробуй отгадать ? : ")

@dp.message_handler(text=['1','2','3',])
async def hello(message: types.Message):
    user = int(message.text)
    randomer = random.randint(1, 3)
    if user == randomer:
        await message.answer(f"Вы угадали! Моё число: {randomer}")
        
    elif user != randomer:
        await message.answer(f"Вы  не угадали! Моё число: {randomer} ")

    
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Помощь")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

executor.start_polling(dp)