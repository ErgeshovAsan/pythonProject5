import asyncio
from bot_config import bot, dp, database
from handlers import private_router
from handlers.group_management import group_router


async def on_startup(bot):
    database.create_tables()

async def main():
    dp.include_router(private_router)
    dp.include_router(group_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
