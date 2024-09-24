from src.models.user_info import UserInfo as UserInfoModel
from src.schemas.user_info import UserInfo 
from jinja2 import Environment, FileSystemLoader

import pandas as pd
import plotly.express as px


# Configurar Jinja2 para renderizar templates
env = Environment(loader=FileSystemLoader('src/templates'))


class UserInfoService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_index(self):
        data = self.db.query(UserInfoModel).all()
        df = pd.DataFrame([(d.nombre, d.edad, d.ciudad, float(d.salario)) for d in data],
                        columns=['Nombre', 'Edad', 'Ciudad', 'Salario'])
        
        # Gráfico de barras (edad vs salario)
        fig_barras = px.bar(df, x='Edad', y='Salario', title='Relación Edad vs Salario')
        barras_html = fig_barras.to_html(full_html=False)

        # Gráfico circular (personas por ciudad)
        fig_pie = px.pie(df, names='Ciudad', title='Personas por Ciudad')
        pie_html = fig_pie.to_html(full_html=False)
        
        # Renderizar plantilla HTML con la tabla y gráficos
        template = env.get_template('index.html')

        return df, barras_html, pie_html, template 
    
    def get_user(self, id):
        result = self.db.query(UserInfoModel).filter(UserInfoModel.id == id).first()
        return result
    
    def create_user(self, userInfo: UserInfo):
        new_user = UserInfoModel(**userInfo.dict())
        self.db.add(new_user)
        self.db.commit()
        return
    
    def update_user(self, id: int, data: UserInfo):
        user = self.db.query(UserInfoModel).filter(UserInfoModel.id == id).first()
        user.nombre = data.nombre
        user.edad = data.edad
        user.ciudad = data.ciudad
        user.salario = data.salario
        self.db.commit()
        return

    
    def delete_user(self, id: int):
        self.db.query(UserInfoModel).filter(UserInfoModel.id == id).delete()
        self.db.commit()
        return