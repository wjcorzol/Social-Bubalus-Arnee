from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField, SubmitField, RadioField
from wtforms.fields.core import RadioField
from wtforms.validators import InputRequired, EqualTo
from wtforms.fields.html5 import EmailField, TelField, DateField

class Login(FlaskForm):
    usr = TextField('Usuario *', render_kw={"placeholder": "Usuario"})
    pwd = PasswordField('Clave *', render_kw={"placeholder": "Contraseña"})
    btnLogin = SubmitField('Login')
    

class CClave(FlaskForm):    
    act = PasswordField('Clave actual *',validators= [InputRequired(message='El campo Clave es requerido')])
    nue = PasswordField('Nueva clave *',validators= [InputRequired(message='El campo Nueva Clave es requerido')])
    ver = PasswordField('Verifique clave *',validators= [InputRequired(message='La verificación de Clave es requerido'), EqualTo(nue,message='La nueva clave y su verificación no coinciden')])
    btn = SubmitField('Cambiar')

class Registro(FlaskForm):
    usr = TextField('Usuario', render_kw={"placeholder": "Usuario"}, validators= [InputRequired(message='El campo Usuario es requerido')])
    mail = EmailField('Email', render_kw={"placeholder": "E-mail"}, validators=[InputRequired(message='El campo Correo electrónico es requerido')])
    pnombr = TextField('Primer Nombre', render_kw={"placeholder": "Primer Nombre"},validators= [InputRequired(message='El campo Primer Nombre es requerido')])
    snombr = TextField('Segundo Nombre', render_kw={"placeholder": "Segundo Nombre"})
    priapellido = TextField('Primer Apellido', render_kw={"placeholder": "Primer Apellido"},validators= [InputRequired(message='El campo Primer Apellido es requerido')])
    segapellido = TextField('Segundo Apellido', render_kw={"placeholder": "Segundo Apellido"})
    sexo = RadioField('Sexo',validators= [InputRequired(message='El campo Sexo es requerido')], choices=[('M', 'M'),('F', 'F'),('O', 'Otro')])
    telefono = TelField('Telefono *', render_kw={"placeholder": "Telefono"},validators= [InputRequired(message='El campo Telefono es requerido')])
    fechanac = DateField('Fecha de Nacimiento',validators= [InputRequired(message='El campo Fecha de Nacimiento es requerido')], format ='%d-%m-%Y')
    cla = PasswordField('Contraseña *', render_kw={"placeholder": "Contraseña"},validators= [InputRequired(message='El campo Contraseña es requerido')])
    ver = PasswordField('Verifica la Contraseña *', render_kw={"placeholder": "Verifica Contraseña"},validators= [InputRequired(message='El campo Verifica la Contraseña es requerido'), EqualTo(cla,message='La nueva clave y su verificación no coinciden')])
    
    btnRegistro = SubmitField('Registrarme')
    