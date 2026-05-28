import flet as ft 
from views import reparaciones_view
from database import reparaciones_db
from controls import controls_catalogos_vehiculos as ctr_cat_veh
from controls import controls_vehiculos as ctr_veh
from views import vehiculos_view
from components import *

def limpiar_lista_reparaciones():
    for fila in reparaciones_view.lista_reparaciones.controls[:]:
        boton= fila.data["boton"]
        reparacion=fila.data["reparacion"]
        precio=fila.data["precio"]
        
        if boton.icon == ft.Icons.DELETE:
            reparaciones_view.lista_reparaciones.controls.remove(fila)
        reparacion.value=None
        precio.value=None

def limpiar_lista_repuestos():
    for fila in reparaciones_view.lista_repuestos.controls[:]:
        boton=fila.data["boton"]
        repuesto= fila.data["repuesto"]
        marca= fila.data["marca"]
        proveedor= fila.data["proveedor"]
        if boton.icon == ft.Icons.DELETE:
            reparaciones_view.lista_repuestos.controls.remove(fila)
            
        repuesto.error_text=None
        marca.error_text=None
        proveedor.error_text=None
        
        repuesto.value=""
        marca.value=""
        proveedor.value=""
        
        fila.data["espacio_repuesto"].visible=False
        fila.data["espacio_marca"].visible=False
        fila.data["espacio_proveedor"].visible=False
        fila.data["espacio_boton"].visible=False
        
def bloquear_dropdown_repuestos(estado=False):
    for fila in reparaciones_view.lista_repuestos.controls:
        repuesto=fila.data["repuesto"]
        fila.data["bloqueo_repuesto"].visible=estado
        repuesto.value=None
        repuesto.text=None
        
        marca=fila.data["marca"]
        fila.data["bloqueo_marca"].visible=estado
        marca.value=None
        marca.text=None
        
        proveedor=fila.data["proveedor"]
        fila.data["bloqueo_proveedor"].visible=estado
        proveedor.value=None
        proveedor.text=None
            
def cambiar_color_repuestos(boton_color, boton_disabled):
    for fila in reparaciones_view.lista_repuestos.controls[:]:
        boton=fila.data["boton"]
        
        boton.color=boton_color
        boton.disabled=boton_disabled

def cambiar_color_reparaciones(color_boton, disabled_boton, color_textfield, disabled_textfield):
    for fila in reparaciones_view.lista_reparaciones.controls[:]:
        boton= fila.data["boton"]
        reparacion= fila.data["reparacion"]
        precio=fila.data["precio"]
        
        boton.color=color_boton
        boton.disabled= disabled_boton
        
        reparacion.color= color_textfield
        reparacion.read_only= disabled_textfield
        
        precio.color=color_textfield
        precio.read_only= disabled_textfield
        precio.suffix=Text("$", 20, color_textfield)
        
def limpiar_campos_reparacion():
    reparaciones_view.fecha_entrada.value=reparaciones_view.fecha_actual
    reparaciones_view.fecha_entrega.value=reparaciones_view.fecha_actual
    reparaciones_view.kilometraje_actual.value=None
    reparaciones_view.siguiente_kilometraje.value=None
    reparaciones_view.personal_encargado.value=None
    reparaciones_view.personal_encargado.text=None
    reparaciones_view.precio_total_reaparacion.value=None
    reparaciones_view.lista_imagenes.controls.clear()
    reparaciones_view.imagenes_seleccionadas.clear()
    reparaciones_view.nuevas_rutas_imagenes.clear()
    limpiar_lista_reparaciones()
    limpiar_lista_repuestos()
    
def interfaz_checkbox_vehiculos():
    #restablece algunos campos funciona de la misma manera que la funcion de limpiar campos
    limpiar_campos_reparacion()
    reparaciones_view.seleccionar_imagen.bgcolor=ft.Colors.GREY_200
    
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
        
        reparaciones_view.stack_personal_encargado.controls[1].visible=False
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
        bloquear_dropdown_repuestos(False)
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
        reparaciones_view.stack_personal_encargado.controls[1].visible=True
        
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
        bloquear_dropdown_repuestos(True)
        cambiar_color_repuestos(ft.Colors.GREY_400, True)
        
        reparaciones_view.text_galeria.color=ft.Colors.GREY_400
        reparaciones_view.seleccionar_imagen.disabled=True
 
def validar_campos_reparaciones():
    validacion=True
    for fila in reparaciones_view.lista_reparaciones.controls[:]:
        reparacion=fila.data["reparacion"]
        precio=fila.data["precio"]
        
        if not reparacion.value and not precio.value and len(reparaciones_view.lista_reparaciones.controls) > 1:
            reparaciones_view.lista_reparaciones.controls.remove(fila)
            reparaciones_view.actualizar_boton_reparaciones()
        
        if not reparacion.value:
            reparacion.error="Campo Obligatorio"
            validacion=False
        elif reparacion.value.strip()=="":
            reparacion.error="Campo Obligatorio"
            reparacion.value=""
            validacion=False
        else:
            reparacion.error=None
            fila.data["espacio_reparacion"].visible=True
            fila.data["espacio_boton"].visible=True
        
        if not precio.value:
            precio.error="Campo Obligatorio"
            validacion=False
        else:
            precio.error=None
            fila.data["espacio_precio"].visible=True
            fila.data["espacio_boton"].visible=True
        
        reparacion_valida = reparacion.value and reparacion.value.strip()
        precio_valido = precio.value and precio.value.strip()

        if reparacion_valida and precio_valido:
            fila.data["espacio_reparacion"].visible = False
            fila.data["espacio_precio"].visible = False
            fila.data["espacio_boton"].visible = False
        else:
            fila.data["espacio_boton"].visible = True
    return validacion        
    
