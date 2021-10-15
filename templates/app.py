from flask import Flask

app= Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return "Pagina de inicio"

@app.route("/registro", methods=["GET", "POST"])
def registro():
    return "Pagina de registro"

@app.route("/login", methods=["GET", "POST"])
def login():
    return "Pagina de login"

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return "Pagina de dashboard administrativo"

@app.route("/busqueda/<id_usuario>", methods=["GET"])
def busqueda_usuario(id_usuario):
    return f"Estás viendo el perfil de {id_usuario}"

@app.route("/feed", methods=["GET"])
def feed():
    return "Pagina del feed"

@app.route("/post/<id_post>", methods=["GET", "POST"])
def detalle_post(id_post):
    return f"Estás viendo el detalle del post {id_post}"

@app.route("/perfilusuario", methods=["GET", "POST"])
def perfilusuario():
    return "Pagina de perfil del usuario"

if __name__=="__main__":
    app.run(debug=True)

