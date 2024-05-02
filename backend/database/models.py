from peewee import Model, CharField, IntegerField, FloatField, BooleanField, SqliteDatabase
# from database.models import database
from pydantic import BaseModel
from enum import Enum
from database import db
from fastapi import APIRouter
from playhouse.shortcuts import model_to_dict


router = APIRouter()

database = SqliteDatabase('database/database.db')

class BaseModel(Model):
    def json(self, exclude=['id']) -> dict:
        result = model_to_dict(
            self,
            exclude=[
                User.password,
                User.token
            ]
        )

        for key in exclude:
            result.pop(key, None)

        return result
    
    class Meta:
        database = db


class User(BaseModel):
    username = CharField()
    email = CharField()
    password = CharField()
    admin = BooleanField(default=False)
    token = CharField(null = True)

class Product(BaseModel):
    name = CharField()
    description =CharField()
    price = FloatField()
    count = IntegerField()

@router.on_event('startup')
async def startup():
    database.connect()
    database.create_tables([User, Product], safe = True)

@router.on_event('shutdown')
async def shutdown():
    await database.close()
