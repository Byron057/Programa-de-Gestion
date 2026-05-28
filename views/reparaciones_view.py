import flet as ft
from components import *
import datetime as dt
from views import vehiculos_view
import controls.controls_personal as ctr_per
import controls.controls_reparaciones as ctr_rep
import database.reparaciones_db as rep_db
import shutil, os
from config import *

fecha_actual= dt.datetime.now().strftime('%d/%m/%Y')

def abrir_calendario(e, campo_text):
    
    def poner_fecha_en_texto(evt):
        
        if evt.control.value:
            campo_text.value = evt.control.value.strftime('%d/%m/%Y')
    #empíeza asi para poder agregar segun el campo que se ncesite, se puede usar en un futuro
    first_date = None
    last_date = None
    #agrega los limites de fechas segun el data de la variable que almacena el texfield para ingresar la fecha
    if campo_text.data == "entrada":
        first_date = dt.datetime(2026, 1, 1)
        last_date = dt.datetime.now()
    elif campo_text.data == "entrega":
        first_date = dt.datetime.now()
    
    calendario_dinamico = ft.DatePicker(
        on_change=poner_fecha_en_texto,
        locale=ft.Locale("es","ES"),
        cancel_text="Cancelar",
        confirm_text="Confirmar",
        entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
        first_date=first_date,
        last_date=last_date
    )
    
    e.page.overlay.append(calendario_dinamico)
    e.page.update()
    calendario_dinamico.open = True
    e.page.update()

text_fecha_entrada=Text("Fecha de Ingreso", 20, ft.Colors.BLACK, "w400" )

calendario_entrada=ft.IconButton(
    icon=ft.Icons.CALENDAR_MONTH, 
    icon_color=ft.Colors.BLUE_700,
    style=ft.ButtonStyle(
        overlay_color=ft.Colors.BLUE_100
    ),
    disabled=False,
    on_click= lambda e: abrir_calendario(e, fecha_entrada)
)
fecha_entrada= ft.TextField(
    hint_text="DD/MM/YYYY",
    height=50,
    value= fecha_actual,
    suffix=calendario_entrada,
    color= ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only= True,
    data="entrada"
)

text_fecha_entrega=Text("Fecha de Entrega", 20, ft.Colors.BLACK, "w400")
calendario_entrega=ft.IconButton(
    icon=ft.Icons.CALENDAR_MONTH, 
    icon_color=ft.Colors.BLUE_700,
    style=ft.ButtonStyle(
        overlay_color=ft.Colors.BLUE_100
    ),
    disabled=False,
    on_click= lambda e: abrir_calendario(e, fecha_entrega)
)
fecha_entrega=ft.TextField(
    hint_text="DD/MM/YYYY",
    height=49,
    suffix=calendario_entrega,
    value=fecha_actual,
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only=True,
    data="entrega"
)


def crear_bloqueo_dropdown(width):
    return  ft.Container(
            width=width,
            height=48, 
            bgcolor=ft.Colors.TRANSPARENT,
            on_click=lambda e: None, 
            visible=False 
        )
