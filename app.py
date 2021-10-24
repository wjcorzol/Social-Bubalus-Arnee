from flask import Flask, render_template as render, jsonify, request
from db import consulta_acc, consulta_sel

app= Flask(__name__)

# sql = "SELECT * FROM habitacion"
# dat = consulta_sel(sql)
# if len(dat)==0:
#   msg = "No se encontraron tales"
# else:
#   msg = "Se encontraron tales"
# return jsonify({"res":msg, "datos":dat})

@app.route("/", methods=["GET"])
def inicio():
    return render("Login.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render("registro.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render("dashboard.html")

@app.route("/perfilusuario", methods=["GET", "POST"])
def perfilusuario():
    return render("perfil.html")

@app.route("/busqueda", methods=["GET", "POST"])
def busqueda():
    return render("busqueda.html")

@app.route("/detallepost", methods=["GET", "POST"])
def detalle():
    return render("detallepost.html")

@app.route("/perfilusuario/<id_usuario>", methods=["GET", "POST"])
def busqueda_usuario(id_usuario):
    return render("busqueda.html")

@app.route("/feed", methods=["GET"])
def feed():
    return render("feed.html")

@app.route("/prueba")
def prueba():
    sql = "SELECT * FROM tabla_usuario"
    dat = consulta_sel(sql)
    if len(dat)==0:
       msg = "No se encontraron tales"
    else:
       msg = "Se encontraron tales"
    return jsonify({"res":msg, "datos":dat})

if __name__=="__main__":
    app.run(debug=True)