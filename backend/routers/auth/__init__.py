from . import login
from . import reg
from fastapi import APIRouter


router =APIRouter(prefix='/auth')

router.include_router(login.router)
router.include_router(reg.router)