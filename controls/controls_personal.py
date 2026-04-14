import flet as ft 
import re
from database import personal_db, db_core
from components import *

def limpiar_formulario():
    from views import personal_view
    #reestablece los datos del formulario
    personal_view.nombres_personal.value=""
    personal_view.apellidos_personal.value=""
    personal_view.cedula_personal.value=""
    personal_view.numero_telefono_personal.value=""
    personal_view.correo_personal.value=""
    personal_view.text_correo.color=ft.Colors.BLACK
    personal_view.correo_personal.color=ft.Colors.BLACK
    personal_view.correo_personal.read_only=False
    personal_view.provincias.value=""
    personal_view.ciudades.value=""
    personal_view.direccion_personal.value=""
    personal_view.check_box_correo.value=True
    
    personal_view.nombres_personal.error=None
    personal_view.apellidos_personal.error=None
    personal_view.cedula_personal.error=None
    personal_view.numero_telefono_personal.error=None
    personal_view.correo_personal.error=None
    personal_view.provincias.error_text=None
    personal_view.ciudades.error_text=None
   
    personal_view.foto_integrante.content=estado_incial_foto()
    
    personal_view.ruta_anterior=None
    personal_view.nueva_ruta=None

def validacion_general():
    from views import personal_view
    validacion=True
    nombres_personal=personal_view.nombres_personal.value.strip()
    apellidos_personal= personal_view.apellidos_personal.value.strip()
    
    if not nombres_personal:
        personal_view.nombres_personal.error="Campo Obligatorio"
        personal_view.nombres_personal.value=""
        validacion=False
    elif nombres_personal.isdigit():
        personal_view.nombres_personal.error="Ingrese un valor correcto"
        validacion=False
    else:
        personal_view.nombres_personal.error=None
        
    if not apellidos_personal:
        personal_view.apellidos_personal.error="Campo Obligatorio"
        personal_view.apellidos_personal.value=""
        validacion=False
    elif apellidos_personal.isdigit():
        personal_view.apellidos_personal.error="Ingrese un valor correcto"
        validacion=False
    else:
        personal_view.apellidos_personal.error=None
        
    if not personal_view.cedula_personal.value:
        personal_view.cedula_personal.error="Campo Obligatorio"
        validacion=False
    elif not personal_view.cedula_personal.value.isdigit():
        personal_view.cedula_personal.error="Solo se Permite Ingresar Números"
        validacion=False
    elif len(personal_view.cedula_personal.value)!= 10:
        personal_view.cedula_personal.error="Ingrese 10 Dígitos"
        validacion=False
    else:
        personal_view.cedula_personal.error=None
    
    if not personal_view.numero_telefono_personal.value:
        personal_view.numero_telefono_personal.error="Campo Obligatorio"
        validacion=False
    elif not personal_view.numero_telefono_personal.value.isdigit():
        personal_view.numero_telefono_personal.error="Solo se Permite Ingresar Números"
        validacion=False
    elif len(personal_view.numero_telefono_personal.value)!= 10:
        personal_view.numero_telefono_personal.error="Ingrese 10 Dígitos"
        validacion=False
    else:
        personal_view.numero_telefono_personal.error=None
    
    patron_correo=r'^[\w\.-]+@[\w\.-]+\.\w+$'  
    
    if personal_view.check_box_correo.value:
        if not personal_view.correo_personal.value:
            personal_view.correo_personal.error="Campo Obligatorio"
            validacion=False
        elif not re.match(patron_correo, personal_view.correo_personal.value):
            personal_view.correo_personal.error="Formato Invalido"
            validacion=False
        else:
            personal_view.correo_personal.error=None

    if not personal_view.provincias.value:
        personal_view.provincias.error_text="Campo Obligatorio"
        validacion=False
    else: 
        personal_view.provincias.error_text=None
    
    if not personal_view.ciudades.value:
        personal_view.ciudades.error_text="Campo Obligatorio"
        validacion=False
    else: 
        personal_view.ciudades.error_text=None
        
    return validacion
def validacion_checkbox():
    from views import personal_view
    #funcion que me permite registtrar o no un correo electronico
    personal_view.correo_personal.value = ""
    personal_view.correo_personal.error=None
    
    if personal_view.check_box_correo.value:
        personal_view.text_correo.color= ft.Colors.BLACK
        personal_view.correo_personal.color= ft.Colors.BLACK
        personal_view.correo_personal.read_only = False
        
    else:
        personal_view.correo_personal.read_only = True
        personal_view.correo_personal.color= ft.Colors.GREY_400
        personal_view.text_correo.color=ft.Colors.GREY_400

