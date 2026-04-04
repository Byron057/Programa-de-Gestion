import flet as ft 
import re
from views import clientes_view,vehiculos_view
from database import db_core
from database import clientes_db
from components import *
def total_clientes():
    total_clientes=clientes_db.contar_clientes_activos()
    return total_clientes
provincias=db_core.cargar_catalogo_provincias()


def limpiar_formulario():
    #reestablece los datos del formulario
    clientes_view.nombres_cliente.value=""
    clientes_view.apellidos_cliente.value=""
    clientes_view.cedula_cliente.value=""
    clientes_view.numero_telefono_cliente.value=""
    clientes_view.correo_cliente.value=""
    clientes_view.text_correo.color=ft.Colors.BLACK
    clientes_view.correo_cliente.color=ft.Colors.BLACK
    clientes_view.correo_cliente.read_only=False
    clientes_view.provincias.value=""
    clientes_view.ciudades.value=""
    clientes_view.direccion_cliente.value=""
    clientes_view.check_box_correo.value=True
    
    clientes_view.nombres_cliente.error=None
    clientes_view.apellidos_cliente.error=None
    clientes_view.cedula_cliente.error=None
    clientes_view.numero_telefono_cliente.error=None
    clientes_view.correo_cliente.error=None
    clientes_view.provincias.error_text=None
    clientes_view.ciudades.error_text=None
    clientes_view.direccion_cliente.error=None
    
def validacion_checkbox():
    #funcion que me permite registtrar o no un correo electronico
    clientes_view.correo_cliente.value = ""
    
    if clientes_view.check_box_correo.value:
        clientes_view.text_correo.color= ft.Colors.BLACK
        clientes_view.correo_cliente.color= ft.Colors.BLACK
        clientes_view.correo_cliente.read_only = False
        
    else:
        clientes_view.correo_cliente.read_only = True
        clientes_view.correo_cliente.color= ft.Colors.GREY_400
        clientes_view.text_correo.color=ft.Colors.GREY_400

def validacion_general():
    validacion=True
    nombres_clientes= clientes_view.nombres_cliente.value.strip()
    apellidos_clientes= clientes_view.apellidos_cliente.value.strip()
    
    if not nombres_clientes:
        clientes_view.nombres_cliente.error="Campo Obligatorio"
        clientes_view.nombres_cliente.value=""
        validacion=False
    elif nombres_clientes.isdigit():
        clientes_view.nombres_cliente.error="Ingrese un valor correcto"
        validacion=False
    else:
        clientes_view.nombres_cliente.error=None
        
    if not apellidos_clientes:
        clientes_view.apellidos_cliente.error="Campo Obligatorio"
        clientes_view.apellidos_cliente.value=""
        validacion=False
    elif apellidos_clientes.isdigit():
        clientes_view.apellidos_cliente.error="Ingrese un valor correcto"
        validacion=False
    else:
        clientes_view.apellidos_cliente.error=None
        
    if not clientes_view.cedula_cliente.value:
        clientes_view.cedula_cliente.error="Campo Obligatorio"
        validacion=False
    elif not clientes_view.cedula_cliente.value.isdigit():
        clientes_view.cedula_cliente.error="Solo se Permite Ingresar Números"
        validacion=False
    elif len (clientes_view.cedula_cliente.value) != 10:
        clientes_view.cedula_cliente.error="Ingrese 10 Dígitos"
        validacion=False
    else:
        clientes_view.cedula_cliente.error=None
    
    if not clientes_view.numero_telefono_cliente.value:
        clientes_view.numero_telefono_cliente.error="Campo Obligatorio"
        validacion=False
    elif not clientes_view.numero_telefono_cliente.value.isdigit():
        clientes_view.numero_telefono_cliente.error="Solo se Permite Ingresar Números"
        validacion=False
    elif len (clientes_view.numero_telefono_cliente.value)!= 10:
        clientes_view.numero_telefono_cliente.error="Ingrese 10 Dígitos"
        validacion=False
    else:
        clientes_view.numero_telefono_cliente.error=None
    
    patron_correo=r'^[\w\.-]+@[\w\.-]+\.\w+$'  
    
    if clientes_view.check_box_correo.value:
        if not clientes_view.correo_cliente.value:
            clientes_view.correo_cliente.error="Campo Obligatorio"
            validacion=False
        elif not re.match(patron_correo, clientes_view.correo_cliente.value):
            clientes_view.correo_cliente.error="Formato Invalido"
            validacion=False
        else:
            clientes_view.correo_cliente.error=None

    if not clientes_view.provincias.value:
        clientes_view.provincias.error_text="Campo Obligatorio"
        validacion=False
    else: 
        clientes_view.provincias.error_text=None
    
    if not clientes_view.ciudades.value:
        clientes_view.ciudades.error_text="Campo Obligatorio"
        validacion=False
    else: 
        clientes_view.ciudades.error_text=None
        
    return validacion

