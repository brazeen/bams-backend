from models import DividendDate, DividendDateCreate
import supabase
import logging

logger = logging.getLogger(__name__)

async def get_dividend_dates_by_user(user_id: str):
    try:
        # Get dividend dates from the database based on user_id
        response = await supabase.table("dividend_dates").select("dividend_dates.id, dividend_dates.ex_date, dividend_dates.pay_date, entries!inner(userid)").eq("entries.userid", user_id).execute()
        if response.status_code == 200:
            dividend_dates_data = response.data
            dividend_dates = [DividendDate(**dd) for dd in dividend_dates_data]
            return dividend_dates
    except Exception as e:
        logger.error(f"Error occurred while fetching dividend dates for user {user_id}: {e}")
        raise

async def add_dividend_date(dividend_date: DividendDateCreate):
    try:
        # Add a new dividend date to the database
        response = await supabase.table("dividend_dates").insert(dividend_date.model_dump()).execute()
        if response.status_code == 201:
            logger.info(f"Dividend date added successfully")
            return True
        else:
            logger.error(f"Failed to add dividend date: {response.error}")
            return False
    except Exception as e:
        logger.error(f"Error occurred while adding dividend date: {e}")
        raise