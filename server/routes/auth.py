import uuid
import bcrypt
from fastapi import APIRouter, HTTPException
from database import db
from models.user import User
from pydantic_schemas.user_create import UserCreate


router=APIRouter()
@router.post('/signup')
def signup_user(user:UserCreate):
  user_db=db.query(User).filter(User.email==user.email).first()
  if user_db:
    raise HTTPException(400,'User already exists')

  hashed_pw=bcrypt.hashpw(user.password.encode(),bcrypt.gensalt())
  user_db=User(id=str(uuid.uuid4()),email=user.email,password=hashed_pw,name=user.name)
  db.add(user_db)
  db.commit()
  db.refresh(user_db)
  return user_db