import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import API_HOST, API_PORT
from .routers.anime_router import router as anime_router

app = FastAPI(title="Aniflow API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(anime_router)


@app.get("/")
async def root():
    return {"message": "API Gateway is running"}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=API_HOST, port=API_PORT, reload=True)
