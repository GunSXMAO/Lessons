from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Получение всех пользователей
@app.get("/users")
def get_users():
    return users

# Добавление нового пользователя
@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='UrbanUser')],
                age: Annotated[int, Path(gt=0, le=120, description="Enter User Age", example=23)]):
    user_id = users[-1].id + 1 if users else 1  # ID = последний ID + 1, если список не пустой
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

# Обновление информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(gt=0, le=1000, description='Enter user ID', example=1)],
                username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='UrbanProfi')],
                age: Annotated[int, Path(gt=0, le=120, description="Enter User Age", example=28)]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE-запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(gt=0, le=1000, description='Enter user ID', example=2)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
