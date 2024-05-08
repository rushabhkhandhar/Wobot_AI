# authentication.py

from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials

def authenticate_user(username: str, password: str):
 
    users = {"user1": "password1", "user2": "password2"}
    if users.get(username) == password:
        return username
    return None

def get_current_user(credentials: HTTPBasicCredentials):
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user
