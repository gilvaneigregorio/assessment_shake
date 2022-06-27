from fastapi import FastAPI
import uvicorn

from models.dao import User
from core.Database import engine

from core import Env
from api import API

User.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(API.router, prefix='/v1')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Env.APP_PORT)
