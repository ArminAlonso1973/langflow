import nest_asyncio
from fastapi import FastAPI, Request, Response
from loguru import logger
from langflow.api import router

nest_asyncio.apply()

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
