from aiogram import Router, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

review_router = Router()
reviewed_users = set()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

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
    await message.answer("Ваш номер телефона?")
    await state.set_state(RestourantReview.phone_number)

@review_router.message(RestourantReview.phone_number)
async def process_food_rating(message: types.Message, state: FSMContext):
    await message.answer("Как оцениваете качество еды?")
    await state.set_state(RestourantReview.food_rating)

@review_router.message(RestourantReview.food_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, напишите оценку от 1 до 5.")
        return
    await message.answer("Как оцениваете чистоту заведения?")
    await state.set_state(RestourantReview.cleanliness_rating)

@review_router.message(RestourantReview.cleanliness_rating)
async def process_extra_comments(message: types.Message, state: FSMContext):
    if message.text not in ["1", "2", "3", "4", "5"]:
        await message.answer("Пожалуйста, напишите оценку от 1 до 5.")
        return
    await message.answer("Дополнительные комментарии/жалоба?")
    await state.set_state(RestourantReview.extra_comments)

@review_router.message(RestourantReview.extra_comments)
async def process_clear(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за отзыв")
    await state.clear()