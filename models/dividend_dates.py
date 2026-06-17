from pydantic import BaseModel, AwareDatetime

class DividendDateBase(BaseModel):
    assetid: int
    ex_date: AwareDatetime
    pay_date: AwareDatetime

class DividendDateCreate(DividendDateBase):
    pass

class DividendDate(DividendDateBase):
    id: int