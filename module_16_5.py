from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Инициализация Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Получение всех пользователей в шаблоне
@app.get("/", response_class=HTMLResponse)
def show_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": None})

# Получение информации о пользователе в шаблоне
@app.get("/user/{user_id}", response_class=HTMLResponse)
def show_user(request: Request, user_id: Annotated[int, Path(gt=0, le=1000)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "users": [], "user": user})
    raise HTTPException(status_code=404, detail="User was not found")

# Добавление нового пользователя
@app.post("/user/{username}/{age}")
def create_user(username: Annotated[str, Path(min_length=3, max_length=20)],
                age: Annotated[int, Path(gt=0, le=120)]):
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

# Обновление информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[int, Path(gt=0, le=1000)],
                username: Annotated[str, Path(min_length=3, max_length=20)],
                age: Annotated[int, Path(gt=0, le=120)]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# Удаление пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(gt=0, le=1000)]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

