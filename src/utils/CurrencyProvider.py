from abc import ABC, abstractmethod
from abc import ABCMeta
from fastapi import HTTPException
import httpx

from utils import Settings
from models.CurrencyConvert import CurrencyConvert

class CurrencyProvider(ABC):
    @staticmethod
    @abstractmethod
    def list() -> list[str]:
        pass

    @staticmethod
    @abstractmethod
    def convert(source: str, destination: str, amount: float, date: str) -> CurrencyConvert:
        pass

class CurrencyDataAPI(CurrencyProvider):
    url_base = "https://api.apilayer.com/currency_data"
    headers= {"apikey": Settings.currency_data_api_key}

    async def list() -> list[str]:
        async with httpx.AsyncClient() as client:
            url = f'{CurrencyDataAPI.url_base}/list'
            response = await client.get(url, headers=CurrencyDataAPI.headers)

            result = response.json()

            request_success = result['success']
            CurrencyDataAPI.handle_request_errors(response.status_code, request_success, request_success)

            return result['currencies']


    async def convert(source: str, destination: str, amount: float, date: str) -> CurrencyConvert:
        async with httpx.AsyncClient() as client:
            url = f'{CurrencyDataAPI.url_base}/convert?from={source}&to={destination}&amount={amount}'
            if date:
                url = f'{url}&date={date}'

            response = await client.get(url, headers=CurrencyDataAPI.headers)
            result = response.json()

            is_success = result['success']
            CurrencyDataAPI.handle_request_errors(response.status_code, is_success, result)

            return CurrencyConvert (
                source = result['query']['from'],
                destination = result['query']['to'],
                amount_input = result['query']['amount'],
                amount_output = result['result'],
                rate = result['info']['quote']
            )

    def handle_request_errors(status_code: int, is_success: bool, request: dict):
        status_code_family = int(status_code % 100)

        if is_success is False:
            if request['error']['code'] == 401:
                raise HTTPException(status_code = 400, detail =  "You have entered an invalid \"source\" property. [Example: source=EUR]")
            if request['error']['code'] == 402:
                raise HTTPException(status_code = 400, detail =  "You have entered an invalid \"destination\" property. [Example: destination=EUR]")
            if request['error']['code'] == 302:
                raise HTTPException(status_code = 400, detail =  "You have entered an invalid date. [Required format: date=YYYY-MM-DD]")

            raise HTTPException(status_code = 400, detail =  "Bad Request, The request was unacceptable")

        if status_code == 429:
            # 429 - Too many requests	API request limit exceeded. See section Rate Limiting for more info.
            raise HTTPException(status_code = 429, detail =  "Too many requests, API request limit exceeded")

        if status_code in (400, 401, 404):
            # 400 - Bad Request	The request was unacceptable, often due to missing a required parameter.
            # 401 - Unauthorized	No valid API key provided.
            # 404 - Not Found	The requested resource doesn't exist.
            raise HTTPException(status_code = 400, detail =  "Bad Request, The request was unacceptable")
        
        if status_code_family == 5:
            # 5xx - Server Error	We have failed to process your request. (You can contact us anytime)
            raise HTTPException(status_code = 500, detail =  "BServer Error, We have failed to process your request")
