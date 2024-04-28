from fastapi import APIRouter, Response
from database.models import Product
from datetime import datetime


router =APIRouter()

@router.post('/')
async def add_product(name: str, 
                      description: str, 
                      price: float,
                      count: int,
                      response: Response):
    response = Product.select() 