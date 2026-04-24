from sqlalchemy import Column, Integer, String
from app.db.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index= True)
    name = Column(String)

class Email(Base):
    __tablename__ = "email"
    
    id = Column(Integer, primary_key=True, index=True)  
    email = Column(String)
    subject = Column(String)
    body = Column(String)