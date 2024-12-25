from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

start_router = Router()

@start_router.message(Command("stop"))
@start_router.message(F.text == "стоп")
async def stop_dialog(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Опрос остановлен")

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    id_list = set()
    user_id = message.from_user.id
    id_list.add(user_id)
    counter = len(id_list)
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=
        [
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data='review')
            ],
            [
                types.InlineKeyboardButton(text="Добавить блюдо в меню", callback_data='dish')
            ]
        ]
    )
    await message.answer(f"Привет, {name}, наш бот обслуживает уже {counter} пользователя, для остановки опроса напишите 'стоп'."
                         , reply_markup=kb)

