from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

def setup_app_with_static(app: FastAPI):
    static_files_dir = Path(__file__).parent / "static"
    if not static_files_dir.exists():
        static_files_dir.mkdir(parents=True, exist_ok=True)
    app.mount("/static", StaticFiles(directory=static_files_dir), name="static")

setup_app_with_static(app)
