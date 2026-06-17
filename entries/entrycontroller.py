import logging
from models import Entry, EntryCreate
import supabase

logger = logging.getLogger(__name__)


    
async def get_entries_by_user(user_id: str):
    # Fetch entries from the database based on user_id
    response = supabase.table("entries").select("*").eq("userid", user_id).execute()
    
    if response.status_code == 200:
        entries_data = response.data
        entries = [Entry(**entry) for entry in entries_data]
        return entries
    else:
        logger.error(f"Failed to fetch entries for user {user_id}: {response.error}")
        return []

async def add_entry(entry: EntryCreate):
    # Add a new entry to the database
    response = supabase.table("entries").insert(entry.model_dump()).execute()
    
    if response.status_code == 201:
        logger.info(f"Entry added successfully")
        return True
    else:
        logger.error(f"Failed to add entry: {response.error}")
        return False
    
async def update_entry(entry_id: int, entry: Entry):
    # Update an existing entry in the database
    response = supabase.table("entries").update(entry.model_dump()).eq("id", entry_id).execute()
    
    if response.status_code == 200:
        logger.info(f"Entry with id {entry_id} updated successfully")
        return True
    else:
        logger.error(f"Failed to update entry with id {entry_id}: {response.error}")
        return False
    
async def delete_entry(entry_id: int):
    # Delete an entry from the database
    response = supabase.table("entries").delete().eq("id", entry_id).execute()
    
    if response.status_code == 200:
        logger.info(f"Entry with id {entry_id} deleted successfully")
        return True
    else:
        logger.error(f"Failed to delete entry with id {entry_id}: {response.error}")
        return False