import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

# Generamos un cliente con las credenciales de conexión del .env
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]  # Seleccionamos la base de datos

def test_connection():
    try:
        client.admin.command('ping')
        print("Conexión exitosa a la base de datos MongoDB")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    test_connection()