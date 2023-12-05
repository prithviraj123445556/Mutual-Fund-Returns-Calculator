from pydantic import BaseModel

class NetProfitResponse(BaseModel):
    net_profit: float

class ErrorBase(BaseModel):
    error: str





