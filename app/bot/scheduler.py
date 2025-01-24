from aiogram import Bot, Dispatcher
from app.bot.handlers import dp

async def start_scheduler():
    bot = Bot(token="YourBotToken")
    await dp.start_polling(bot)