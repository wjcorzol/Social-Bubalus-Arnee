from flask import Flask, request, flash, redirect, session, send_file
from flask import render_template as render
from formularios import Login, Registro
from formularios import Spublicacion
from markupsafe import escape
from db import consulta_accion, consulta_selecion
from werkzeug.security import check_password_hash, generate_password_hash
from utils import login_valido, pass_valido, email_valido
import os

#create query from sql db and return result
def consulta(query):
    conexion = consulta_selecion(query)
    return conexion

#create query from insert a new register
def insertar(query,data):
    conexion = consulta_accion(query,data)
    return conexion

# Ejecutar la consulta
sql_i = f"INSERT INTO tabla_usuario(usuario, primerNom, segundoNom, primerApe, segundoApe, email, sexo, nacimiento, clave, celular) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
datos = ["andres", "Willy", "", "Corzo", "Linares", "andres@gmail.com", "M", "1998-01-01", "123s456789", "123s456789", "3041234537"] 
sql = f"SELECT * FROM tabla_usuario"

print(len(consulta(sql)))
insertar(sql_i,datos)
print(len(consulta(sql)))