def guardar_campos_reparaciones(id_orden_rep):
    for fila in reparaciones_view.lista_reparaciones.controls[:]:
        reparacion=fila.data["reparacion"].value.title().strip()
        precio=fila.data["precio"].value.title().strip()
        reparaciones_db.guardar_reparaciones_realizadas(id_orden_rep, reparacion, precio)              

def validacion_general():
    validacion= True
    
    validacion_reparacion=validar_campos_reparaciones()
    validacion_repuestos=ctr_cat_veh.validar_campos_repuestos()

    if not reparaciones_view.personal_encargado.value:
        reparaciones_view.personal_encargado.error_text="Campo Obligatorio"
        validacion=False
    else:
        reparaciones_view.personal_encargado.error_text=None
    
    if not reparaciones_view.precio_total_reaparacion.value:
        reparaciones_view.precio_total_reaparacion.error="Campo Obligatorio"
        validacion=False
    else:
        reparaciones_view.precio_total_reaparacion.error=None
    
    if not reparaciones_view.kilometraje_actual.value:
        reparaciones_view.kilometraje_actual.error="Campo Obligatorio"
        validacion=False
    elif not reparaciones_view.kilometraje_actual.value.isdigit():
        reparaciones_view.kilometraje_actual.error="Solo se Permite Números"
        validacion=False
    else:
        reparaciones_view.kilometraje_actual.error=None
    
    if not reparaciones_view.siguiente_kilometraje.value:
        reparaciones_view.siguiente_kilometraje.error="Campo Obligatorio"
        validacion=False
    elif not reparaciones_view.siguiente_kilometraje.value.isdigit():
        reparaciones_view.siguiente_kilometraje.error="Solo se Permite Números"
        validacion=False
    else:
        reparaciones_view.siguiente_kilometraje.error=None
        
    if validacion_reparacion and validacion_repuestos:
        validacion = validacion and validacion_reparacion and validacion_repuestos
    else:
        validacion=False
        
    
    return validacion



def guardar_campos_orden_reparacion(id_vehiculo):
    
    fecha_ingreso=reparaciones_view.fecha_entrada.value.strip()
    fecha_salida=reparaciones_view.fecha_entrega.value.strip()
    id_personal=reparaciones_view.personal_encargado.value
    precio_total=reparaciones_view.precio_total_reaparacion.value.strip()
    kilometraje_actual=reparaciones_view.kilometraje_actual.value.strip()
    proximo_kilometraje= reparaciones_view.siguiente_kilometraje.value.strip()
    
    id_orden_rep=reparaciones_db.guardar_orden_reparacion(
        id_vehiculo, fecha_ingreso, fecha_salida, id_personal,
        precio_total, kilometraje_actual, proximo_kilometraje
    )
    return id_orden_rep

def guardar_repuestos_utilizados(id_orden_rep, id_repuesto, id_marca, id_proveedor):
    reparaciones_db.guardar_repuestos_utilizados(id_orden_rep, id_repuesto, id_marca, id_proveedor)
        
def guardar_reparaciones(id_vehiculo):
    if reparaciones_view.vehiculos_view.checkbox_agregar_reparacion.value == True:
        id_orden_rep = guardar_campos_orden_reparacion(id_vehiculo)

        # Cambio: se recorren todos los repuestos guardados.
        repuestos = ctr_cat_veh.guardar_campos_repuestos()

        for id_repuesto, id_marca, id_proveedor in repuestos:
            guardar_repuestos_utilizados(
                id_orden_rep,
                id_repuesto,
                id_marca,
                id_proveedor
            )

        guardar_campos_reparaciones(id_orden_rep)
        guardar_imagenes(id_orden_rep)
def guardar_imagenes(id_orden_reparacion):
    reparaciones_view.guardar_imagenes_vehiculos()
    for ruta in reparaciones_view.nuevas_rutas_imagenes:
        print(ruta)
        reparaciones_db.guardar_rutas_imagenes_veh(id_orden_reparacion, ruta)

def guardar_nueva_orden(e,id_vehiculo):
    guardado=False
    validacion= validacion_general()  
    if validacion == True:
        id_orden_rep=guardar_campos_orden_reparacion(id_vehiculo)
        repuestos = ctr_cat_veh.guardar_campos_repuestos()

        for id_repuesto, id_marca, id_proveedor in repuestos:
            guardar_repuestos_utilizados(
                id_orden_rep,
                id_repuesto,
                id_marca,
                id_proveedor
            )
        guardar_campos_reparaciones(id_orden_rep)
        guardar_imagenes(id_orden_rep)
        guardado= True
        if guardado==True:
            e.page.run_task(save_alert,e)
            limpiar_campos_reparacion()
            e.page.pop_dialog()
            datos=ctr_veh.obtener_datos_vehiculos()
            nuevo_item=datos[id_vehiculo]
            vehiculos_view.cambiar_vista(
                vehiculos_view.detalles_vehiculos(nuevo_item)
            )
        else:
            e.page.run_task(alerta_error,e,"Verifique si los datos ya estan en el sistema")