text_personal_encargado=Text("Personal Encargado", 20, ft.Colors.BLACK, "400")
personal_encargado= ft.Dropdown(
    width=300,
    content_padding=10,
    hint_text="Seleccione el Personal Encargado",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
stack_personal_encargado=ft.Stack(
        controls=[
            personal_encargado,
            crear_bloqueo_dropdown(300) 
        ]
    )

def validar_text_precio(e):
    valor = e.control.value or ""

    resultado = ""
    punto_usado = False

    for c in valor:
        if c.isdigit():
            resultado += c
        elif c == "." and not punto_usado:
            resultado += c
            punto_usado = True

    if "." in resultado:
        parte_entera, parte_decimal = resultado.split(".", 1)
        resultado = parte_entera + "." + parte_decimal[:2]

    if e.control.value != resultado:
        e.control.value = resultado
        e.control.update()


suffix_precio_reparacion=Text("$", 18, ft.Colors.BLACK)
text_precio_total=Text("Precio Total", 20, ft.Colors.BLACK,"w400")
precio_total_reaparacion=ft.TextField(
    hint_text="25",
    content_padding=13,
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    on_change= lambda e: validar_text_precio(e),
    read_only=False,
    suffix=suffix_precio_reparacion,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)

def calcular_kilometraje():
    #funcion que me permite calcular automaticamente el proximo km sumandole el estandar que es 5000
    valor_ingresado= kilometraje_actual.value
    if valor_ingresado == "":
        siguiente_kilometraje.value=""
        return
    
    try:
        km_actual = int(valor_ingresado)
        km_calculado = km_actual + 5000
        
        siguiente_kilometraje.value = str(km_calculado)
    except ValueError:
        #permite que no me salte ningun error y se cierre el programa
        #añadir en mensaje de error para que se ingresen correctamente los diferentes campos
        pass
    
suffix_kilometraje_actual=Text("km", 20, ft.Colors.BLACK)
text_kilometraje_actual=Text("Kilometraje Actual", 20, ft.Colors.BLACK, "w400")
kilometraje_actual=ft.TextField(
    hint_text="10005",
    content_padding=10,
    on_change=calcular_kilometraje,
    suffix=suffix_kilometraje_actual,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)

suffix_siguiente_kilometraje=Text("km", 20, ft.Colors.BLACK)
text_siguiente_kilometraje =Text("Siguiente Kilometraje", 20 ,ft.Colors.BLACK, "w400")
siguiente_kilometraje=ft.TextField(
    hint_text="15005",
    content_padding=10,
    suffix=suffix_siguiente_kilometraje,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)

def actualizar_boton_reparaciones():
    for fila in lista_reparaciones.controls:
        boton=fila.data["boton"]
        boton.icon=ft.Icons.DELETE
        boton.bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.RED,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }
    if lista_reparaciones.controls:
            ultima = lista_reparaciones.controls[-1]
            ultima.controls[2].controls[0].icon = ft.Icons.ADD
            ultima.controls[2].controls[0].bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }
def crear_campo_reparacion():
    reparacion=ft.TextField(
        hint_text="Detalles de la reparación realizada",
        border_color=ft.Colors.BLACK,
        width=410,
        content_padding=10,
        color=ft.Colors.BLACK,
        read_only=False,
        error_style=ft.TextStyle(
            color=ft.Colors.RED_ACCENT_700,
            weight=ft.FontWeight.W_500,
            font_family="Roboto-Medium"
        )
    )
    precio=ft.TextField(
        hint_text="Precio",
        border_color=ft.Colors.BLACK,
        width=196,
        color=ft.Colors.BLACK,
        on_change=lambda e: (validar_text_precio(e), calcular_precio_total()),
        keyboard_type=ft.KeyboardType.NUMBER,
        read_only=False,
        suffix=Text("$", 18, ft.Colors.BLACK),
        content_padding=10,
        error_style=ft.TextStyle(
            color=ft.Colors.RED_ACCENT_700,
            weight=ft.FontWeight.W_500,
            font_family="Roboto-Medium"
        )
    )
    boton_general=ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
            ft.ControlState.DISABLED: ft.Colors.GREY_400
        }
    )
    def crear_espacio(width, height):
        return ft.Container(
            width=width,
            height=height,
            bgcolor=ft.Colors.TRANSPARENT,
            visible=False,
        )
    stack_reparacion=ft.Column(
        controls=[
            reparacion,
            crear_espacio(410, 10)
        ]
    )
    stack_precio=ft.Column(
        controls=[
            precio,
            crear_espacio(196, 10)
        ]
    )
    column_icon=ft.Column(
        spacing=9,
        controls=[
            boton_general,
            crear_espacio(40,10)
        ]
    )
    
    fila=ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
        controls=[
            stack_reparacion,
            stack_precio,
            column_icon
        ]
    )
 
        
    def acccion_boton(e):
        if boton_general.icon == ft.Icons.ADD:
            lista_reparaciones.controls.append(crear_campo_reparacion())
        else:
            if len(lista_reparaciones.controls) > 1:
                lista_reparaciones.controls.remove(fila)
                calcular_precio_total()
        actualizar_boton_reparaciones()
    
    boton_general.on_click=acccion_boton
    
    fila.data={
        "reparacion": reparacion,
        "precio": precio,
        "boton": boton_general,
        
        "espacio_reparacion": stack_reparacion.controls[1],
        "espacio_precio": stack_precio.controls[1],
        "espacio_boton": column_icon.controls[1]
    }
    
    return fila

