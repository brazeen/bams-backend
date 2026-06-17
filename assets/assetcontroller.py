from models import Asset, AssetCreate
import supabase
import logging

logger = logging.getLogger(__name__)

async def get_assets_by_user(user_id: str):
    # Fetch assets from the database based on user_id
    response = supabase.table("assets").select("*, entries!inner(*)").eq("entries.userid", user_id).execute()
    if response.status_code == 200:
        assets_data = response.data
        assets = [Asset(**asset) for asset in assets_data]
        return assets
    else:
        logger.error(f"Failed to fetch assets for user {user_id}: {response.error}")
        return []
    
async def add_asset(asset: AssetCreate):
    # Add a new asset to the database
    
    response = supabase.table("assets").insert(asset.model_dump()).execute()
    
    if response.status_code == 201:
        logger.info(f"Asset added successfully")
        return True
    else:
        logger.error(f"Failed to add asset: {response.error}")
        return False
    
async def update_asset(asset_id: int, asset: Asset):
    # Update an existing asset in the database
    
    response = supabase.table("assets").update(asset.model_dump()).eq("id", asset_id).execute()
    
    if response.status_code == 200:
        logger.info(f"Asset with id {asset_id} updated successfully")
        return True
    else:
        logger.error(f"Failed to update asset with id {asset_id}: {response.error}")
        return False
    