def guardar_db_datos_limpios():
    cedula=clientes_view.cedula_cliente.value.strip()
    nombres=clientes_view.nombres_cliente.value.strip().title()
    apellidos= clientes_view.apellidos_cliente.value.strip().title()
    telefono= clientes_view.numero_telefono_cliente.value.strip()
    if clientes_view.correo_cliente.value=="":
        correo="No se Registro un Correo"
    else:
        correo=clientes_view.correo_cliente.value.strip()
    provincia=clientes_view.provincias.value
    ciudad=clientes_view.ciudades.value
    if clientes_view.direccion_cliente.value=="":
        direccion="No se Registro una Direccion"
    else:
        direccion=clientes_view.direccion_cliente.value.strip()
    #Flata registrar un vehiculo, campo obligatorio para mostrar reportes, si no esta asociado a un vehiculo este presentara una alerta

    resultado,ultimo_id=clientes_db.guardar_clientes(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion)
    
    return resultado,ultimo_id
    
def provincia_change(e):
    pro=clientes_view.provincias.value
    id_prov = next((p[0] for p in provincias if p[1] == pro), None)
    
    ciudades= db_core.cargar_catalogo_ciudades(id_prov)
    
    clientes_view.ciudades.options=[ft.dropdown.Option(text= c[1],style= ft.TextStyle(color="black")) for c in ciudades]
    clientes_view.ciudades.value=None

#Permite asiganr los valores al dropdown para que no exista ningun problema al validar
def autollenado_dropdown(value):
    dropdown=vehiculos_view.propietario_vehiculo
    dropdown.value = str(value)
    for opt in dropdown.options:
        if str(opt.key) == str(value):
            dropdown.text = opt.text
            break

def guardar_datos_clientes(e, cerrar_dialog=False):
    validacion= validacion_general()
    if validacion==True:
        se_guardo_en_db,nuevo_id= guardar_db_datos_limpios()
        if se_guardo_en_db == True:
            e.page.run_task(save_alert,e)
            if cerrar_dialog== False:
                clientes_view.cambiar_vista(clientes_view.listado_clientes())
            else:
                vehiculos_view.cargar_catalogos()
                autollenado_dropdown(nuevo_id)
                e.page.pop_dialog()
                limpiar_formulario()
        else:
            e.page.run_task(alerta_error, e,"Verifique si la cedula ya existe en el sistema")


def obtener_datos_clientes():
    clientes={}
    for c in clientes_db.mostrar_clientes_registrados():
        id_cliente=c[0]
        if id_cliente not in clientes:
            clientes[id_cliente]={
                "id_cliente": id_cliente,
                "CEDULA": c[1],
                "NOMBRES": c[2],
                "APELLIDOS": c[3],
                "TELEFONO": c[4],
                "CORREO": c[5],
                "PROVINCIA": c[6],
                "CIUDAD": c[7],
                "DIRECCION": c[8],
                "VEHICULOS": []
            }
            
        if c[9]: 
            vehiculo = {
                "id_vehiculo": c[9],
                "PLACA": c[10],
                "MODELO": c[11],
                "TIPO": c[12],
            }
            if not any(v["id_vehiculo"] == c[9] for v in clientes[id_cliente]["VEHICULOS"]):
                clientes[id_cliente]["VEHICULOS"].append(vehiculo)

            
    return clientes

def editar_datos_clientes():
    cedula=clientes_view.cedula_cliente.value.strip()
    nombres=clientes_view.nombres_cliente.value.strip().title()
    apellidos= clientes_view.apellidos_cliente.value.strip().title()
    telefono= clientes_view.numero_telefono_cliente.value.strip()
    if clientes_view.correo_cliente.value=="":
        correo="No se Registro un Correo"
    else:
        correo=clientes_view.correo_cliente.value.strip()
    provincia=clientes_view.provincias.value
    ciudad=clientes_view.ciudades.value
    if clientes_view.direccion_cliente.value=="":
        direccion="No se Registro una Direccion"
    else:
        direccion=clientes_view.direccion_cliente.value.strip()
    id=clientes_view.id_actual
    #Flata registrar un vehiculo, campo obligatorio para mostrar reportes, si no esta asociado a un vehiculo este presentara una alerta

    resultado= clientes_db.editar_datos_clientes(cedula, nombres, apellidos, telefono, correo, provincia, ciudad, direccion,id)
    
    return resultado

def guardar_datos_modificados(e):
    validacion= validacion_general()
    if validacion==True:
        se_guardo_en_db= editar_datos_clientes()
        if se_guardo_en_db == True:
            e.page.run_task(save_alert,e)
            
            e.page.pop_dialog()
            
            datos=obtener_datos_clientes()
            nuevo_item=datos[clientes_view.id_actual]
            clientes_view.cambiar_vista(
                clientes_view.detalles_clientes(nuevo_item)
            )
        else:
            e.page.run_task(alerta_error, e,"Verifique si la cedula ya existe en el sistema")

def eliminar_datos_cliente():
   id=clientes_view.id_actual
   clientes_db.eliminar_clientes(id)
   clientes_view.cambiar_vista(clientes_view.listado_clientes())