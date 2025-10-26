from pydantic import BaseModel


class CalculationRequest(BaseModel):
    numbers: str


class CalculationResponse(BaseModel):
    result: int
