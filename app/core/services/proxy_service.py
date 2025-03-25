from fastapi import Request, Response
import httpx

from ...config import ANIME_SERVICE_URL


class ProxyService:
    """Handles requests that need to be proxied"""

    @staticmethod
    async def proxy_request(request: Request):
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=request.method,
                url=f"{ANIME_SERVICE_URL}{request.url.path}",
                headers=dict(request.headers),
                params=dict(request.query_params),
                content=await request.body()
            )

            return Response(
                content=response.content,  # Return raw content
                status_code=response.status_code,
                headers=dict(response.headers)  # Copy headers properly
            )
