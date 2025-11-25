import json
from mongo_connection import read_data

OPENMETEO = "openmeteo"
METEOSOURCE = "meteosource"


def leer_openmeteo(filtro: dict = None):
    """
    Lee datos de la colección 'openmeteo' en MongoDB.
    - filtro: diccionario opcional para filtrar resultados (default: todos)

    Retorna una lista de documentos.
    """
    return read_data(OPENMETEO, filtro)


def leer_meteosource(filtro: dict = None):
    """
    Lee datos de la colección 'meteosource' en MongoDB.
    - filtro: diccionario opcional para filtrar resultados (default: todos)

    Retorna una lista de documentos.
    """
    return read_data(METEOSOURCE, filtro)


def leer_todo():
    """
    Lee datos de ambas colecciones en MongoDB.
    Retorna un diccionario con listas de documentos.
    """
    datos_openmeteo = leer_openmeteo()
    print(f"======== DOCUMENTOS EN 'OPENMETEO': {len(datos_openmeteo)} ========")
    if len(datos_openmeteo) > 0:
        for i, doc in enumerate(datos_openmeteo):
            print(f"==== DOCUMENTO {i+1} ({doc['timestamp_captura']}) ====")
            print(json.dumps(doc, indent=2, ensure_ascii=False))

    datos_meteosource = leer_meteosource()
    print(f"======== DOCUMENTOS EN 'METEOSOURCE': {len(datos_meteosource)} ========")
    if len(datos_meteosource) > 0:
        for i, doc in enumerate(datos_meteosource):
            print(f"==== DOCUMENTO {i+1} ({doc['timestamp_captura']}) ====")
            print(json.dumps(doc, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    # Prueba de lectura de datos
    leer_todo()
