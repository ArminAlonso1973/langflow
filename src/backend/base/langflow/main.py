import sys
import uvicorn
import nest_asyncio
from loguru import logger
from fastapi import FastAPI
from langflow.api import router
from langflow.main import setup_app
from pathlib import Path

nest_asyncio.apply()

app = FastAPI()

static_files_dir = Path("static")

if not static_files_dir.exists():
    logger.error(f"Static files directory does not exist: {static_files_dir}")
else:
    logger.info(f"Static files directory: {static_files_dir}")

setup_app(app)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
