from fastapi import APIRouter

from api.v1.routers import auth_router
from api.v1.routers import currency_router

'''API implements all avaliable routers'''

router = APIRouter()

router.include_router(auth_router.router)
router.include_router(currency_router.router)
