from pydantic import BaseModel, Field
from typing import Optional


class UserInfo(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(max_length=100)
    edad: int = Field(le=140)
    ciudad: str = Field(max_length=100)
    salario: float = Field(le=100000)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Juan Perez",
                "edad": 30,
                "ciudad": "Lima",
                "salario": 2500.50
            }
        }