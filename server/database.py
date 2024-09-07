from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL='postgresql://postgres:nilesh123@localhost:5432/fluttermusicapp'

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
db=SessionLocal()