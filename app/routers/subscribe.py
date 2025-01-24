from fastapi import APIRouter, Depends
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal
from app.utils import fetch_product_data

router = APIRouter(prefix="/api/v1/subscribe", tags=["subscribe"])
scheduler = AsyncIOScheduler()

async def get_session():
    async with SessionLocal() as session:
        yield session

@router.get("/{artikul}")
async def subscribe_product(artikul: int, session: AsyncSession = Depends(get_session)):
    async def periodic_task():
        product_data = await fetch_product_data(artikul)
        await create_or_update_product(product_data, session)

    scheduler.add_job(periodic_task, "interval", minutes=30, id=str(artikul), replace_existing=True)
    return {"message": "Subscription started."}