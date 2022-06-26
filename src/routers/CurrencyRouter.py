import fastapi

from models.CurrencyConvert import CurrencyConvert
from utils.CurrencyProvider import CurrencyDataAPI

router = fastapi.APIRouter(
    prefix="/currencies",
    tags=["currencies"],
)

@router.get("/list", response_model=dict)
async def get_currencies_list():
    return await CurrencyDataAPI.list()

@router.get("/convert", response_model=CurrencyConvert)
async def get_convert_currency(source: str, destination: str, amount: float, date: str | None = None):
    return await CurrencyDataAPI.convert(source, destination, amount, date)