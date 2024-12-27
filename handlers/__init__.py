from aiogram import Router, F
from .start import start_router
from .review_dialog import review_router
from .myinfo import myinfo_router
from .random import random_router
from .dishes import dishes_router
from .menu_of_dishes import dish_router

private_router = Router()


private_router.include_router(start_router)
private_router.include_router(review_router)
private_router.include_router(myinfo_router)
private_router.include_router(random_router)
private_router.include_router(dish_router)
private_router.include_router(dishes_router)

private_router.message.filter(F.chat.type == "private")
private_router.callback_query.filter(F.chat.type == "private")