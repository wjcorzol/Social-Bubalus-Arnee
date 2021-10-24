
import sqlite3

URL_db = 'static/db/socialbubalus.db'

def consulta_sel(query) -> list: 
    "Retorna una lista"
    try:
        with sqlite3.connect(URL_db) as con:
            cursor = con.cursor()
            sal = cursor.execute(query).fetchall()
    except Exception as ex:
        sal = None
    return sal

def consulta_acc(query) -> int: 
    "Retorna un entero"
    try:
        with sqlite3.connect(URL_db) as con:
            cursor = con.cursor()
            sal = cursor.execute(query).rowcount
            if sal != 0:
                con.commit()
    except Exception as ex:
        sal = 0
    return sal