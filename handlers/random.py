from aiogram.filters import Command
from aiogram import Router, types
import random


random_router = Router()

recipes = [
    {
        "image": "images/4_sezona.jpg",
        "caption": "4 сезона:\n1. Приготовить основу.\n2. Добавить соус и начинки для 4 сезонов.\n3. Выпекать 10-15 минут."
    },
    {
        "image": "images/sezar.jpg",
        "caption": "Салат Цезарь:\n1. Сделать тесто для пиццы.\n2. Нарезать листья салата.\n3. Добавить курицу, сыр и сухарики."
                   "\n4. Полить соусом Цезарь.\n5. Выпекать 10-15 минут."
    },
    {
        "image": "images/margarita.jpg",
        "caption": "Маргарита:\n1. Сделать тесто для пиццы.\n2. Намазать томатным соусом.\n3. Добавить сыр моцарелла и помидор.\n4. Выпекать 10-15 минут."
    }
]

@random_router.message(Command('random'))
async def start_handler(message: types.Message):
    pizza_random = random.choice(recipes)
    images = types.FSInputFile(pizza_random["image"])
    await message.answer_photo(photo=images, caption=pizza_random["caption"])