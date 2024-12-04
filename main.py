from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio
from dotenv import dotenv_values
import random

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_handler(message: types.Message):
    id = set()
    user_id = message.from_user.id
    id.add(user_id)
    counter = len(id)
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}, наш бот обслуживает уже {counter} пользователя")

@dp.message(Command('myinfo'))
async def start_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Ваш id: {id}, имя: {name}, фамилия: {username}")

@dp.message(Command('random'))
async def start_handler(message: types.Message):
    name = ("Саша", "Маша", "Даша", "Наташа")
    name_random = random.choice(name)
    await message.answer(name_random)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
