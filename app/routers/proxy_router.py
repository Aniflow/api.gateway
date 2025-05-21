from fastapi import APIRouter, Request

from ..core.services.proxy_service import ProxyService
from ..core.decorators.authenticated import authenticated

router = APIRouter()


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
@authenticated
async def catch_all(request: Request):
    return await ProxyService.proxy_request(request)
