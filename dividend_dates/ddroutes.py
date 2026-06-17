from fastapi import APIRouter
from fastapi.responses import JSONResponse
from assetcontroller import get_dividend_dates_by_user, add_dividend_date
from models import DividendDateCreate


router = APIRouter(
    prefix="/dd",
    tags=["dividend_dates"],
)


@router.get("/{user_id}")
async def get_user_dividend_dates(user_id: str):
    try:
        dividend_dates = await get_dividend_dates_by_user(user_id)
        return JSONResponse(content=[dd.dict() for dd in dividend_dates], status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.post("/")
async def add_new_dividend_date(dividend_date: DividendDateCreate):
    try:
        success = await add_dividend_date(dividend_date)
        if success:
            return JSONResponse(content={"message": "Dividend date added successfully"}, status_code=201)
        else:
            return JSONResponse(content={"error": "Failed to add dividend date"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
