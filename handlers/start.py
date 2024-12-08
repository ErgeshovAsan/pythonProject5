from aiogram.filters import Command
from aiogram import Router, types

start_router = Router()

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    id = set()
    user_id = message.from_user.id
    id.add(user_id)
    counter = len(id)
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}, наш бот обслуживает уже {counter} пользователя")