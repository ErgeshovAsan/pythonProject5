from aiogram import Router, F, types
from datetime import timedelta


group_router = Router()
group_router.message.filter(F.chat.type != "private")

bad_words = ("персик", "мандарин")

@group_router.message()
async def check_bad_words_handler(message: types.Message):
    # await message.answer(f"Привет, {message.from_user.first_name}")
    for word in bad_words:
        if word in message.text:
            # await message.delete()
            autor = message.from_user.id
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=autor
            )
            break

@group_router.message(F.text == "бан 1д")
async def ban_date(message: types.Message):
    if message.reply_to_message:
        user = await message.reply_to_message.from_user
        await message.chat.ban(
            user_id=user.id,
            until_date=timedelta(days=1)
        )

@group_router.message(F.text == "бан 3ч")
async def ban_date(message: types.Message):
    if message.reply_to_message:
        user = await message.reply_to_message.from_user
        await message.chat.ban(
            user_id=user.id,
            until_date=timedelta(hours=3)
        )

@group_router.message(F.text == "бан 3н")
async def ban_date(message: types.Message):
    if message.reply_to_message:
        user = await message.reply_to_message.from_user
        await message.chat.ban(
            user_id=user.id,
            until_date=timedelta(weeks=3)
        )

@group_router.message(F.text == "бан 3м")
async def ban_date(message: types.Message):
    if message.reply_to_message:
        user = await message.reply_to_message.from_user
        await message.chat.ban(
            user_id=user.id,
            until_date=timedelta(minutes=3)
        )