def calcular_precio_total():
    precios_recolectados=[]
    for fila in lista_reparaciones.controls[:]:
        precio=fila.data["precio"]
        try:
            if precio.value != "":
                precios_recolectados.append(float(precio.value))
        except:
            pass
    suma_total=sum(precios_recolectados)
    if suma_total != 0:
        if suma_total.is_integer():
            precio_total_reaparacion.value=str(int(suma_total))
        else:  
            precio_total_reaparacion.value=f"{suma_total:.2f}"
    else:
        precio_total_reaparacion.value=""
    

def actualizar_boton_repuestos():
    for fila in lista_repuestos.controls:
        boton=fila.controls[3].controls[0]
        boton.icon=ft.Icons.DELETE
        boton.bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.RED,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }
    if lista_repuestos.controls:
            ultima = lista_repuestos.controls[-1]
            ultima.controls[3].controls[0].icon = ft.Icons.ADD
            ultima.controls[3].controls[0].bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }

def crear_campo_repuestos():
    
    repuesto=ft.Dropdown(
        width=196,
        editable=True,
        enable_filter=True,
        hint_text="Repuesto",
        border_color=ft.Colors.BLACK,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        error_style=ft.TextStyle(
            color=ft.Colors.RED_ACCENT_700,
            weight=ft.FontWeight.W_500,
            font_family="Roboto-Medium"
        ),
        capitalization=ft.TextCapitalization.WORDS,
        on_text_change= limpiar_key_al_cambiar
    )
    marca_repuesto=ft.Dropdown(
        width=196,
        editable=True,
        enable_filter=True,
        hint_text="Marca",
        border_color=ft.Colors.BLACK,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        error_style=ft.TextStyle(
            color=ft.Colors.RED_ACCENT_700,
            weight=ft.FontWeight.W_500,
            font_family="Roboto-Medium"
        ),
        
        capitalization=ft.TextCapitalization.WORDS,
        on_text_change= limpiar_key_al_cambiar
    )
    proveedor_repuesto=ft.Dropdown(
        width=196,
        editable=True,
        enable_filter=True,
        hint_text="Proveedor",
        border_color=ft.Colors.BLACK,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.WHITE,
        error_style=ft.TextStyle(
            color=ft.Colors.RED_ACCENT_700,
            weight=ft.FontWeight.W_500,
            font_family="Roboto-Medium"
        ),
        capitalization=ft.TextCapitalization.WORDS,
        on_text_change= limpiar_key_al_cambiar
    )
    boton_general=ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
            ft.ControlState.DISABLED: ft.Colors.GREY_400
        }
    )
    def crear_espacio(width, height):
        return ft.Container(
            width=width,
            height=height,
            bgcolor=ft.Colors.TRANSPARENT,
            visible=False,
        )
    
    stack_repuesto=ft.Column(
        controls=[
            ft.Stack(
                controls=[
                repuesto,
                crear_bloqueo_dropdown(196)
                ]
            ),
            crear_espacio(196,10)
        ]
    )
    stack_marca=ft.Column(
        controls=[
            ft.Stack(
                controls=[
                marca_repuesto,
                crear_bloqueo_dropdown(196)
                ]
            ),
            crear_espacio(196,10)
        ]
    )
    stack_proovedor=ft.Column(
        controls=[
            ft.Stack(
                controls=[
                proveedor_repuesto,
                crear_bloqueo_dropdown(196)
                ]
            ),
            crear_espacio(196,10)
        ]
    )
    column_icon=ft.Column(
        spacing=9,
        controls=[
            boton_general,
            crear_espacio(40,10)
        ]
    )
    def acccion_boton(e):
        if boton_general.icon== ft.Icons.ADD:
            lista_repuestos.controls.append(crear_campo_repuestos())
            vehiculos_view.cargar_catalogos()
        else:
            if len(lista_repuestos.controls) > 1:
                lista_repuestos.controls.remove(fila)
        actualizar_boton_repuestos()
    
    boton_general.on_click=acccion_boton
    fila=ft.Row(
        spacing=15,
        controls=[
            stack_repuesto,
            stack_marca,
            stack_proovedor,
            column_icon
        ]
    )
    fila.data = {
    "repuesto": repuesto,
    "marca": marca_repuesto,
    "proveedor": proveedor_repuesto,
    "boton": boton_general,
    
    "bloqueo_repuesto": stack_repuesto.controls[0].controls[1],
    "bloqueo_marca": stack_marca.controls[0].controls[1],
    "bloqueo_proveedor": stack_proovedor.controls[0].controls[1],
    
    "espacio_repuesto": stack_repuesto.controls[1],
    "espacio_marca": stack_marca.controls[1],
    "espacio_proveedor": stack_proovedor.controls[1],
    "espacio_boton": column_icon.controls[1]
    }   
    return fila 

