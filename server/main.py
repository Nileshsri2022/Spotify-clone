# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from models.base import Base
from routes import auth
from database import engine

app=FastAPI()

app.include_router(auth.router,prefix='/auth')
# treat as req.body and other as query parameter
Base.metadata.create_all(engine)