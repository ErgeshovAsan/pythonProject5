from aiogram import Router, types, F
from bot_config import database
from aiogram.filters import Command
from pprint import pprint

dishes_router = Router()


@dishes_router.message(Command("dishes"))
async def all_dishes(message: types.Message):
    dish_list = database.get_all_dishes()
    pprint(dish_list)
    for dish in dish_list:
        cover = dish['cover']
        txt = f"Название: {dish['name']}\nЦена: {dish['price']}\nОписание: {dish['description']}\nКатегория: {dish['category']}"
        await message.answer_photo(
            photo=cover,
            caption=txt
        )
