import flet as ft
from components import *
import datetime as dt
from views import vehiculos_view

fecha_actual= dt.datetime.now().strftime('%d/%m/%Y')

def interfaz_checkbox_vehiculos():
    #restablece algunos campos funciona de la misma manera que la funcion de limpiar campos
    fecha_entrada.value=fecha_actual
    fecha_entrega.value=fecha_actual
    kilometraje_actual.value=""
    siguiente_kilometraje.value=""
    
    #desabilitar y habilitar los campos de trabajos
    #ojo faltan algunos campos
    if vehiculos_view.checkbox_agregar_reparacion.value==True:
        #cambiar a la carpeta controls
        text_fecha_entrada.color=ft.Colors.BLACK
        fecha_entrada.color=ft.Colors.BLACK
        calendario_entrada.icon_color=ft.Colors.BLUE_700
        calendario_entrada.disabled=False
        
        text_fecha_entrega.color=ft.Colors.BLACK
        fecha_entrega.color=ft.Colors.BLACK
        calendario_entrega.icon_color=ft.Colors.BLUE_700
        calendario_entrega.disabled=False
        
        suffix_kilometraje_actual.color=ft.Colors.BLACK
        text_kilometraje_actual.color=ft.Colors.BLACK
        kilometraje_actual.color=ft.Colors.BLACK
        kilometraje_actual.read_only= False
        
        suffix_siguiente_kilometraje.color=ft.Colors.BLACK
        text_siguiente_kilometraje.color=ft.Colors.BLACK
        siguiente_kilometraje.color=ft.Colors.BLACK
        siguiente_kilometraje.read_only=False
        
        boton_agregar_reparacion.disabled=False 
        boton_eliminar_reparacion.disabled=False  
        
    else:
        
        text_fecha_entrada.color=ft.Colors.GREY_400
        fecha_entrada.color=ft.Colors.GREY_400
        calendario_entrada.icon_color=ft.Colors.GREY_400
        calendario_entrada.disabled=True
        
        text_fecha_entrega.color=ft.Colors.GREY_400
        fecha_entrega.color=ft.Colors.GREY_400
        calendario_entrega.icon_color=ft.Colors.GREY_400
        calendario_entrega.disabled=True
        
        suffix_kilometraje_actual.color=ft.Colors.GREY_400
        text_kilometraje_actual.color=ft.Colors.GREY_400
        kilometraje_actual.color=ft.Colors.GREY_400
        kilometraje_actual.read_only= True
        
        suffix_siguiente_kilometraje.color=ft.Colors.GREY_400
        text_siguiente_kilometraje.color=ft.Colors.GREY_400
        siguiente_kilometraje.color=ft.Colors.GREY_400
        siguiente_kilometraje.read_only=True

        boton_agregar_reparacion.disabled=True
        boton_eliminar_reparacion.disabled=True


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
    height=50,
    suffix=calendario_entrega,
    value=fecha_actual,
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only=True,
    data="entrega"
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
    read_only=False
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

def agregar_nueva_reparacion():
    #funcion que me permite agregar mas text field para poder agregar mas reparaciones y su costo
    #agregar funcion que permita calcular el total "tambien el precio de repuestos"
    lista_reparaciones_realizadas.controls.append(
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    hint_text="Detalles de la reparación realizada",
                    border_color=ft.Colors.BLACK,
                    color=ft.Colors.BLACK,
                    read_only=False
                ),
                ft.VerticalDivider(),
                ft.TextField(
                    hint_text="25",
                    suffix=suffix_precio_reparacion,
                    color=ft.Colors.BLACK,
                    border_color=ft.Colors.BLACK,
                    read_only=False
                )
            ]
        )
    )
    
    if len(lista_reparaciones_realizadas.controls) > 0:
        boton_eliminar_reparacion.disabled=False


def eliminar_campos_reparaciones():
    #permite eliminar el ultimo campo de reaparacion ademas desabilita el boton de eliminar
    if len(lista_reparaciones_realizadas.controls) > 0:
        boton_eliminar_reparacion.disabled=False
        lista_reparaciones_realizadas.controls.pop(-1)

    if len(lista_reparaciones_realizadas.controls) == 0:
        boton_eliminar_reparacion.disabled=True


def print_prueba():
    #logica de prueba para poder almacenar los datos de las reparaciones y costos en una lista,
    #tiene que recorrer los value y estos agregar en una sola lista ademas de borrarse todo en el apartado de limpiar formulario
    
    print(reaparacion_obligatorio.value)
    for e in lista_reparaciones_realizadas.controls:
        print(e.controls[0].value)

text_reparaciones=Text("Reparaciones Realizadas", 20, ft.Colors.BLACK, "w400")
lista_reparaciones_realizadas=ft.Column()
reaparacion_obligatorio=ft.TextField(
    hint_text="Detalles de la reparación realizada",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False
)

suffix_precio_reparacion=Text("$", 20, ft.Colors.BLACK)
text_precio_reparacion=Text("Precio", 20, ft.Colors.BLACK,"w400")
precio_reaparacion=ft.TextField(
    hint_text="25",
    suffix=suffix_precio_reparacion,
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only=False
)

boton_agregar_reparacion=ft.Button(
    content=Text("Agregar Nueva Reparación", 15, ft.Colors.WHITE, "w500"),
    icon= Icon(ft.Icons.ADD, ft.Colors.WHITE, 25),
    bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.GREEN,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
        
    },
    on_click=lambda e: agregar_nueva_reparacion()
)
boton_eliminar_reparacion=ft.Button(
    content=Text("Eliminar Última Reparación", 15, ft.Colors.WHITE, "w500"),
    icon=Icon(ft.Icons.DELETE, ft.Colors.WHITE, 25),
    bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.RED,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    },
    disabled=True,
    on_click= lambda e: eliminar_campos_reparaciones()
    
    
)

galeria_imagenes_seleccionadas=ft.Row(wrap=True, spacing=10)
async def pick_files(e):
   
    #faltan validaciones para poder guardar en la db, solo se va aguardar la ruta
    #debe crearse una carpeta en la que se guardaran estas imagenes
    
    def eliminar_foto(foto_eliminar):
        galeria_imagenes_seleccionadas.controls.remove(foto_eliminar)
    file_picker=ft.FilePicker()
    
    lista_imagenes= await file_picker.pick_files(allow_multiple=True, file_type=ft.FilePickerFileType.IMAGE)

    if lista_imagenes:
        for i in lista_imagenes:
            tarjeta=ft.Container(
                width=100,
                height=90
            )
            imagen=ft.Image(
                src=i.path,
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
        galeria_imagenes_seleccionadas.controls.append(tarjeta)

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
                        reaparacion_obligatorio,
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_precio_reparacion,
                        precio_reaparacion
                        
                    ]
                )
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                lista_reparaciones_realizadas
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                boton_agregar_reparacion,

                boton_eliminar_reparacion
            ]
        ),
        ft.Container(
            height=100, 
            width=670, 
            border=ft.border.all(1, ft.Colors.BLACK),
            border_radius=30,
            padding=ft.padding.only(left=20,right=20,top=10, bottom=10),
            content=(
                ft.Row(
                    controls=[
                        galeria_imagenes_seleccionadas,
                        ft.Container(
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
                    ]
                )
            ),
        )
    ]
    
)