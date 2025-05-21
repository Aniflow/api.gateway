import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CONFIG
from .routers.proxy_router import router as proxy_router

app = FastAPI(title="Aniflow API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.ALLOW_ORIGINS],
    allow_methods=[CONFIG.ALLOW_METHODS],
    allow_headers=[CONFIG.ALLOW_HEADERS],
    allow_credentials=CONFIG.ALLOW_CREDENTIALS,
)

app.include_router(proxy_router)


@app.get("/")
async def root():
    return {"message": "API Gateway is running"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        st=CONFIG.API_HOST,
        port=CONFIG.API_PORT,
        reload=True
    )
