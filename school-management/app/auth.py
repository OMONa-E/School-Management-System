from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt # type: ignore
from datetime import datetime, timedelta
from passlib.context import CryptContext # type: ignore
from sqlalchemy.orm import Session
from app import models, database
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv
from pathlib import Path

# Define absolute path to the .env file - 1 level up
BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / ".env"

# Load the .env file
load_dotenv(ENV_PATH)

# Define key and Algorithm for encoding and decoding JWT
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

# Create a new instance of the CryptContext class for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

#  Create password hash function
def get_password_hash(password):
    return pwd_context.hash(password)

# Verify password hashed password function
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create JWT access token function
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Authenticate user function
def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

# Get current user from token function
def get_current_user(token: str = Depends(auth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user