def estado_incial_foto():
    from views import personal_view
    return ft.Container(
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.UPLOAD, size=40, color=ft.Colors.GREY_400),
                ft.Text("Subir foto", size=12, color=ft.Colors.BLACK),
                ft.Text("JPG o PNG", size=10, color=ft.Colors.GREY_600)
            ]
        ),
        on_click=personal_view.seleccionar_foto,
        ink=True
    )

def guardar_db_datos_limpios():
    from views import personal_view
    cedula=personal_view.cedula_personal.value.strip()
    nombres= personal_view.nombres_personal.value.strip().title()
    apellidos= personal_view.apellidos_personal.value.strip().title()
    telefono= personal_view.numero_telefono_personal.value.strip()
    if personal_view.correo_personal.value=="":
        correo="No se Registro nn Correo"
    else:
        correo=personal_view.correo_personal.value.strip()
    provincia= personal_view.provincias.value
    ciudad= personal_view.ciudades.value
    if personal_view.direccion_personal.value=="":
        direccion="No se Registro una Direccion"
    else: 
        direccion=personal_view.direccion_personal.value.strip()
    
    if personal_view.nueva_ruta=="":
        foto=""
    else:
        foto=personal_view.nueva_ruta
    
    resultado=personal_db.guardar_personal(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,foto)
    
    return resultado

def obtener_datos_personal():
    peronsal={}
    for p in personal_db.mostrar_personal_registrado():
        id_personal=p[0]
        if id_personal not in peronsal:
            peronsal[id_personal]={
                "id_personal": id_personal,
                "CEDULA": p[1],
                "NOMBRES": p[2],
                "APELLIDOS": p[3],
                "TELEFONO": p[4],
                "CORREO": p[5],
                "PROVINCIA": p[6],
                "CIUDAD": p[7],
                "DIRECCION": p[8],
                "FOTO": p[9]
            }
    return peronsal

def guardar_datos_personal(e):
    from views import personal_view
    validacion=validacion_general()
    if validacion == True:
        se_guardo_en_db = guardar_db_datos_limpios()
        if se_guardo_en_db == True:
            e.page.run_task(save_alert,e)
            personal_view.cambiar_vista(personal_view.listado_personal())
        else:
            e.page.run_task(alerta_error, e,"Verifique si la cedula ya existe en el sistema")


def editar_datos_personal():
    from views import personal_view
    cedula=personal_view.cedula_personal.value.strip()
    nombres= personal_view.nombres_personal.value.strip().title()
    apellidos= personal_view.apellidos_personal.value.strip().title()
    telefono= personal_view.numero_telefono_personal.value.strip()
    if personal_view.correo_personal.value=="":
        correo="No Se Registro Un Correo"
    else:
        correo=personal_view.correo_personal.value.strip()
    provincia= personal_view.provincias.value
    ciudad= personal_view.ciudades.value
    if personal_view.direccion_personal.value=="":
        direccion="No se registro una Direccion"
    else: 
        direccion=personal_view.direccion_personal.value.strip()
    
    if personal_view.nueva_ruta=="":
        foto=""
    else:
        foto=personal_view.nueva_ruta
    id=personal_view.id_actual
    
    resultado=personal_db.editar_datos_personal(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,foto,id)
    
    return resultado

def guardar_datos_modificados(e):
    from views import personal_view
    validacion=validacion_general()
    if validacion == True:
        se_guardo_en_db = editar_datos_personal()
        if se_guardo_en_db == True:
            
            e.page.pop_dialog()
            
            e.page.run_task(save_alert,e)
            
            datos=obtener_datos_personal()
            nuevo_item = datos[personal_view.id_actual]

            personal_view.cambiar_vista(
                personal_view.detalles_personal(nuevo_item)
            )

            
        else:
            e.page.run_task(alerta_error, e,"Verifique si la cedula ya existe en el sistema")
provincias=db_core.cargar_catalogo_provincias()

def provincia_change(e):
    from views import personal_view
    pro=personal_view.provincias.value
    id_prov = next((p[0] for p in provincias if p[1] == pro), None)
    
    ciudades= db_core.cargar_catalogo_ciudades(id_prov)
    
    personal_view.ciudades.options=[ft.dropdown.Option(text= p[1],style= ft.TextStyle(color="black")) for p in ciudades]
    personal_view.ciudades.value=None


def eliminar_datos_personal():
    from views import personal_view
    id=personal_view.id_actual
    personal_db.eliminar_datos_personal(id)
    personal_view.cambiar_vista(personal_view.listado_personal())