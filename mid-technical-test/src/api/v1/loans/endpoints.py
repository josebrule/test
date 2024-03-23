from fastapi import APIRouter, status, Request

from core.utils.responses import EnvelopeResponse
from .crud import create_loan, delete_loan, get_loan, list_loan, update_loan


router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post(
    "/Create", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def create(request: Request) -> EnvelopeResponse:
    body = await request.json()
    print(body)
    amount = body.get('amount')
    customer_id = body.get('customer_id')
    return create_loan(amount, customer_id)

@router.get(
    "/List", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
def list() -> EnvelopeResponse:
    return EnvelopeResponse(errors=None, body=list_loan())

@router.get(
    "/Retrieve", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def retrive(request: Request) -> any:
    body = await request.json()
    loan_id = body.get('loan_id')
    amount = body.get('amount')
    customer_id = body.get('customer_id')
    if loan_id:
        result = get_loan(loan_id)
    elif amount:
        result = get_loan(amount)
    elif customer_id:
        result = get_loan(customer_id)
    else:
        result = "No existe el usuario"
    return EnvelopeResponse(errors=None, body=result.__json__())

@router.put(
    "/Update", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def update(request: Request) -> EnvelopeResponse:
    body = await request.json()
    loan_id = body.get('loan_id')
    amount = body.get('amount')
    result = update_loan(loan_id, amount)
    return EnvelopeResponse(errors=None, body=result.__json__())

@router.delete(
    "/Delete", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def delete(request: Request) -> EnvelopeResponse:
    body = await request.json()
    loan_id = body.get('loan_id')
    result = delete_loan(loan_id)
    
    return EnvelopeResponse(errors=None, body=result)
