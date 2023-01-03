import datetime
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import uuid
from .users.models import User

app = FastAPI()

# define request and response models for the endpoint
class UserRequest(BaseModel):
    username: str
    password: str
    email: str
    first_name: str
    last_name: str

class UserResponse(BaseModel):
    id: uuid
    username: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime

# define the endpoint for creating a new user
@app.post("/users/")
def create_user(user_request: UserRequest):
    # create a new user object with the provided data
    user = User()
    user.CreateAccount(**user_request.dict())
    # if the user object was created successfully, return the user data
    if user:
        return UserResponse(
            id=user.id,
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=user.created_at
        )
    else:
        # if the user object was not created, raise an HTTPException
        raise HTTPException(status_code=400, detail="Invalid user data")
