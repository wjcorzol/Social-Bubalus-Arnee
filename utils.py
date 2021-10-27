import re
from validate_email import validate_email

def email_valido(email) -> bool:
    """ Comprueba que el email se encuentre en el formato correcto """
    return validate_email(email)

def login_valido(login) -> any:
    """ Comprueba que el login cumple con las restricciones establecidas """
    return re.search('^[a-zA-Z0-9_\-.]{5,40}$',login)

def pass_valido(clave) -> any:
    """ Comprueba que la contraseña cumple con las restricciones establecidas al menos una minúscula, una mayúscula y un dígito """
    return re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[^\W]{5,40}',clave)