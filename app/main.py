from fastapi import FastAPI
from app.routers import products, subscribe
from app.database import init_db
from app.bot.scheduler import start_scheduler

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
    await start_scheduler()

app.include_router(products.router)
app.include_router(subscribe.router)