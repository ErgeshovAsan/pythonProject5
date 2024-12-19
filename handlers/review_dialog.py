from aiogram import Router, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from bot_config import database

review_router = Router()
reviewed_users = set()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()
    process_data = State()

def get_rating_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=" 1", callback_data="1"),
                InlineKeyboardButton(text=" 2", callback_data="2"),
                InlineKeyboardButton(text=" 3", callback_data="3"),
                InlineKeyboardButton(text=" 4", callback_data="4"),
                InlineKeyboardButton(text=" 5", callback_data="5"),
            ]
        ]
    )

@review_router.callback_query(F.data == "review")
async def feedback_start(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    if user_id in reviewed_users:
        await callback.message.answer("Вы уже оставляли отзыв. Нельзя оставлять отзыв более одного раза.")
        await state.clear()
        return

    reviewed_users.add(user_id)
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)

@review_router.message(RestourantReview.name)
async def process_contact(message: types.Message, state: FSMContext):
    if len(message.text) < 3:
        await message.answer("Пожалуйста, напишите имя больше 4 символьов")
        return
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона?")
    await state.set_state(RestourantReview.phone_number)

@review_router.message(RestourantReview.phone_number)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer("Как оцениваете качество еды?", reply_markup=get_rating_keyboard())
    await state.set_state(RestourantReview.food_rating)

@review_router.callback_query(RestourantReview.food_rating)
async def process_cleanliness_rating(callback: types.CallbackQuery, state: FSMContext):
    # if message.text not in ["1", "2", "3", "4", "5"]:
    #     await message.answer("Пожалуйста, напишите оценку от 1 до 5.")
    #     return
    rating = int(callback.data)
    await callback.message.edit_text(f"Спасибо за вашу оценку: {rating}")
    await state.update_data(food_rating=callback.data)
    await callback.message.answer("Как оцениваете чистоту заведения?", reply_markup=get_rating_keyboard())
    await state.set_state(RestourantReview.cleanliness_rating)

@review_router.callback_query(RestourantReview.cleanliness_rating)
async def process_extra_comments(callback: types.CallbackQuery, state: FSMContext):
    # if message.text not in ["1", "2", "3", "4", "5"]:
    #     await message.answer("Пожалуйста, напишите оценку от 1 до 5.")
    #     return
    rating = int(callback.data)
    await callback.message.edit_text(f"Спасибо за вашу оценку: {rating}")
    await state.update_data(cleanliness_rating=callback.data)
    await callback.message.answer("Дополнительные комментарии/жалоба?")
    await state.set_state(RestourantReview.extra_comments)

@review_router.message(RestourantReview.extra_comments)
async def process_data(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("Дата посещения?")
    await state.set_state(RestourantReview.process_data)

@review_router.message(RestourantReview.process_data)
async def process_clear(message: types.Message, state: FSMContext):
    await state.update_data(process_data=message.text)
    await message.answer("Спасибо за отзыв")
    data = await state.get_data()
    print(data)
    database.save_review(data)
    await state.clear()