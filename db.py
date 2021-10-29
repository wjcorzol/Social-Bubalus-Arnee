import sqlite3

URL_DB = 'static/db/socialbubalus.db'

def consulta_selecion(query) -> list:
    try:

        with sqlite3.connect(URL_DB) as con:       # Conectarse a la base de datos
            cursor = con.cursor()                  # Crea un área temporal para manejo
            sal = cursor.execute(query).fetchall() # Ejecutando la consulta y recuperando los resultados
            print(sal)
    except Exception as ex:
        sal = ""
        print(ex)
    return sal

def consulta_selecion_rowcount(query) -> list:
    try:

        with sqlite3.connect(URL_DB) as con:       # Conectarse a la base de datos
            cursor = con.cursor()                  # Crea un área temporal para manejo
            sal = cursor.execute(query).rowcount() # Ejecutando la consulta y recuperando los resultados
            print(sal)
    except Exception as ex:
        sal = 0
        print(ex)
    return sal

def consulta_accion(query, datos) -> int:
    try:

        with sqlite3.connect(URL_DB) as con:       # Conectarse a la base de datos
            cursor = con.cursor()                  # Crea un área temporal para manejo
            sal = cursor.execute(query, datos).rowcount   # Ejecutando la consulta y recuperando los resultados
            if sal!=0:
                con.commit()                       # Asegura los cambios en la base de datos
            print(sal)
    except Exception as ex:
        sal = 0
        print(ex)
    return sal

