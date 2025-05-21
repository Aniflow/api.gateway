import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import (API_PORT, API_HOST, ALLOW_ORIGINS,
                     ALLOW_METHODS, ALLOW_CREDENTIALS, ALLOW_HEADERS)
from .routers.proxy_router import router as proxy_router

app = FastAPI(title="Aniflow API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOW_ORIGINS],
    allow_methods=[ALLOW_METHODS],
    allow_headers=[ALLOW_HEADERS],
    allow_credentials=ALLOW_CREDENTIALS,
)

app.include_router(proxy_router)


@app.get("/")
async def root():
    return {"message": "API Gateway is running"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)
