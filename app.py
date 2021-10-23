from flask import Flask, request
from flask import render_template as render
from formularios import Login
from markupsafe import escape
import os

app= Flask(__name__)

app.secret_key = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def inicio():
    login = Login()
    if request.method == "GET":
        return render("login_copy.html")
    else:
        return render("login_copy.html")

@app.route("/registro/", methods=["GET", "POST"])
def registro():
    return render("registro.html")

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