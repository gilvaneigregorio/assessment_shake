from fastapi import FastAPI
import uvicorn

from models.dao import user
from core.database import engine

from core import environment
from api import api

user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api.router, prefix='/v1')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=environment.APP_PORT)
