from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models import Product

async def get_product_by_artikul(artikul: int, session: AsyncSession):
    result = await session.execute(select(Product).where(Product.artikul == artikul))
    return result.scalars().first()

async def create_or_update_product(data: dict, session: AsyncSession):
    product = await get_product_by_artikul(data["artikul"], session)
    if product:
        for key, value in data.items():
            setattr(product, key, value)
    else:
        product = Product(**data)
        session.add(product)
    await session.commit()