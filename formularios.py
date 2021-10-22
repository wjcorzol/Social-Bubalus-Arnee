from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField, SubmitField, RadioField
from wtforms.fields.core import RadioField
from wtforms.validators import InputRequired, EqualTo
from wtforms.fields.html5 import EmailField, TelField, DateField

class Login(FlaskForm):    # public class Login extends FlaskForm
    usr = TextField('Usuario *',validators= [InputRequired(message='El campo Usuario es requerido')])
    pwd = PasswordField('Clave *',validators= [InputRequired(message='El campo Clave es requerido')])
    btn = SubmitField('Login')

class CClave(FlaskForm):    
    act = PasswordField('Clave actual *',validators= [InputRequired(message='El campo Clave es requerido')])
    nue = PasswordField('Nueva clave *',validators= [InputRequired(message='El campo Nueva Clave es requerido')])
    ver = PasswordField('Verifique clave *',validators= [InputRequired(message='La verificación de Clave es requerido'), EqualTo(nue,message='La nueva clave y su verificación no coinciden')])
    btn = SubmitField('Cambiar')

class Registro(FlaskForm):
    usr = TextField('Usuario *',validators= [InputRequired(message='El campo Usuario es requerido')])
    mail = EmailField('Email *', validators=[InputRequired(message='El campo Correo electrónico es requerido')])
    pnombr = TextField('Primer Nombre *',validators= [InputRequired(message='El campo Primer Nombre es requerido')])
    snombr = TextField('Segundo Nombre')
    priapellido = TextField('Primer Apellido *',validators= [InputRequired(message='El campo Primer Apellido es requerido')])
    segapellido = TextField('Segundo Apellido')
    sexo = RadioField('Sexo *',validators= [InputRequired(message='El campo Sexo es requerido')])
    telefono = TelField('Telefono *',validators= [InputRequired(message='El campo Telefono es requerido')])
    fechanac = DateField('Fecha de Nacimiento *',validators= [InputRequired(message='El campo Fecha de Nacimiento es requerido')])
    cla = PasswordField('Contraseña *',validators= [InputRequired(message='El campo Contraseña es requerido')])
    ver = PasswordField('Verifica la Contraseña *',validators= [InputRequired(message='El campo Verifica la Contraseña es requerido'), EqualTo(nue,message='La nueva clave y su verificación no coinciden')])
    
    btn = SubmitField('Registrarme')
    btn = SubmitField('Cancelar')