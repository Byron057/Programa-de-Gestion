import flet as ft 
from views import vehiculos_view
from database import vehiculos_db
from components import *

def guardar_marcas():
    pass

def mostrar_vehiculos():
    return vehiculos_db.catalogos_vehiculos.mostrar_marcas()

def marca_change(e):
    marca=vehiculos_view.marca_vehiculo.value
    id= next((m[0] for m in marca if m[1]== marca),None)
    
    