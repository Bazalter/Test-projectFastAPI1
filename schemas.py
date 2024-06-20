from pydantic import BaseModel
from typing import List


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    category_id: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class Category(CategoryBase):
    id: int
    products: List[Product] = []

    class Config:
        orm_mode = True
