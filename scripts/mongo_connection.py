import os
from dotenv import load_dotenv
from bson import ObjectId
from pymongo import MongoClient

load_dotenv()  # Cargar variables del archivo .env
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

# Generamos un cliente con las credenciales de conexión del .env
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]  # Seleccionamos la base de datos


def test_connection():
    """
    Prueba la conexión a la base de datos.
    """
    try:
        client.admin.command("ping")
        print("Conexión exitosa a la base de datos MongoDB")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")


def read_data(collection_name: str, filtro: dict = None):
    """
    Lee documentos de una colección de MongoDB.
    - collection_name: nombre de la colección
    - filtro: diccionario opcional para filtrar resultados (default: todos)

    Retorna una lista de documentos.
    """
    try:
        collection = db[collection_name]

        if filtro is None:
            filtro = {}

        documentos = list(collection.find(filtro))

        # Convertir ObjectId a str para evitar problemas al serializar
        for doc in documentos:
            if "_id" in doc and isinstance(doc["_id"], ObjectId):
                doc["_id"] = str(doc["_id"])

        return documentos

    except Exception as e:
        print(f"Error leyendo datos de MongoDB ({collection_name}): {e}")
        return []


def insert_data(collection_name: str, data: dict):
    """
    Inserta un documento en una colección dada.
    Retorna el ID del documento insertado.
    """
    try:
        collection = db[collection_name]
        resultado = collection.insert_one(data)
        print(
            f"Documento insertado en '{collection_name}' con ID: {resultado.inserted_id}"
        )
        return resultado.inserted_id
    except Exception as e:
        print(f"Error insertando documento en MongoDB: {e}")
        return None


if __name__ == "__main__":
    test_connection()
