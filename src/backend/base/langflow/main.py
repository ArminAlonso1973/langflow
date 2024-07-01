import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from loguru import logger
from langflow.api import router

app = FastAPI()

def setup_app_with_static(app):
    static_files_dir = Path("static")
    if not static_files_dir.exists():
        raise RuntimeError(f"Static files directory does not exist: {static_files_dir}")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    logger.info(f"Setting up app with static files directory {static_files_dir}")

setup_app_with_static(app)

app.include_router(router)

if __name__ == "__main__":
    import nest_asyncio
    import uvicorn
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)
