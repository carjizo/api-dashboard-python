from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL

Base = declarative_base()

class UserInfo(Base):

    __tablename__ = "user_info"

    id = Column(Integer, primary_key = True, autoincrement=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    ciudad = Column(String(100))
    salario = Column(DECIMAL(10, 2))