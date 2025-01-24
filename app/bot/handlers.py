from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal
from app.crud import get_product_by_artikul
from app.config import BOT_TOKEN  # Import BOT_TOKEN from the config module

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Define keyboard
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Get product data"))

# /start command handler
@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Welcome! Use the button below to get product data.", reply_markup=keyboard)

# Handler for "Get product data" button
@dp.message_handler(lambda message: message.text == "Get product data")
async def get_product_data_handler(message: types.Message):
    await message.answer("Please provide the product article number:")

# Handler for receiving article numbers
@dp.message_handler(lambda message: message.text.isdigit())
async def fetch_product_data_handler(message: types.Message):
    artikul = int(message.text)
    async with SessionLocal() as session:
        product = await get_product_by_artikul(artikul, session)
        if not product:
            await message.answer("Product not found in the database.")
            return
        response = (
            f"Product Name: {product.name}\n"
            f"Artikul: {product.artikul}\n"
            f"Price: {product.price} RUB\n"
            f"Rating: {product.rating}\n"
            f"Total Quantity: {product.total_quantity}\n"
        )
        await message.answer(response)
