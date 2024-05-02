from fastapi import APIRouter
from database.models import User
import bcrypt


router = APIRouter()

@router.post('/')
async def reg_user(username:str, email:str, password:str):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    user = User.create(username=username, email=email, password=hashed)
    return user.password