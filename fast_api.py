from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from models import User, Gender, Role, UserUpdateRequest
from typing import List

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("589d957c-2652-4582-9711-0ff5c997e52f"),
        first_name="Vineel",
        last_name="Vempati",
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=UUID("3ace2454-cc2a-49b4-9e47-b26b17d7a3d2"),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        print(f"user_id type {type(user_id)}")
        print(f"User ID: {user.id}, Type: {type(user.id)}")
        print(f"If uuid.id:{user.id}==user_id:{user_id}")
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(status_code=404, detail=f"The user ID {user_id} is not present")


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                print(f"First name not null: {user_update.first_name}")
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                print(f"Last name not null: {user_update.last_name}")
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                print(f"Middle name not null: {user_update.middle_name}")
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                print(f"Roles not null: {user_update.roles}")
                user.roles = user_update.roles
            return
    raise HTTPException(status_code=404, detail=f"The user ID {user_id} is not present")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fast_api:app", host="localhost", port=8000, reload=True)