text_reparaciones=Text("Reparaciones Realizadas", 20, ft.Colors.BLACK, "w400")
text_repuestos=Text("Repuestos Utilizados", 20, ft.Colors.BLACK, "w400")

lista_reparaciones=ft.Column(spacing=10)
lista_reparaciones.controls.append(crear_campo_reparacion())
actualizar_boton_reparaciones()

lista_repuestos=ft.Column()
lista_repuestos.controls.append(crear_campo_repuestos())
actualizar_boton_repuestos()

text_galeria=Text("Estado del Vehículo ", 20, ft.Colors.BLACK, "w400")
lista_imagenes=ft.Row(spacing=10)

def construir_galeria(ruta):
    def eliminar_foto(foto_eliminar):
        lista_imagenes.controls.remove(foto_eliminar)
        imagenes_seleccionadas.remove(foto_eliminar.data)
    
    tarjeta=ft.Container(
        width=100,
        height=90,
        data=ruta
    )
    imagen=ft.Image(
        src=ruta,
        width=100,
        height=80,
        fit=ft.BoxFit.COVER,
        border_radius=5
        
    )
    boton_x=ft.Container(
        content=ft.IconButton(
            icon=ft.Icons.CANCEL,
            icon_color=ft.Colors.RED,
            on_click=lambda e, t=tarjeta: eliminar_foto(t),
        )
    )
    tarjeta.content=ft.Stack([imagen, boton_x])
    lista_imagenes.controls.append(tarjeta)

imagenes_seleccionadas=[]
async def pick_files(e):
       
    file_picker=ft.FilePicker()
    lista_imagenes_seleccionadas= await file_picker.pick_files(allow_multiple=True, file_type=ft.FilePickerFileType.IMAGE)

    if lista_imagenes_seleccionadas:
        for i in lista_imagenes_seleccionadas:
            if not i.path in imagenes_seleccionadas:
                imagenes_seleccionadas.append(i.path)
                construir_galeria(i.path)
            lista_imagenes.update()

seleccionar_imagen=ft.Container(
    width=50,
    height=90,
    bgcolor=ft.Colors.GREY_200,
    border_radius=5,
    alignment=ft.Alignment.CENTER_LEFT,
    content=(
        Icon(ft.Icons.UPLOAD_FILE, ft.Colors.GREY_400, 30)
    ),
    on_click= pick_files
)
galeria_imagenes=ft.Container(
    height=100, 
    width=670, 
    border=ft.border.all(1, ft.Colors.BLACK),
    border_radius=30,
    padding=ft.padding.only(left=20,right=20,top=10, bottom=10),
    clip_behavior=ft.ClipBehavior.HARD_EDGE,
    content=(
        ft.Row(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                lista_imagenes,
                seleccionar_imagen
    
            ]
        )
    ),
)

nuevas_rutas_imagenes=[]
def guardar_imagenes_vehiculos():

    global nuevas_rutas_imagenes

    nuevas_rutas_imagenes.clear()

    if not imagenes_seleccionadas:
        return

    for ruta in imagenes_seleccionadas:

        try:

            nombre_archivo = os.path.basename(ruta)

            ruta_destino = os.path.join(
                RUTA_FOTOS_VEHICULOS,
                nombre_archivo
            )

            try:

                shutil.copy(
                    ruta,
                    ruta_destino
                )

            except shutil.SameFileError:
                pass

            nuevas_rutas_imagenes.append(
                ruta_destino
            )

        except Exception as e:

            print(
                f"Error guardando imagen: {e}"
            )

