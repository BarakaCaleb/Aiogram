from aiogram import Bot, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command  # Import the Command filter for Aiogram 3.x
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal
from app.crud import get_product_by_artikul
from app.config import BOT_TOKEN

# Initialize bot and router
bot = Bot(token=BOT_TOKEN)
router = Router()

# Define keyboard
keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Get product data")]],
    resize_keyboard=True
)

# /start command handler
@router.message(Command(commands=["start"]))  # Use Command filter
async def start_handler(message: Message):
    await message.answer("Welcome! Use the button below to get product data.", reply_markup=keyboard)

# Handler for "Get product data" button
@router.message(lambda message: message.text == "Get product data")
async def get_product_data_handler(message: Message):
    await message.answer("Please provide the product article number:")

# Handler for receiving article numbers
@router.message(lambda message: message.text.isdigit())
async def fetch_product_data_handler(message: Message):
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
