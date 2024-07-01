import os
from fastapi import FastAPI
from langflow.main import setup_app
from pathlib import Path

app = FastAPI()

def setup_app_with_static(app: FastAPI):
    backend_only = os.getenv("BACKEND_ONLY", "false").lower() == "true"
    static_files_dir = Path("static")

    if not backend_only:
        if not static_files_dir.exists():
            raise RuntimeError(f"Static files directory does not exist: {static_files_dir}")
        app.mount("/static", StaticFiles(directory=str(static_files_dir)), name="static")

    setup_app(app)

setup_app_with_static(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
