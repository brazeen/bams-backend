from pydantic import BaseModel, AwareDatetime
from decimal import Decimal

class EntryBase(BaseModel):
    assetid: int
    userid: int
    currency: str
    price: Decimal
    quantity: Decimal
    purchased_at: AwareDatetime

class EntryCreate(EntryBase):
    pass

class Entry(EntryBase):
    id: int
    


