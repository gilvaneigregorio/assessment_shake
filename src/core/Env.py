import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = int(os.getenv('APP_PORT'))
CURRENCY_DATA_API_KEY = os.getenv('CURRENCY_DATA_API_KEY')
DATABASE_URI = os.getenv('DATABASE_URI')
