from functools import wraps
from fastapi import Request, HTTPException
from ..auth.auth_handler import verify_jwt


def authenticated(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        try:
            verify_jwt(request)

        except HTTPException as e:
            raise HTTPException(
                status_code=e.status_code,
                detail=e.detail,
                headers=getattr(e, "headers", None)
            )

        except Exception:
            raise HTTPException(
                status_code=500,
                detail="Internal server error during authentication"
            )

        return await func(request, *args, **kwargs)

    return wrapper
