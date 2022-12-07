from aiogram import Bot, Dispatcher, executor, types
import config 

import random

bot = Bot(config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'go'])
async def start(message : types.Message):
    # with open('users.txt', 'r', encoding='utf-8') as read_user:
    #     res = read_user.readlines()
    #     users = []
    #     if res != []:
    #         for i in res:
    #             username = i.split()
    #             if username not in users:
    #                 users.append(username)
    #                 if username in users:
    #                     with open('users.txt', 'a+', encoding='utf-8') as user:
    #                         user.write(f'{message.from_user.username} {message.from_user.id} {time.ctime()}\n')
    #     else:
    #         with open('users.txt', 'a+', encoding='utf-8') as users:
    #             users.write(f"{message.from_user.username} {message.from_user.id} {time.ctime()}\n")
    await message.answer(f"Здраствуйте {message.from_user.full_name}!\nДобро пожаловать в наш бот!\nВведите комманду /help - чтобы узнать что может делать этот бот",reply_markup = nav.mainMenu)
        
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Я могу вам предложить игру << Рандомное число >>\nПравила игры:\n1) Я угадываю число от 1 до 3 вы должны его отгадать\n2) Не писать текст <<Эчтеке чыкпайт>>\nМои Комманды:\n/start - Запустить бота.\n/help - Помощь.\n/startplay - Начать игру")

@dp.message_handler(commands=['startplay'])
async def startplay(message: types.Message):
    await message.answer("Ты в игре. Я загадаю число от 1 до 3, Попробуй отгадать ? : ")

@dp.message_handler(text=["1","2","3",])
async def hello(message: types.Message):
    user = int(message.text)
    randomer = random.randint(1, 3)
    if user == randomer:
        await message.reply(f"Вы угадали! Моё число: {randomer}")
        
    elif user != randomer:
        await message.reply(f"Вы  не угадали! Моё число: {randomer} ")

    
# @dp.message_handler(content_types=['text'])
# async def other(message: types.Message):
#     if message.text =='🔻Рандомное число':
#         await message.answer(f".{message.from_user},'Угадайте', {random.randint(1,3)}")
        
#     elif message.text == '🔵Другое':
        
#         await message.answer(f"{message.from_user}, '🔵Другое',reply_markups = nav.otherMenu")
        

    
    
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Помощь")

@dp.message_handler(text = "Привет")
async def hello(message: types.Message):
    await message.answer("Привет")

# @dp.message_handler(commands=['play'])
# async def play(message:types.Message):
#     await message.answer("Я загадал число от 1 до 3")
# random_number = random.randint(1,3)
# users = int(input("Угадай число: "))
# if users == random_number:
#     print("Вы угадали! ")
# else:
#     print("Вы проиграли")
              
    
# @dp.message_handler()
# async def not_foun(message: types.Message):
#     await message.reply("Я вас не понял введите /help")
    

executor.start_polling(dp)