from fastapi import FastAPI
from routers import auth, text
from database.models import router as db_router

app = FastAPI()

#dsffcsxzfcxz
app.include_router(auth.router)
app.include_router(text.router)

app.include_router(db_router)