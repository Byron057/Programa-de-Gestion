import flet as ft
from views import vehiculos_view
import re
from database import vehiculos_db, catalogos_vehiculos_db, clientes_db
from controls import controls_catalogos_vehiculos
from components import *


def limpiar_formulario():
    vehiculos_view.marca_vehiculo.value=""
    vehiculos_view.marca_vehiculo.error_text=None
    vehiculos_view.modelo_vehiculo.value=""
    vehiculos_view.modelo_vehiculo.error_text=None
    vehiculos_view.placa_vehiculo.value=""
    vehiculos_view.placa_vehiculo.error=None
    vehiculos_view.año_vehiculo.value=""
    vehiculos_view.año_vehiculo.error=None
    vehiculos_view.tipo_vehiculo.value=""
    vehiculos_view.tipo_vehiculo.error_text=None
    vehiculos_view.color_vehiculo.value=""
    vehiculos_view.color_vehiculo.error_text=None
    vehiculos_view.propietario_vehiculo.value=None
    vehiculos_view.propietario_vehiculo.text=None
    vehiculos_view.propietario_vehiculo.error_text=None
    
    
    vehiculos_view.checkbox_agregar_reparacion.value=True 
     
def validacion_general():
    validacion=True
    
    marca_veh=vehiculos_view.marca_vehiculo.text.strip()
    modelo_veh=vehiculos_view.modelo_vehiculo.text.strip()
    año_text=vehiculos_view.año_vehiculo.value.strip()
    tipo_veh=vehiculos_view.tipo_vehiculo.text.strip()
    color_veh=vehiculos_view.color_vehiculo.text.strip()
    propietario_value=vehiculos_view.propietario_vehiculo.value
    propietario_text=vehiculos_view.propietario_vehiculo.text
    
    opciones= vehiculos_view.propietario_vehiculo.options
    
    textos_validos=[opt.text for opt in opciones]
    
    if not marca_veh:
        vehiculos_view.marca_vehiculo.error_text="Campo Obligatorio"
        validacion=False
    else:
        vehiculos_view.marca_vehiculo.error_text=None
        
    if not modelo_veh:
        vehiculos_view.modelo_vehiculo.error_text="Campo Obligatorio"
        validacion=False
    else:
        vehiculos_view.modelo_vehiculo.error_text=None
        
    patron_placa= r'^[A-Z]{2,3}-\d{3,4}$'
    
    if not vehiculos_view.placa_vehiculo.value:
        vehiculos_view.placa_vehiculo.error="Campo Obligatorio"
        validacion=False
    elif not re.match(patron_placa, vehiculos_view.placa_vehiculo.value):
        vehiculos_view.placa_vehiculo.error="Ingrese una Placa Valida"
        validacion=False
    else:
        vehiculos_view.placa_vehiculo.error=None
    
    if not año_text:
        vehiculos_view.año_vehiculo.error="Campo Obligatorio"
        validacion=False
    elif not año_text.isdigit():
        vehiculos_view.año_vehiculo.error="Solo se permite numeros"
        validacion=False
    else:
        año_veh=int(año_text)
        vehiculos_view.año_vehiculo.error=None
        if año_veh<=1950 or año_veh>=2026:
            vehiculos_view.año_vehiculo.error="Ingrese un año Valido"
            validacion=False
        else:
            vehiculos_view.año_vehiculo.error=None
    if not tipo_veh:
        vehiculos_view.tipo_vehiculo.error_text="Campo Obligatorio"
        validacion=False
    else:
        vehiculos_view.tipo_vehiculo.error_text=None
    if not color_veh:
        vehiculos_view.color_vehiculo.error_text="Campo Obligatorio"
        validacion=False
    else:
        vehiculos_view.color_vehiculo.error_text=None
    
    #cambie por value si en el futuro da algun error antes estaba como text 
    if not propietario_value:
        vehiculos_view.propietario_vehiculo.value = None
        vehiculos_view.propietario_vehiculo.value= None
        vehiculos_view.propietario_vehiculo.error_text = None
    elif propietario_text not in textos_validos:
        vehiculos_view.propietario_vehiculo.error_text = "Seleccione un propietario válido"
        validacion = False
    else:
        vehiculos_view.propietario_vehiculo.error_text = None
        
    return validacion

