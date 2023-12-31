from fastapi import APIRouter, HTTPException

from app.users.dao import UsersDAO
from app.users.schemas import SUserRegister
from app.users.auth import get_password_hash

router = APIRouter(
    prefix='/auth',
    tags=['Auth &  пользователи'],
)

@router.post('/register')
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    print(f'добавлен пользователь {user_data.email}')