formulario_reparaciones=ft.Column(
    #aqui se agregan los campos necesarios para poder registrar nuevas reparaciones, 
    #asignado en una variable diferente para poder agregar en un alert dialog
    expand=True,
    controls=[
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_fecha_entrada,
                        ft.Row(
                            controls=[
                                fecha_entrada
                            ]
                        )
                        
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_fecha_entrega,
                        ft.Row(
                            controls=[
                                fecha_entrega
                            ]
                        )
                        
                    ]
                )
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_personal_encargado,
                        stack_personal_encargado
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_precio_total,
                        precio_total_reaparacion
                    ]
                )
                
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_kilometraje_actual,
                        kilometraje_actual
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_siguiente_kilometraje,
                        siguiente_kilometraje
                    ]
                )
                
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_reparaciones,
                        lista_reparaciones
                    ]
                )
            ]
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_repuestos,
                        lista_repuestos
                    ]
                )
            ]
            ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[   
                        text_galeria,
                        galeria_imagenes
                    ]
                )
            ]
        )
    ]
    
)

def registrar_nueva_orden(e, id_vehiculo):
    seleccionar_imagen.bgcolor=ft.Colors.WHITE
    boton_cancelar= ft.Button(
        content=Text("Cancelar",20, ft.Colors.BLACK),
        bgcolor=ft.Colors.GREY_300,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
        on_click=lambda e: [e.page.pop_dialog(),ctr_rep.limpiar_campos_reparacion()]
    )
    boton_guardar=ft.Button(
        content=Text("Guardar", 20, ft.Colors.WHITE),
        disabled=False,
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DISABLED: ft.Colors.GREY_400, 
                ft.ControlState.DEFAULT: ft.Colors.BLUE_700   
            },
            color={
                ft.ControlState.DISABLED: ft.Colors.GREY_600, 
                ft.ControlState.DEFAULT: ft.Colors.WHITE      
            },
            shape=ft.RoundedRectangleBorder(radius=1)
        ),
        on_click= lambda e: ctr_rep.guardar_nueva_orden(e,id_vehiculo)
    )
    formulario_global=e.page.show_dialog(
        ft.AlertDialog(
            modal=True,
            open=True,
            bgcolor=ft.Colors.WHITE,
            content= ft.Column(
                width=720,
                height=540,
                scroll=ft.ScrollMode.AUTO,
                controls= [
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                            "Nueva Reparacion",
                            size=30,
                            weight="w500",
                            color=ft.Colors.BLACK
                            )
                        ]
                    ),
                    formulario_reparaciones,
                    ft.Divider(color=ft.Colors.TRANSPARENT),
                    ft.Container(
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                boton_cancelar,
                                boton_guardar
                            ]
                        )
                    )  
                ]
            )
        )
    )
    return formulario_global

