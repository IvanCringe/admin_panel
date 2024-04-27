from peewee import Model, CharField, IntegerField, FloatField, BooleanField, SqliteDatabase
# from database.models import database
from pydantic import BaseModel
from enum import Enum
from fastapi import APIRouter


router = APIRouter()

database = SqliteDatabase('database/database.db')

# router = APIRouter()

class Categories(str, Enum):
    Electronics = 'Электроника',
    Clothing = 'Одежда',
    Books = 'Книги',
    Home_Kitchen = 'Дом и кухня',
    Sports_Outdoors = 'Спорт и отдых на природе',
    Beauty_Personal_Care = 'Красота и личная гигиена',
    Toys_Games = 'Игрушки и игры',
    Automotive = 'Автомобильные товары',
    Health_Household = 'Здоровье и быт',
    Tools_Home_Improvement = 'Инструменты и улучшение дома'

class User(Model):
    username = CharField()
    email = CharField()
    password = CharField()
    admin = BooleanField(default=False)
    token = CharField(null = True)
    unhash_password = CharField(null = True)
    class Meta:
        database = database

class BaseModel(Model):
    class Meta:
        database = database

@router.on_event('startup')
async def startup():
    database.connect()
    database.create_tables([User], safe = True)

@router.on_event('shutdown')
async def shutdown():
    await database.close()
