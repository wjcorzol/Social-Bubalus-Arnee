import sqlite3

URL_DB = 'socialbubalus.db'

def consulta_selecion(query) -> list:
    try:

        with sqlite3.connect(URL_DB) as con:       # Conectarse a la base de datos
            cursor = con.cursor()                  # Crea un área temporal para manejo
            sal = cursor.execute(query).fetchall() # Ejecutando la consulta y recuperando los resultados
    except Exception as ex:
        sal = None
    return sal

def consulta_accion(query) -> int:
    try:
        
        with sqlite3.connect(URL_DB) as con:       # Conectarse a la base de datos
            cursor = con.cursor()                  # Crea un área temporal para manejo
            sal = cursor.execute(query).rowcount   # Ejecutando la consulta y recuperando los resultados
            if sal!=0:
                con.commit()                       # Asegura los cambios en la base de datos
    except Exception as ex:
        sal = 0
    return sal

