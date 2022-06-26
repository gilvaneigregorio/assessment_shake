from fastapi import FastAPI
import uvicorn

from utils import Settings
from routers import AuthRouter, CurrencyRouter

app = FastAPI()

app.include_router(AuthRouter.router)
app.include_router(CurrencyRouter.router)


@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=Settings.app_port)

