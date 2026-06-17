from fastapi import APIRouter
from fastapi.responses import JSONResponse
from assetcontroller import get_assets_by_user, add_asset, update_asset
from models import Asset, AssetCreate


router = APIRouter(
    prefix="/assets",
    tags=["assets"],
)


@router.get("/{user_id}")
async def get_user_assets(user_id: str):
    try:
        assets = await get_assets_by_user(user_id)
        return JSONResponse(content=[asset.dict() for asset in assets], status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.post("/")
async def add_new_asset(asset: AssetCreate):
    try:
        success = await add_asset(asset)
        if success:
            return JSONResponse(content={"message": "Asset added successfully"}, status_code=201)
        else:
            return JSONResponse(content={"error": "Failed to add asset"}, status_code=400)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.put("/{asset_id}")
async def update_existing_asset(asset_id: int, asset: Asset):
    try:
        success = await update_asset(asset_id, asset)
        if success:
            return JSONResponse(content={"message": "Asset updated successfully"}, status_code=200)
        else:
            return JSONResponse(content={"error": "Failed to update asset"}, status_code=400)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
        