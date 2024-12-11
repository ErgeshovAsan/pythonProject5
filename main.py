import asyncio
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router
from handlers.review_dialog import review_router
from bot_config import bot, dp



async def main():
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
