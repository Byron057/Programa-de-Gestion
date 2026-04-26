import flet as ft 
from views import reparaciones_view
from components import *

def limpiar_lista_reparaciones():
    for fila in reparaciones_view.lista_reparaciones.controls[:]:
        boton= fila.controls[2]
        textfield=fila.controls[0]
        if boton.icon == ft.Icons.DELETE:
            reparaciones_view.lista_reparaciones.controls.remove(fila)
        textfield.value=""

def limpiar_lista_repuestos():
    for fila in reparaciones_view.lista_repuestos.controls[:]:
        boton=fila.controls[3]
        repuesto= fila.controls[0]
        marca= fila.controls[1]
        proveedor= fila.controls[2]
        if boton.icon == ft.Icons.DELETE:
            reparaciones_view.lista_repuestos.controls.remove(fila)
        repuesto.value=""
        marca.value=""
        proveedor.value=""

def bloquear_dropdown_repustos(estado=False):
    for fila in reparaciones_view.lista_repuestos.controls:
        repuesto=fila.controls[0]
        repuesto.controls[1].visible=estado
        repuesto.controls[0].value=None
        repuesto.controls[0].text=None
        
        marca=fila.controls[1]
        marca.controls[1].visible=estado
        marca.controls[0].value=None
        marca.controls[0].text=None
        
        proveedor=fila.controls[2]
        proveedor.controls[1].visible=estado
        proveedor.controls[0].value=None
        proveedor.controls[0].text=None
        
        
        
def cambiar_color_repuestos(boton_color, boton_disabled):
    for fila in reparaciones_view.lista_repuestos.controls[:]:
        boton=fila.controls[3]
        
        boton.color=boton_color
        boton.disabled=boton_disabled

def cambiar_color_reparaciones(color_boton, disabled_boton, color_textfield, disabled_textfield):
    for fila in reparaciones_view.lista_reparaciones.controls[:]:
        boton= fila.controls[2]
        textfield= fila.controls[0]
        text_field_precio=fila.controls[1]
        
        boton.color=color_boton
        boton.disabled= disabled_boton
        
        textfield.color= color_textfield
        textfield.read_only= disabled_textfield
        
        text_field_precio.color=color_textfield
        text_field_precio.read_only= disabled_textfield
        text_field_precio.suffix=Text("$", 20, color_textfield)
        

