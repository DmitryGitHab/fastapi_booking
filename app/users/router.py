from fastapi import APIRouter

from app.users.schemas import SUserRegister

router = APIRouter(
    prefix='/auth',
    tags=['Auth &  пользователи'],
)

@router.post('/register')
async def register_user(user_data: SUserRegister):
    pass
    # existing_user =