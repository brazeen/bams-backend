from pydantic import BaseModel
from enum import Enum
from decimal import Decimal

class AssetType(str, Enum):
    STOCK = "STOCK",
    ETF = "ETF",
    REIT = "REIT",
    BOND = "BOND",
    CASH = "CASH"

class AssetBase(BaseModel):
    symbol: str
    sector: str = "Others"
    name: str
    current_price: Decimal
    type: AssetType
    expense_ratio: Decimal
    dividend_rate: Decimal # how much is paid per year

class AssetCreate(AssetBase):
    pass

class Asset(AssetBase):
    id: int
    


