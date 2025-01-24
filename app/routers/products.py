from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal
from app.schemas import ProductRequest
from app.crud import create_or_update_product
from app.utils import fetch_product_data

router = APIRouter(prefix="/api/v1/products", tags=["products"])

async def get_session():
    async with SessionLocal() as session:
        yield session

@router.post("/")
async def post_product(product: ProductRequest, session: AsyncSession = Depends(get_session)):
    product_data = await fetch_product_data(product.artikul)
    await create_or_update_product(product_data, session)
    return {"message": "Product data successfully stored."}