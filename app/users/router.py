from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.exception import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
# from app.users.dependencies import get_current_admin_user
from app.users.models import Users
from app.users.schemas import SUserAuth
from app.users.auth import get_password_hash, verif_pasword, authenticate_user, create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['Auth &  пользователи'],
)

@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)
    print(f'добавлен пользователь {user_data.email}')


@router.post('/login')
async def register_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token

@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return f'user has been logout'

@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user

# @router.get("/all")
# async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
#     return await UsersDAO.find_all()