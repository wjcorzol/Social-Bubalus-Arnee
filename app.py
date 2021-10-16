from flask import Flask
from flask import render_template as render

app= Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return render("home.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    return render("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    return render("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render("dashboard.html")

@app.route("/perfilusuario", methods=["GET", "POST"])
def perfilusuario():
    return render("perfil.html")

@app.route("/configuracion", methods=["GET", "POST"])
def configuracion():
    return render("configuracion.html")

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

@app.route("/feed/<id_post>", methods=["GET", "POST"])
def detalle_post(id_post):
    return render("detallepost.html")



if __name__=="__main__":
    app.run(debug=True)