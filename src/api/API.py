from fastapi import APIRouter

from api.v1.routers import AuthRouter, CurrencyRouter

'''API implements all avaliable routers'''

router = APIRouter()

router.include_router(AuthRouter.router)
router.include_router(CurrencyRouter.router)