from fastapi import Request, Response
import httpx
from starlette.responses import JSONResponse
from ...config import SERVICE_ROUTES


class ProxyService:
    @staticmethod
    async def proxy_request(request: Request) -> Response:
        path = request.url.path
        method = request.method
        body = await request.body()
        headers = dict(request.headers)

        for prefix, target_url in SERVICE_ROUTES.items():
            if path.startswith(prefix):
                url = f"{target_url}{path}"
                async with httpx.AsyncClient() as client:
                    try:
                        resp = await client.request(
                            method,
                            url,
                            headers=headers,
                            content=body,
                            params=request.query_params
                        )

                        return Response(
                            content=resp.content,
                            status_code=resp.status_code,
                            headers=resp.headers
                        )

                    except httpx.RequestError as e:
                        return JSONResponse(
                            status_code=502,
                            content={
                                "error": f"Upstream error: {str(e)}"
                            }
                        )

        return JSONResponse(
            status_code=404,
            content={"error": "Route not found"}
        )
