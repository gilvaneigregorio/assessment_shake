import fastapi
from fastapi import Depends
from pydantic import constr, condecimal

from models.dto.currency_convert import CurrencyConvert
from clients import clients
from core.auth import get_current_user

router = fastapi.APIRouter(
    prefix="/currencies",
    tags=["currencies"],
    dependencies=[Depends(get_current_user)]
)


@router.get("/list", response_model=dict)
async def get_currencies_list():
    return await clients.getCurrencyProvider().list()


@router.get("/convert", response_model=CurrencyConvert)
async def get_convert_currency(
    source: constr(min_length=3, max_length=3),
    destination: constr(min_length=3, max_length=3),
    amount: condecimal(ge=0),
    date: str | None = None,
):
    return await clients.getCurrencyProvider().convert(
        source, destination, amount, date
    )
