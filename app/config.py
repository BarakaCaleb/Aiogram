import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Bearer token for authorization
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# Telegram bot token
BOT_TOKEN = os.getenv("BOT_TOKEN")


if not all([DATABASE_URL, AUTH_TOKEN, BOT_TOKEN]):
    raise ValueError("Environment variables not properly set in the .env file.")
