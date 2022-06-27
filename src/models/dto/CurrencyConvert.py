from pydantic import BaseModel


class CurrencyConvert(BaseModel):
    source: str
    destination: str
    amount_input: float
    amount_output: float
    rate: float
