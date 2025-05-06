import time
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

DB_HOST = 'db_landing'
DB_USER = 'user_name'
DB_PASSWORD = 'user_password'
DB_NAME = 'landing_db'
DB_PORT = 3306

def wait_for_db():
    while True:
        try:
            # Intentamos conectar a la base de datos
            engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
            connection = engine.connect()
            print("Base de datos lista para conectarse!")
            connection.close()
            break
        except OperationalError:
            print("Esperando a que la base de datos esté disponible...")
            time.sleep(5)  # Espera 5 segundos antes de volver a intentar

if __name__ == '__main__':
    wait_for_db()