def guardar_datos_limpios_vehiculo():
    
    controls_catalogos_vehiculos.gaurdar_datos_catalogos()
    vehiculos_view.cargar_catalogos()
    marca=vehiculos_view.marca_vehiculo.text.strip().title()
    id_cliente=vehiculos_view.propietario_vehiculo.value
    id_marca= next(
        (ma[0] for ma in catalogos_vehiculos_db.mostrar_marcas() if ma[1] == marca), 
        None
    )
    modelo=vehiculos_view.modelo_vehiculo.text.strip().title()
    id_modelo= next(
        (mo[0] for mo in catalogos_vehiculos_db.mostrar_modelos(id_marca) if mo[1] == modelo),
        None
    )
    placa=vehiculos_view.placa_vehiculo.value.strip().upper()
    year=vehiculos_view.año_vehiculo.value.strip().title()
    
    tipo=vehiculos_view.tipo_vehiculo.text
    id_tipo=next(
        (ti[0] for ti in catalogos_vehiculos_db.mostrar_tipos_vehiculos() if ti[1]== tipo),
        None
    )
    color=vehiculos_view.color_vehiculo.text
    id_color=next(
        (co[0] for co in catalogos_vehiculos_db.mostrar_colores() if co[1] == color),
        None
    )
    resultado=vehiculos_db.guardar_vehiculos(id_cliente, id_marca, id_modelo, placa, year, id_tipo, id_color)
    
    return True
    
def obtener_datos_vehiculos():
    vehiculos={}
    for v in vehiculos_db.mostrar_vehiculos_registrados():
        id_vehiculo= v[0]
        if id_vehiculo not in vehiculos:
            vehiculos[id_vehiculo]={
                "id_vehiculo": id_vehiculo,
                "id_cliente": v[1],
                "MARCA": v[2],
                "MODELO":v[3],
                "PLACA": v[4],
                "YEAR": v[5],
                "TIPO": v[6],
                "COLOR": v[7],
                "PROPIETARIO": []
            }
        if v[8]:
            propietario={
                "CEDULA": v[8],
                "NOMBRES": v[9],
                "APELLIDOS": v[10],
                "TELEFONO": v[11],
            }
            if not any(c["CEDULA"] == v[8] for c in vehiculos[id_vehiculo]["PROPIETARIO"]):
                vehiculos[id_vehiculo]["PROPIETARIO"].append(propietario)
    return vehiculos

def guardar_datos_vehiculos(e, cerrar_dialog=False):
    validacion=validacion_general()
    if validacion==True:
        se_guardo_db= guardar_datos_limpios_vehiculo()
        if se_guardo_db == True:
            e.page.run_task(save_alert,e)
            if cerrar_dialog== False:
                vehiculos_view.cambiar_vista(vehiculos_view.listado_vehiculos())
            else:
                e.page.pop_dialog()
        else:
            e.page.run_task(alerta_error,e,"Verifique si los datos ya estan en el sistema")
            
def editar_datos_vehiculo():
    controls_catalogos_vehiculos.gaurdar_datos_catalogos()
    vehiculos_view.cargar_catalogos()
    marca=vehiculos_view.marca_vehiculo.text.strip().title()
    
    id_cliente=vehiculos_view.propietario_vehiculo.value
    
    id_marca= next(
        (ma[0] for ma in catalogos_vehiculos_db.mostrar_marcas() if ma[1] == marca), 
        None
    )
    modelo=vehiculos_view.modelo_vehiculo.text.strip().title()
    id_modelo= next(
        (mo[0] for mo in catalogos_vehiculos_db.mostrar_modelos(id_marca) if mo[1] == modelo),
        None
    )
    placa=vehiculos_view.placa_vehiculo.value.strip().upper()
    year=vehiculos_view.año_vehiculo.value.strip().title()
    
    tipo=vehiculos_view.tipo_vehiculo.text
    id_tipo=next(
        (ti[0] for ti in catalogos_vehiculos_db.mostrar_tipos_vehiculos() if ti[1]== tipo),
        None
    )
    color=vehiculos_view.color_vehiculo.text
    id_color=next(
        (co[0] for co in catalogos_vehiculos_db.mostrar_colores() if co[1] == color),
        None
    )
    id_vehiculo= vehiculos_view.id_actual_veh
    resultado=vehiculos_db.editar_datos_vehiculo(id_cliente, id_marca, id_modelo, placa, year, id_tipo, id_color,id_vehiculo)
    
    return resultado
def guardar_datos_editados(e):
    validacion=validacion_general()
    if validacion==True:
        se_guardo_db= editar_datos_vehiculo()
        if se_guardo_db == True:
            e.page.run_task(save_alert,e)
            e.page.pop_dialog()
            datos=obtener_datos_vehiculos()
            nuevo_item=datos[vehiculos_view.id_actual_veh]
            vehiculos_view.cambiar_vista(
                vehiculos_view.detalles_vehiculos(nuevo_item)
            )
        else:
            e.page.run_task(alerta_error,e,"Verifique si los datos ya estan en el sistema")