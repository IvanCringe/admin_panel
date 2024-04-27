from fastapi import APIRouter, Request, HTTPException
from database.models import User


router = APIRouter()

@router.get('/')
async def test(request: Request):
    try:
        user_token = request.cookies.get('token')
        user = User.get(user_token == User.token)
        return {'msg': f'{user.username}, {user.password}'}
    except:
        raise HTTPException(status_code=400, detail="Зарегистрируся")