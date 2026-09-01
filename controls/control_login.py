from database import db_core

def login_principal(email_ingresado, password_ingresada):
    datos = db_core.datos_login()
    
    # Validaciones de campos vacíos
    if not email_ingresado:
        return False, "email", "Campo Obligatorio"
    if not password_ingresada:
        return False, "password", "Campo Obligatorio"
        
    # Lógica de un solo usuario (usando el primer registro de la base de datos)
    correo_db = datos[0][3]
    password_db = datos[0][4]
    
    if email_ingresado != correo_db:
        return False, "email", "Usuario Incorrecto"
        
    if password_ingresada != password_db:
        return False, "password", "Contraseña Incorrecta"
        
    # Si el correo y la contraseña coinciden
    return True, "exito", ""