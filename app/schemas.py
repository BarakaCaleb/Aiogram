from pydantic import BaseModel

class ProductRequest(BaseModel):
    artikul: int

class ProductResponse(BaseModel):
    name: str
    artikul: int
    price: float
    rating: float
    total_quantity: int