def detalles_reparaciones(e,orden):
    
    def campo(icono, titulo, valor):
        return ft.Container(
            expand=True,
            padding=12,
            border_radius=12,
            bgcolor=ft.Colors.GREY_100,
            border=ft.border.all(1, ft.Colors.GREY_300),
            content=ft.Row(
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=35,
                        height=35,
                        border_radius=8,
                        bgcolor=ft.Colors.BLUE_100,
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(icono, size=18, color=ft.Colors.BLUE_700)
                    ),
                    ft.Column(
                        spacing=2,
                        expand=True,
                        controls=[
                            Text(titulo, 12, ft.Colors.BLACK),
                            Text(valor, 16, ft.Colors.GREY_600 ,"bold")
                        ]
                    )
                ]
            )
        )
    
    datos = ft.Column(
        spacing=12,
        controls=[
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.CALENDAR_MONTH, "Fecha Ingreso", orden["FECHA_INGRESO"]),
                    campo(ft.Icons.EVENT, "Fecha Entrega", orden["FECHA_SALIDA"])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.PERSON, "Personal Encargado", orden["PERSONAL_ENCARGADO"]["NOMBRES"]),
                    campo(ft.Icons.ATTACH_MONEY, "Precio Total", f"${orden['PRECIO_TOTAL']}")
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.STRAIGHTEN, "Kilometraje Actual", f"{orden['KILOMETRAJE_ACTUAL']} km"),
                    campo(ft.Icons.ROUTE, "Siguiente KM", f"{orden['PROXIMO_KILOMETRAJE']} km")
                ]
            )
        ]
    )
    
    def lista_reparaciones_realizadas(orden):

        lista = ft.Column(
            spacing=8
        )

        for rr in orden["REPARACIONES_REALIZADAS"]:
            item=ft.Row(
            spacing=12,
            expand=True,
            controls=[
                ft.Container(
                    padding=10,
                    border_radius=8,
                    width=600,
                    bgcolor=ft.Colors.GREY_100,
                    border=ft.border.all(1, ft.Colors.GREY_300),

                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # ← centrar ícono
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                expand=True,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10,
                                controls=[
                                    ft.Icon(
                                        ft.Icons.BUILD,
                                        color=ft.Colors.BLUE_700
                                    ),
                                    ft.Text(
                                        rr["REPARACION"],
                                        color=ft.Colors.BLACK,
                                        size=16,
                                        expand=True
                                    )
                                ]
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=10,
                    border_radius=8,
                    bgcolor=ft.Colors.GREY_100,
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    width=107,

                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            ft.Text(
                                f"${rr['PRECIO']}",
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                                expand=True
                            )
                        ]
                    )
                )
            ]
        )
            lista.controls.append(item)

        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Reparaciones Realizadas",
                    size=20,
                    weight="w500",
                    color=ft.Colors.BLACK
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            "Reparacion",
                            size=20,
                            color=ft.Colors.BLACK
                        ),
                        ft.Container(width=492),
                        ft.Text(
                            "Precio",
                            size=20,
                            color=ft.Colors.BLACK
                        )
                    ]
                ),
                lista
            ]
        )
    def lista_repuestos_utilizados(orden):
        lista = ft.Column(
            spacing=8
        )

        for rr in orden["REPUESTOS_UTILIZADOS"]:
            item=ft.Row(
            spacing=12,
            expand=True,
            controls=[
                ft.Container(
                    padding=10,
                    border_radius=8,
                    width=232,
                    bgcolor=ft.Colors.GREY_100,
                    border=ft.border.all(1, ft.Colors.GREY_300),

                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  # ← centrar ícono
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                expand=True,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                                alignment=ft.MainAxisAlignment.START,
                                spacing=10,
                                controls=[
                                    ft.Text(
                                        rr["REPUESTO"],
                                        color=ft.Colors.BLACK,
                                        size=16,
                                        expand=True
                                    )
                                ]
                            ),
                        ]
                    )
                ),
                ft.Container(
                    padding=10,
                    border_radius=8,
                    bgcolor=ft.Colors.GREY_100,
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    width=232,

                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            ft.Text(
                                f"{rr['MARCA_REPUESTO']}",
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                                expand=True
                            )
                        ]
                    )
                ),
                ft.Container(
                    padding=10,
                    border_radius=8,
                    bgcolor=ft.Colors.GREY_100,
                    border=ft.border.all(1, ft.Colors.GREY_300),
                    width=232,

                    content=ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,  
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[
                            ft.Text(
                                f"{rr['PROVEEDOR']}",
                                weight=ft.FontWeight.W_500,
                                color=ft.Colors.BLACK,
                                expand=True
                            )
                        ]
                    )
                )
            ]
        )
            lista.controls.append(item)
        if not orden["REPUESTOS_UTILIZADOS"]:
            return ft.Column()
        else:
            return ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Repuestos Utilizados",
                        size=20,
                        weight="w500",
                        color=ft.Colors.BLACK
                    ),
                    ft.Row(
                        controls=[
                            ft.Text(
                                "Repuesto",
                                size=20,
                                color=ft.Colors.BLACK
                            ),
                            ft.Container(width=140),
                            ft.Text(
                                "Marca",
                                size=20,
                                color=ft.Colors.BLACK
                            ),
                            ft.Container(width=170),
                            ft.Text(
                                "Proveedor",
                                size=20,
                                color=ft.Colors.BLACK
                            )
                        ]
                    ),
                    lista
                ]
            )
    def lista_imagenes(orden):

        lista = ft.GridView(
            expand=False,
            runs_count=3,
            max_extent=180,
            child_aspect_ratio=1.0,
            spacing=12,
            run_spacing=12
        )

        for img in orden["RUTAS_IMAGENES"]:

            ruta = img["RUTA_IMAGEN"]

            if not ruta or not os.path.exists(ruta):
                continue

            item = ft.Container(
                width=180,
                height=180,
                border_radius=10,
                border=ft.border.all(1, ft.Colors.GREY_300),
                clip_behavior=ft.ClipBehavior.HARD_EDGE,

                content=ft.Image(
                    src=ruta
                )
            )

            lista.controls.append(item)

        # Si no hay imágenes válidas
        if len(lista.controls) == 0:
            return ft.Column()

        else:
            return ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        "Imagenes de la Reparacion",
                        size=20,
                        weight="w500",
                        color=ft.Colors.BLACK
                    ),
                    lista
                ]
            )
    return e.page.show_dialog(
        ft.AlertDialog(
            modal=True,
            open=True,
            bgcolor=ft.Colors.WHITE,
            content= ft.Column(
                width=720,
                expand=True,
                controls= [
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Detalles de la Orden de  Reparacion",
                                size=25,
                                weight="w500",
                                color=ft.Colors.BLACK
                            ),
                        ]
                    ),
                ft.Container(
                        expand=True,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            controls=[

                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Container(
                                            width=150,
                                            height=160,
                                            border_radius=10,
                                            alignment=ft.Alignment.CENTER,
                                            content=ft.Icon(
                                                ft.Icons.ASSIGNMENT,
                                                size=150,
                                                color=ft.Colors.GREY_400
                                            )
                                        )
                                    ]
                                ),
                                datos,
                                lista_reparaciones_realizadas(orden),
                                lista_repuestos_utilizados(orden),
                                lista_imagenes(orden)
                            ]
                        )
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.Button(
                                content=Text("Regresar",20, ft.Colors.BLACK),
                                bgcolor=ft.Colors.GREY_300,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
                                on_click=lambda e: [e.page.pop_dialog()]
                            )
                        ] 
                    )
                ]
            )
        )
    )

