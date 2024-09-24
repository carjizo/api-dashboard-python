# Dashboard FastAPI con MySQL

Este proyecto utiliza FastAPI para crear un pequeño dashboard que se conecta a una base de datos MySQL, realiza un crud y visualiza datos utilizando Plotly.

## Requisitos

- Python 3.x
- MySQL

## Base de datos 
1. CREATE:
   ```bash
    CREATE TABLE user_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    ciudad VARCHAR(100),
    salario DECIMAL(10, 2)
    );
2. INSERT:
   ```bash
    INSERT INTO 
	user_info (nombre, edad, ciudad, salario)
    VALUES 
        ('Juan Perez', 30, 'Lima', 2500.50),
        ('Maria Garcia', 28, 'Arequipa', 3000.00),
        ('Carlos Ramos', 35, 'Cusco', 3500.75),
        ('Ana Fernandez', 26, 'Trujillo', 2800.00),
        ('Luis Mendoza', 40, 'Piura', 4000.25),
        ('Sofia Torres', 32, 'Chiclayo', 3200.75),
        ('Pedro López', 45, 'Tacna', 4500.50),
        ('Gabriela Vargas', 29, 'Iquitos', 3100.00);
    
    SELECT * FROM user_info ui limit 10;
## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/carjizo/api-dashboard-python.git
   cd dashboard-fastapi
2. Preparar entorno virtual (linux):
   ```bash
   python -m venv env

   source env/bin/activate

   pip install -r requirements.txt
3. Configurar credenciales Mysql en archivo src/config/config.py:
   ```bash
   DATABASE_URL = "mysql+pymysql://user:password@localhost/user_info_db"
4. Ejecutar app:
   ```bash
   uvicorn src.app:app --reload
5. Acceder: http://127.0.0.1:8000/index
## Documentación (enpoints CRUD)
http://127.0.0.1:8000/docs
## Index
![](./imgs/index.png)
## CRUD
![](./imgs/docs.png)