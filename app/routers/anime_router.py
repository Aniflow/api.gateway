from fastapi import APIRouter, Request

from ..core.services.proxy_service import ProxyService

router = APIRouter()


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def anime_proxy(request: Request):
    response = await ProxyService.proxy_request(request)
    return response
