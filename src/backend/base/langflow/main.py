import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from loguru import logger

from langflow.api import router as langflow_router

app = FastAPI()

def setup_app_with_static(app: FastAPI) -> None:
    static_files_dir = "static"
    if not os.path.exists(static_files_dir):
        raise RuntimeError(f"Static files directory does not exist: {static_files_dir}")
    
    app.mount("/static", StaticFiles(directory=static_files_dir), name="static")
    logger.info(f"Setting up app with static files directory {static_files_dir}")

setup_app_with_static(app)
app.include_router(langflow_router)

if __name__ == "__main__":
    import nest_asyncio
    import uvicorn

    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=8000)
