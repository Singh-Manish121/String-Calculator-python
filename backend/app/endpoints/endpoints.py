from fastapi import APIRouter, HTTPException
from ..services.calculator import add
from ..models.models import CalculationRequest, CalculationResponse
# from ..main import app


router = APIRouter()

@router.post("/api/calculate", response_model=CalculationResponse)
def calculate(req: CalculationRequest):
    try:
        result = add(req.numbers)
    except ValueError as e:
        raise HTTPException( status_code=400, detail=str(e))
    return CalculationResponse(result=result)