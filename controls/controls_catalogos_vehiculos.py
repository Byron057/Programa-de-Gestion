import flet as ft 
from views import vehiculos_view
from controls import controls_clientes as ctr_cln
from database import catalogos_vehiculos_db
from views import vehiculos_view, reparaciones_view
from components import *

def mostrar_marcas():
    return catalogos_vehiculos_db.mostrar_marcas()
def mostrar_colores():
    return catalogos_vehiculos_db.mostrar_colores()
def mostrar_tipos_vehiculos():
    return catalogos_vehiculos_db.mostrar_tipos_vehiculos()
def mostrar_clientes():
    return ctr_cln.obtener_datos_clientes()

def mostrar_repuestos():
    return catalogos_vehiculos_db.mostrar_repuestos()

def mostrar_marcas_repuestos():
    return catalogos_vehiculos_db.mostrar_marca_repuestos()

def mostrar_porveedores_repuestos():
    return catalogos_vehiculos_db.mostrar_proveedor_repuestos()


def gaurdar_datos_catalogos():
    marca=vehiculos_view.marca_vehiculo.text.strip().title()
    modelo=vehiculos_view.modelo_vehiculo.text.strip().title()
    color=vehiculos_view.color_vehiculo.text.strip().title()
    tipo=vehiculos_view.tipo_vehiculo.text.strip().title()
    
    id_marca=catalogos_vehiculos_db.guardar_nueva_marca(marca)
    catalogos_vehiculos_db.guardar_nuevo_modelo(id_marca,modelo)
    catalogos_vehiculos_db.guardar_nuevo_color(color)
    catalogos_vehiculos_db.guardar_nuevo_tipo(tipo)
    
    
def marca_change(e):
    marca = vehiculos_view.marca_vehiculo.value or vehiculos_view.marca_vehiculo.text
    if isinstance(marca, str):
        marca = marca.strip().title()
    else:
        marca = None
    id = next((m[0] for m in mostrar_marcas() if m[1] == marca), None)
    
    modelos = catalogos_vehiculos_db.mostrar_modelos(id) if id else []
    
    vehiculos_view.modelo_vehiculo.options = [
        ft.dropdown.Option(text=m[1], style=ft.TextStyle(color="black")) for m in modelos
    ]
    vehiculos_view.modelo_vehiculo.value = None
    vehiculos_view.modelo_vehiculo.text = ""

def validar_campos_repuestos():
    validacion=True
    for fila in reparaciones_view.lista_repuestos.controls[:]:
        repuesto=fila.data["repuesto"]
        marca=fila.data["marca"]
        proovedor=fila.data["proveedor"]
        
        if not repuesto.text and not marca.text and not proovedor.text and len(reparaciones_view.lista_repuestos.controls)>1:
            reparaciones_view.lista_repuestos.controls.remove(fila)
            reparaciones_view.actualizar_boton_repuestos()
        if  repuesto.text or marca.text or proovedor.text or len(reparaciones_view.lista_repuestos.controls)>1:    

            if not repuesto.text:
                repuesto.error_text="Campo Obligatorio"
                validacion=False
            else:
                fila.data["espacio_repuesto"].visible=True
                fila.data["espacio_boton"].visible=True
                repuesto.error_text=None
                
            if not marca.text:
                marca.error_text="Campo Obligatorio"
                validacion=False
            else:
                fila.data["espacio_marca"].visible=True
                fila.data["espacio_boton"].visible=True
                marca.error_text=None
            if not proovedor.text:
                proovedor.error_text="Campo Obligatorio"
                validacion=False
            else:
                fila.data["espacio_proveedor"].visible=True
                fila.data["espacio_boton"].visible=True
                proovedor.error_text= None
        else:
            repuesto.error_text=None
            marca.error_text=None
            proovedor.error_text= None
            
        if not marca.error_text and not repuesto.error_text and not proovedor.error_text:
            fila.data["espacio_repuesto"].visible=False
            fila.data["espacio_marca"].visible=False
            fila.data["espacio_proveedor"].visible=False
            fila.data["espacio_boton"].visible=False
        else:
            
            fila.data["espacio_boton"].visible=True
    return validacion

def guardar_campos_repuestos():
    for fila in reparaciones_view.lista_repuestos.controls[:]:
        if not fila.data["repuesto"].text and not fila.data["marca"].text and not fila.data["proveedor"].text:
            continue
        else:
            repuesto=fila.data["repuesto"].text.title()
            marca=fila.data["marca"].text.title()
            proveedor=fila.data["proveedor"].text.title()
        
            id_repuesto=catalogos_vehiculos_db.guardar_repuesto(repuesto)
            id_marca=catalogos_vehiculos_db.guardar_marca_repuesto(marca)
            id_proveedor=catalogos_vehiculos_db.guardar_proveedor_repuesto(proveedor)
                
            return id_repuesto, id_marca, id_proveedor
    return None