from fastapi import FastAPI, Path

app = FastAPI()

# Словарь для хранения пользователей
users = {'1': 'Имя: Example, возраст: 18'}

# Получение всех пользователей
@app.get("/users")
def get_users():
    return users

# Добавление нового пользователя
@app.post("/user/{username}/{age}")
def create_user(username: str = Path(gt=3, le=20, description='Enter username', example='UrbanUser'), age: int = Path(gt=1, le=120, description="Enter User Age", example='23')):
    new_id = str(max(map(int, users.keys())) + 1)  # Получаем максимальный ключ и увеличиваем его
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"

# Обновление информации о пользователе
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str = Path(gt=0, le=1000, description='Enter user ID', example='1'),
                username: str = Path(gt=3, le=20, description='Enter username', example='UrbanUser'),
                age: int = Path(gt=1, le=120, description="Enter User Age", example='23')):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    return f"User {user_id} not found"

# Удаление пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    return f"User {user_id} not found"
