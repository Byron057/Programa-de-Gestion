import flet as ft 
from views import vehiculos_view
from controls import controls_clientes as ctr_cln
from database import catalogos_vehiculos_db,clientes_db
from components import *

def mostrar_marcas():
    return catalogos_vehiculos_db.mostrar_marcas()
def mostrar_colores():
    return catalogos_vehiculos_db.mostrar_colores()
def mostrar_tipos_vehiculos():
    return catalogos_vehiculos_db.mostrar_tipos_vehiculos()
def mostrar_clientes():
    return ctr_cln.obtener_datos_clientes()



def gaurdar_datos_catalogos():
    marca=vehiculos_view.marca_vehiculo.text.strip().title()
    modelo=vehiculos_view.modelo_vehiculo.text.strip().title()
    color=vehiculos_view.color_vehiculo.text.strip().title()
    tipo=vehiculos_view.tipo_vehiculo.text.strip().title()
    
    id_marca=catalogos_vehiculos_db.guardar_nueva_marca(marca)
    print(id_marca)
    catalogos_vehiculos_db.guardar_nuevo_modelo(id_marca,modelo)
    catalogos_vehiculos_db.guardar_nuevo_color(color)
    catalogos_vehiculos_db.guardar_nuevo_tipo(tipo)
    
    
def marca_change(e):
    marca=vehiculos_view.marca_vehiculo.text
    id= next((m[0] for m in mostrar_marcas() if m[1]== marca),None)
    
    modelos= catalogos_vehiculos_db.mostrar_modelos(id)
    
    vehiculos_view.modelo_vehiculo.options=[ft.dropdown.Option(text= m[1],style= ft.TextStyle(color="black")) for m in modelos]
    vehiculos_view.modelo_vehiculo.value=None