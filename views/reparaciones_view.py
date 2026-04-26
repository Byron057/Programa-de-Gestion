import flet as ft
from components import *
import datetime as dt
from views import vehiculos_view
import controls.controls_personal as ctr_per
import shutil, os

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
    hint_text="Seleccione el Personal Encargado",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    text="",
    bgcolor=ft.Colors.WHITE,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    ),
    options=[
        ft.dropdown.Option(
            text=f" {p["CEDULA"]} - {p['NOMBRES']} ", style=ft.TextStyle(color="black")
        ) for p in ctr_per.obtener_datos_personal().values()
    ]
)
stack_personal_encargaado=ft.Stack(
        controls=[
            personal_encargado,
            crear_bloqueo_dropdown(300) 
        ]
    )

def validar_text_recio(e):
    valor = e.control.value or ""
    
    if valor == "":
        return

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

    if valor != resultado:
        e.control.value = resultado
        e.control.update()


suffix_precio_reparacion=Text("$", 20, ft.Colors.BLACK)
text_precio_total=Text("Precio Total", 20, ft.Colors.BLACK,"w400")
precio_total_reaparacion=ft.TextField(
    hint_text="25",
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    on_change= lambda e: validar_text_recio(e),
    read_only=False,
    suffix=suffix_precio_reparacion,
    height=50
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
    suffix=suffix_siguiente_kilometraje,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False
)

def actualizar_boton_reparaciones():
    for fila in lista_reparaciones.controls:
        boton=fila.controls[2]
        boton.icon=ft.Icons.DELETE
        boton.bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.RED,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }
    if lista_reparaciones.controls:
            ultima = lista_reparaciones.controls[-1]
            ultima.controls[2].icon = ft.Icons.ADD
            ultima.controls[2].bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }
def crear_campo_reparacion():
    text=ft.TextField(
        hint_text="Detalles de la reparación realizada",
        border_color=ft.Colors.BLACK,
        width=410,
        color=ft.Colors.BLACK,
        read_only=False
    )
    precio=ft.TextField(
        hint_text="Precio",
        border_color=ft.Colors.BLACK,
        width=196,
        height=49,
        color=ft.Colors.BLACK,
        on_change=lambda e: (validar_text_recio(e), calcular_precio_total()),
        keyboard_type=ft.KeyboardType.NUMBER,
        read_only=False,
        suffix=Text("$", 20, ft.Colors.BLACK)
    )
    boton_general=ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
            ft.ControlState.DISABLED: ft.Colors.GREY_400
        }
    )
    fila=ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
        controls=[
            text,
            precio,
            boton_general
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
    
    return fila

def calcular_precio_total():
    precios_recolectados=[]
    for fila in lista_reparaciones.controls[:]:
        precio=fila.controls[1]
        try:
            precio.error=None
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
        boton=fila.controls[3]
        boton.icon=ft.Icons.DELETE
        boton.bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.RED,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    }
    if lista_repuestos.controls:
            ultima = lista_repuestos.controls[-1]
            ultima.controls[3].icon = ft.Icons.ADD
            ultima.controls[3].bgcolor={
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
        options=[
            ft.dropdown.Option(
                text=f" {p["CEDULA"]} - {p['NOMBRES']} ", style=ft.TextStyle(color="black")
            ) for p in ctr_per.obtener_datos_personal().values()#mostrar repuestos registrados
        ]
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
        options=[
            ft.dropdown.Option(
                text=f" {p["CEDULA"]} - {p['NOMBRES']} ", style=ft.TextStyle(color="black")
            ) for p in ctr_per.obtener_datos_personal().values()#mostrar marcas de repuestos regisrados registrados
        ]
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
        options=[
            ft.dropdown.Option(
                text=f" {p["CEDULA"]} - {p['NOMBRES']} ", style=ft.TextStyle(color="black")
            ) for p in ctr_per.obtener_datos_personal().values()#mostrar almacenes registrados
        ]
    )
    boton_general=ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.GREEN_400,
            ft.ControlState.DISABLED: ft.Colors.GREY_400
        }
    )
    
    stack_repuesto=ft.Stack(
        controls=[
            repuesto,
            crear_bloqueo_dropdown(196)
        ]
    )
    stack_marca=ft.Stack(
        controls=[
            marca_repuesto,
            crear_bloqueo_dropdown(196)
        ]
    )
    stack_proovedor=ft.Stack(
        controls=[
            proveedor_repuesto,
            crear_bloqueo_dropdown(196)
        ]
    )
    def acccion_boton(e):
        if boton_general.icon== ft.Icons.ADD:
            lista_repuestos.controls.append(crear_campo_repuestos())
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
            boton_general
        ]
    )
    
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
        print(imagenes_seleccionadas)
    
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
                print(imagenes_seleccionadas)
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
    content=(
        ft.Row(
            controls=[
                lista_imagenes,
                seleccionar_imagen
    
            ]
        )
    ),
)

nuevas_rutas_imagenes=[]
def guardar_imagenes_vehiculos():
    destino_imagenes= os.path.join("assets", "fotos_vehiculos")
    if imagenes_seleccionadas:
        try:
            for ruta in imagenes_seleccionadas:
                nueva_ruta=shutil.copy(ruta,destino_imagenes)
                nuevas_rutas_imagenes.append(nueva_ruta)
        except:
            pass
        print(nuevas_rutas_imagenes)

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
                        stack_personal_encargaado
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