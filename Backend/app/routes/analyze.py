from fastapi import APIRouter
from app.models.schemas import AnalyzeRequest

router = APIRouter()

@router.post("/analyze")
def analyze(data: AnalyzeRequest):
    return {
        "received_input": data.input,
        "length": len(data.input),
        "message": "Input processed successfully"
    }