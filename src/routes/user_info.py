from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

from src.config.database import Session
from src.services.user_info import UserInfoService
from src.models.user_info import UserInfo as UserInfoModel
from src.schemas.user_info import UserInfo

user_info_router = APIRouter()


# Ruta para obtener datos desde la base de datos existente
@user_info_router.get("/index", tags=['dashboard'], response_class=HTMLResponse)
def index() -> HTMLResponse:
    db = Session()
    df, barras_html, pie_html, template  = UserInfoService(db).get_index()
    return template.render(table=df.to_html(classes='data'), barras_html=barras_html, pie_html=pie_html)

@user_info_router.post('/user', tags=['user'], response_model=dict, status_code=201)
def create_user(userInfo: UserInfo) -> dict:
    db = Session()
    UserInfoService(db).create_user(userInfo)
    return JSONResponse(status_code=201, content={"message": "Usuario registrado"})


@user_info_router.delete('/user/{id}', tags=['user'], response_model=dict, status_code=200)
def delete_user(id: int)-> dict:
    db = Session()
    result: UserInfoModel = db.query(UserInfoModel).filter(UserInfoModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Usuario no encontró"})
    UserInfoService(db).delete_user(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el usuario"})


@user_info_router.put('/user/{id}', tags=['user'], response_model=dict, status_code=200)
def update_user(id: int, userInfo: UserInfo)-> dict:
    db = Session()
    result = UserInfoService(db).get_user(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Usuario no encontrado"})
    
    UserInfoService(db).update_user(id, userInfo)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el usuario"})