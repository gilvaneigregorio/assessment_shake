import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = int(os.getenv('APP_PORT'))
CURRENCY_DATA_API_KEY = os.getenv('CURRENCY_DATA_API_KEY')
API_LOGIN_ENDPOINT = os.getenv('API_LOGIN_ENDPOINT')

DATABASE_URI = os.getenv('DATABASE_URI')
DATABASE_URI_ASYNC = os.getenv('DATABASE_URI_ASYNC')


JWT_SECRET = os.getenv('JWT_SECRET')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES')