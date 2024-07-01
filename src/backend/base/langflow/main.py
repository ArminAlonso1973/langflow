import sys
import uvicorn
import nest_asyncio
from loguru import logger
from fastapi import FastAPI
from langflow.api import router
from langflow.main import setup_app

nest_asyncio.apply()

app = FastAPI()
setup_app(app)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
