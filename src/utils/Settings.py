import os
from dotenv import load_dotenv

load_dotenv()

app_port = int(os.getenv('APP_PORT'))
currency_data_api_key = os.getenv('CURRENCY_DATA_API_KEY')