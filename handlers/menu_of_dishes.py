from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot_config import database


dish_router = Router()
dish_router.message.filter(F.from_user.id == 1377166423)
dish_router.callback_query.filter(F.from_user.id == 1377166423)

class MenuDishes(StatesGroup):
    name = State()
    price = State()
    description = State()
    category = State()

@dish_router.callback_query(F.data == "dish")
async def feedback_start(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Название блюда?")
    await state.set_state(MenuDishes.name)

@dish_router.message(MenuDishes.name)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Цена?")
    await state.set_state(MenuDishes.price)

@dish_router.message(MenuDishes.price)
async def process_description(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Описание?")
    await state.set_state(MenuDishes.description)

@dish_router.message(MenuDishes.description)
async def process_category(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=
        [
            [
                types.KeyboardButton(text="Пицца 3(дм)"),
                types.KeyboardButton(text="Пицца 4(дм)")
            ],
            [
                types.KeyboardButton(text="Горячие напитки"),
                types.KeyboardButton(text="Холодные напитки")
            ]
        ]
    )
    await state.update_data(description=message.text)
    await message.answer("Категория?", reply_markup=kb)
    await state.set_state(MenuDishes.category)

@dish_router.message(MenuDishes.category)
async def process_clear(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer("Блюдо сохранено")
    data = await state.get_data()
    print(data)
    database.save_dish(data)
    await state.clear()