from fastapi import FastAPI
from app.routers import products, bot
from app.database import init_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = FastAPI()

# Initializing  database
@app.on_event("startup")
async def startup_event():
    await init_db()

# Include Routers
app.include_router(products.router)


scheduler = AsyncIOScheduler()
scheduler.start()