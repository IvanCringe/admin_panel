from datetime import datetime, timezone
from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse
from database.models import User
import bcrypt
import jwt
from config.config import SECRET_KEY


router = APIRouter()

@router.post('/login')
async def login(username: str, password: str, response: Response):
    try:
        user = User.get(User.username == username)
        user_payload = {'name': user.username,
                        'email': user.email,
                        'password': user.password,
                        'admin': user.admin}
        token = jwt.encode(user_payload, SECRET_KEY, algorithm='HS256')
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            response.set_cookie(key="token", value=token)
            user = User.get(User.username == username)
            user.token = token
            user.save()
            return {"message": f"Login successful: token - {token}"}
        else:
            raise HTTPException(status_code=401, detail="Incorrect password")
    except User.DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")
