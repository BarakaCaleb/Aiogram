from aiogram import Bot, Dispatcher
from app.bot.handlers import router
from app.config import BOT_TOKEN

async def start_scheduler():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)  # Register the router
    await dp.start_polling(bot)
