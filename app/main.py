from fastapi import FastAPI
from app.routers import products, bot
from app.database import init_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = FastAPI()

# Initialize database
@app.on_event("startup")
async def startup_event():
    await init_db()

# Include Routers
app.include_router(products.router)

# Scheduler setup
scheduler = AsyncIOScheduler()
scheduler.start()