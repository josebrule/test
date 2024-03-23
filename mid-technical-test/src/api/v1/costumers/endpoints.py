from fastapi import APIRouter, status, Request

from core.utils.responses import EnvelopeResponse
from .crud import create_user, delete_user_by_email, delete_user_by_name, get_user, get_user_by_email, get_user_by_name, list_users, update_user, delete_user

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.post(
    "/Create", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def create(request: Request) -> EnvelopeResponse:
    body = await request.json()
    print(body)
    full_name = body.get('full_name')
    email = body.get('email')
    return create_user(full_name, email)

@router.get(
    "/List", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
def list() -> EnvelopeResponse:
    return EnvelopeResponse(errors=None, body=list_users())

@router.get(
    "/Retrieve", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def retrive(request: Request) -> any:
    body = await request.json()
    id_user = body.get('id')
    full_name = body.get('full_name')
    email = body.get('email')
    if id_user:
        result = get_user(id_user)
    elif full_name:
        result = get_user_by_name(full_name)
    elif email:
        result = get_user_by_email(email)
    else:
        result = "No existe el usuario"
    return EnvelopeResponse(errors=None, body=result.__json__())

@router.put(
    "/Update", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def update(request: Request) -> EnvelopeResponse:
    body = await request.json()
    id_user = body.get('id')
    full_name = body.get('full_name')
    email = body.get('email')
    result = update_user(id_user, full_name, email)
    return EnvelopeResponse(errors=None, body=result.__json__())

@router.delete(
    "/Delete", status_code=status.HTTP_200_OK, summary="Health check service", response_model=EnvelopeResponse
)
async def delete(request: Request) -> EnvelopeResponse:
    body = await request.json()
    id_user = body.get('id')
    full_name = body.get('full_name')
    email = body.get('email')
    if id_user:
        result = delete_user(id_user)
    elif full_name:
        result = delete_user_by_name(full_name)
    elif email:
        result = delete_user_by_email(email)
    else:
        result = "No existe el usuario"
    
    return EnvelopeResponse(errors=None, body=result)