from aiogram import Bot, Dispatcher
from app.bot.handlers import dp
from app.config import BOT_TOKEN  # Import BOT_TOKEN

async def start_scheduler():
    bot = Bot(token=BOT_TOKEN)  # Use dynamic BOT_TOKEN
    await dp.start_polling(bot)