def hitorial_reparaciones(item):
    
    def crear_tarjeta_orden(orden):
        fecha_ingreso=orden["FECHA_INGRESO"]
        precio_total=orden["PRECIO_TOTAL"]
        kilometraje=orden["KILOMETRAJE_ACTUAL"]
        nombre_personal=orden["PERSONAL_ENCARGADO"]["NOMBRES"]
        return ft.Card(
            elevation=5,
            shadow_color=ft.Colors.WHITE,
            content=ft.Container(
                bgcolor=ft.Colors.GREY_100,
                padding=3,
                border=ft.border.all(2, ft.Colors.BLACK),
                border_radius=10,
                content=ft.ListTile(
                    leading=ft.Icon(icon=ft.Icons.BUILD, size=50),
                    title=ft.Text(
                    value=f"{fecha_ingreso}",
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_500
                    ),
                    subtitle=ft.Text(
                        value=f" Encargado: {nombre_personal}     Precio: ${precio_total}      Kilometraje: {kilometraje}Km " ,
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.W_400
                    ),
                    bgcolor=ft.Colors.GREY_100,
                    on_click= lambda e: detalles_reparaciones(e,orden)
                )
            )
        )
    def historial_reparaciones_registradas(item):
        lista_historial_reparaciones=ft.Column()
        sin_historial=ft.Text(
            "No Existen Ordenes De Reparaciones Registradas",
            size=20,
            color=ft.Colors.GREY_400
        )
        if item["ORDEN_REPARACION"]:
            for orden in item["ORDEN_REPARACION"]:
                orden_reparacion=crear_tarjeta_orden(orden)
                lista_historial_reparaciones.controls.append(orden_reparacion)
        else:
            lista_historial_reparaciones.controls.append(sin_historial)  
        return ft.Column(
            expand=True,
            controls=[
                lista_historial_reparaciones
            ]
        )
    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "Historial de Reparaciones",
                size=25,
                weight="w500",
                color=ft.Colors.BLACK,
            ),
            ft.Divider(),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ft.Button(
                        Text("Agregar Nuevo Reparacion", color=ft.Colors.WHITE),
                        Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                        bgcolor=ft.Colors.BLUE_700,
                        on_click= lambda e: registrar_nueva_orden(e, item["id_vehiculo"])
                        )
                ],
            ),
            historial_reparaciones_registradas(item)
        ]
    )