def interfaz_checkbox_vehiculos():
    #restablece algunos campos funciona de la misma manera que la funcion de limpiar campos
    reparaciones_view.fecha_entrada.value=reparaciones_view.fecha_actual
    reparaciones_view.fecha_entrega.value=reparaciones_view.fecha_actual
    reparaciones_view.kilometraje_actual.value=""
    reparaciones_view.siguiente_kilometraje.value=""
    reparaciones_view.personal_encargado.value=None
    reparaciones_view.personal_encargado.text=None
    reparaciones_view.precio_total_reaparacion.value=""
    reparaciones_view.lista_imagenes.controls.clear()
    reparaciones_view.imagenes_seleccionadas.clear()
    reparaciones_view.nuevas_rutas_imagenes.clear()
    
    limpiar_lista_reparaciones()
    limpiar_lista_repuestos()
   
    if reparaciones_view.vehiculos_view.checkbox_agregar_reparacion.value==True:
        #cambiar a la carpeta controls
        reparaciones_view.text_fecha_entrada.color=ft.Colors.BLACK
        reparaciones_view.fecha_entrada.color=ft.Colors.BLACK
        reparaciones_view.calendario_entrada.icon_color=ft.Colors.BLUE_700
        reparaciones_view.calendario_entrada.disabled=False
        
        reparaciones_view.text_fecha_entrega.color=ft.Colors.BLACK
        reparaciones_view.fecha_entrega.color=ft.Colors.BLACK
        reparaciones_view.calendario_entrega.icon_color=ft.Colors.BLUE_700
        reparaciones_view.calendario_entrega.disabled=False
        
        reparaciones_view.stack_personal_encargaado.controls[1].visible=False
        reparaciones_view.suffix_kilometraje_actual.color=ft.Colors.BLACK
        reparaciones_view.text_kilometraje_actual.color=ft.Colors.BLACK
        reparaciones_view.kilometraje_actual.color=ft.Colors.BLACK
        reparaciones_view.kilometraje_actual.read_only= False
        
        reparaciones_view.text_personal_encargado.color=ft.Colors.BLACK
        reparaciones_view.personal_encargado.disabled=False
        
        reparaciones_view.text_precio_total.color=ft.Colors.BLACK
        reparaciones_view.precio_total_reaparacion.color=ft.Colors.BLACK
        reparaciones_view.suffix_precio_reparacion.color=ft.Colors.BLACK
        reparaciones_view.precio_total_reaparacion.read_only=False
        
        reparaciones_view.suffix_siguiente_kilometraje.color=ft.Colors.BLACK
        reparaciones_view.text_siguiente_kilometraje.color=ft.Colors.BLACK
        reparaciones_view.siguiente_kilometraje.color=ft.Colors.BLACK
        reparaciones_view.siguiente_kilometraje.read_only=False
        
        reparaciones_view.text_reparaciones.color=ft.Colors.BLACK
        cambiar_color_reparaciones(ft.Colors.GREEN_400, False, ft.Colors.BLACK, False)
        
        reparaciones_view.text_repuestos.color=ft.Colors.BLACK
        bloquear_dropdown_repustos(False)
        cambiar_color_repuestos(ft.Colors.GREEN_400, False)
        
        reparaciones_view.text_galeria.color=ft.Colors.BLACK
        reparaciones_view.seleccionar_imagen.disabled=False
        
    else:
        reparaciones_view.text_fecha_entrada.color=ft.Colors.GREY_400
        reparaciones_view.fecha_entrada.color=ft.Colors.GREY_400
        reparaciones_view.calendario_entrada.icon_color=ft.Colors.GREY_400
        reparaciones_view.calendario_entrada.disabled=True
        
        reparaciones_view.text_fecha_entrega.color=ft.Colors.GREY_400
        reparaciones_view.fecha_entrega.color=ft.Colors.GREY_400
        reparaciones_view.calendario_entrega.icon_color=ft.Colors.GREY_400
        reparaciones_view.calendario_entrega.disabled=True
        
        reparaciones_view.text_personal_encargado.color=ft.Colors.GREY_400
        reparaciones_view.stack_personal_encargaado.controls[1].visible=True
        
        reparaciones_view.text_precio_total.color=ft.Colors.GREY_400
        reparaciones_view.precio_total_reaparacion.color=ft.Colors.GREY_400
        reparaciones_view.suffix_precio_reparacion.color=ft.Colors.GREY_400
        reparaciones_view.precio_total_reaparacion.read_only=True
        
        reparaciones_view.suffix_kilometraje_actual.color=ft.Colors.GREY_400
        reparaciones_view.text_kilometraje_actual.color=ft.Colors.GREY_400
        reparaciones_view.kilometraje_actual.color=ft.Colors.GREY_400
        reparaciones_view.kilometraje_actual.read_only= True
        
        reparaciones_view.suffix_siguiente_kilometraje.color=ft.Colors.GREY_400
        reparaciones_view.text_siguiente_kilometraje.color=ft.Colors.GREY_400
        reparaciones_view.siguiente_kilometraje.color=ft.Colors.GREY_400
        reparaciones_view.siguiente_kilometraje.read_only=True
        
        reparaciones_view.text_reparaciones.color=ft.Colors.GREY_400
        cambiar_color_reparaciones(ft.Colors.GREY_400, True, ft.Colors.GREY_400, True)
        
        reparaciones_view.text_repuestos.color=ft.Colors.GREY_400
        bloquear_dropdown_repustos(True)
        cambiar_color_repuestos(ft.Colors.GREY_400, True)
        
        reparaciones_view.text_galeria.color=ft.Colors.GREY_400
        reparaciones_view.seleccionar_imagen.disabled=True