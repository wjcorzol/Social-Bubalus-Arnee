from flask import Flask, request, flash, redirect, session, send_file
from flask import render_template as render
from formularios import Login, Registro
from formularios import Spublicacion
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
        sql = f"SELECT usuario, clave, primerNom, segundoNombre, primerApe, segundoApe, email, sexo, nacimiento, celular FROM tabla_usuario WHERE usuario='{usuario}'"
        # Ejecutar la consulta
        res = consulta_selecion(sql)
        #tomar decisiones
        
        if len(res)>0:  
            password_db = res[0][1]

            if check_password_hash(password_db,password):
                session.clear()
                session['usr_id'] = res[0][0]
                session['pwd_id'] = password
                session['nombre'] = res[0][2]
                session['segundoNombre'] = res[0][3]
                session['apellido'] = res[0][4]
                session['segundoApellido'] = res[0][5]
                session['email'] = res[0][6]
                session['sexo'] = res[0][7]
                session['nacimiento'] = res[0][8]
                session['celular'] = res[0][9] 
                return redirect('/feed/')
            else:
                flash('Usuario o clave invalida')
                frm = Login()
                return render('login_copy.html', form = login, titulo = "Inicio de Sesión")

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')


@app.route("/registro/", methods=["GET", "POST"])
def crearUsuario():
    registro = Registro()

    if request.method == 'GET':
        return render("registro_copy.html",form=registro, titulo = 'Registro')
    else:
        #recuperar información del formulario
        usuario = escape(request.form['usr']).strip()
        primerNombre = escape(request.form['pnombr'])
        primerApellido = escape(request.form['priapellido'])
        sexo = escape(request.form['sexo'])
        telefono = escape(request.form['telefono'])
        password = escape(request.form['cla']).strip()
        email = escape(request.form['mail'])
        segundoNombre = escape(request.form['snombr'])
        segundoApellido = escape(request.form['segapellido'])
        pais = escape(request.form['pais'])
        fechaNacimiento = escape(request.form['fechanac'])
        verificacionClave = escape(request.form['ver']).strip()
                #Validacion de datos
        if len(usuario.strip()) == 0:
            flash('Campo Usuario es requerido')

        if len(password.strip()) == 0:
            flash('Campo Contraseña es requerido')
        
        if password != verificacionClave:
            flash('Las contraseñas no coinciden')

        # Preparar la consulta 
        sql = f"INSERT INTO tabla_usuario(usuario, primerNom, segundoNom, primerApe, segundoApe, email, sexo, nacimiento, clave, celular) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # Ejecutar la consulta
        password = generate_password_hash(password)
        res = consulta_accion(sql, (usuario, primerNombre, segundoNombre, primerApellido, segundoNombre, email, sexo, fechaNacimiento, password,  telefono ))
        # Procesar la respuesta
        if res!=0:
            flash('Datos han sido exitosamente grabados')
        else:
            flash('Por favor reintente')        
        return redirect('/feed/')

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

@app.route("/feed/", methods=["GET","POST"])
def subirpublicacion():
    publica = Spublicacion()
    if request.method == 'GET':
        return render("feed.html",form = publica, titulo = 'Feed')
    else:
        #recuperar información del formulario
        usuario = session['usr_id']
        fecha = escape(request.form[''])
        descripcion = escape(request.form['descripcion'])
        multimedia = escape(request.form['imagen'])
                #Validacion de datos
        if len(usuario.strip()) == 0:
            flash('Campo Usuario es requerido')

        if len(fecha.strip()) == 0:
            flash('Campo Contraseña es requerido')

        # Preparar la consulta 
        sql = f"INSERT INTO tabla_publicaciones(usuario, fecha, descripcion, multimedia) VALUES (?, ?, ?, ?)"
        # Ejecutar la consulta
        res = consulta_accion(sql, (usuario, fecha, descripcion, multimedia))
        # Procesar la respuesta
        if res!=0:
            flash('Publicacion creada.')
        else:
            flash('Por favor reintente')        
        return redirect('/feed/')

if __name__=="__main__":
    app.run(port = 5000, debug = True)