from aiogram.filters import Command
from aiogram import Router, types


myinfo_router = Router()

@myinfo_router.message(Command('myinfo'))
async def start_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f"Ваш id: {id}, имя: {name}, фамилия: {username}")