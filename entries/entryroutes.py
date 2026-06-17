from fastapi import APIRouter
from fastapi.responses import JSONResponse
from assetcontroller import get_entries_by_user, add_entry, update_entry, delete_entry
from models import Entry, EntryCreate


router = APIRouter(
    prefix="/entries",
    tags=["entries"],
)


@router.get("/{user_id}")
async def get_user_entries(user_id: str):
    try:
        entries = await get_entries_by_user(user_id)
        return JSONResponse(content=[entry.dict() for entry in entries], status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.post("/")
async def add_new_entry(entry: EntryCreate):
    try:
        success = await add_entry(entry)
        if success:
            return JSONResponse(content={"message": "Entry added successfully"}, status_code=201)
        else:
            return JSONResponse(content={"error": "Failed to add entry"}, status_code=400)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.put("/{entry_id}")
async def update_existing_entry(entry_id: int, entry: Entry):
    try:
        success = await update_entry(entry_id, entry)
        if success:
            return JSONResponse(content={"message": "Entry updated successfully"}, status_code=200)
        else:
            return JSONResponse(content={"error": "Failed to update entry"}, status_code=400)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@router.delete("/{entry_id}")
async def delete_existing_entry(entry_id: int):
    try:
        success = await delete_entry(entry_id)
        if success:
            return JSONResponse(content={"message": "Entry deleted successfully"}, status_code=200)
        else:
            return JSONResponse(content={"error": "Failed to delete entry"}, status_code=400)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)