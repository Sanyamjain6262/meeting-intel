from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db import SessionDep

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/health/db")
async def health_db(session: SessionDep) -> JSONResponse:
    try:
        await session.execute(text("SELECT 1"))
    # A refused connection surfaces as OSError, not as a SQLAlchemy error.
    except (SQLAlchemyError, OSError):
        return JSONResponse(
            {"status": "unavailable"}, status_code=status.HTTP_503_SERVICE_UNAVAILABLE
        )
    return JSONResponse({"status": "ok"})
