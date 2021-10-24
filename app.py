from flask import Flask, request, flash, redirect, session, send_file
from flask import render_template as render
from formularios import Login, Registro
from markupsafe import escape
from db import consulta_accion, consulta_selecion
from werkzeug.security import check_password_hash, generate_password_hash
from utils import login_valido, pass_valido, email_valido
import os

app= Flask(__name__)

app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
@app.route("/login/", methods=["GET", "POST"])
def inicio():
    login = Login()
    if request.method == "GET":
        return render("login_copy.html",form=login, titulo = "Inicio de Sesión")
    else:
            #recuperar información del formulario
        usuario = escape(request.form['usr'])
        password = escape(request.form['pwd'])
        #Validacion de datos
        if len(usuario.strip()) == 0:
            flash('Campo Usuario es requerido')

        if len(password.strip()) == 0:
            flash('Campo Contraseña es requerido')
        
        # Preparar la consulta 
        sql = f"SELECT usuario, password FROM usuario WHERE usuario='{usuario}'"
        # Ejecutar la consulta
        res = consulta_selecion(sql)
        #tomar decisiones
        if len(res)>0:
            password_usuario = res[0][1]

            if password_usuario == password:
                return render("feed.html")# debe redirecionar a la ruta no mostrar el html desde la ruta login
            else:
                flash('Usuario o clave invalida')
                frm = Login()
                return render('login_copy.html', form = login, titulo = "Inicio de Sesión")


@app.route("/registro/", methods=["GET", "POST"])
def crearUsuario():
    registro = Registro()

    return render("registro_copy.html",form=registro)

@app.route("/dashboard/", methods=["GET", "POST"])
def dashboard():
    return render("dashboard.html")

@app.route("/perfilusuario/", methods=["GET", "POST"])
def perfilusuario():
    return render("perfil.html")

@app.route("/busqueda/", methods=["GET", "POST"])
def busqueda():
    return render("busqueda.html")

@app.route("/detallepost/", methods=["GET", "POST"])
def detalle():
    return render("detallepost.html")

@app.route("/perfilusuario/<id_usuario>/", methods=["GET", "POST"])
def busqueda_usuario(id_usuario):
    return render("busqueda.html")

@app.route("/feed/", methods=["GET"])
def feed():
    return render("feed.html")

if __name__=="__main__":
    app.run(port = 5000, debug = True)