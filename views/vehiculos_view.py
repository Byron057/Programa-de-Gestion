import flet as ft
from components import *
from views import *
import json
import datetime as dt
import os
from controls import controls_catalogos_vehiculos as ctr_cat_veh
from controls import controls_vehiculos as ctr_veh
from controls import controls_reparaciones as ctr_rep
from views import reparaciones_view 
from views import clientes_view

#variable que se edita para poder cambbiar entre pantalla sin modificar la barra superior o las notificacioes
pantalla_vehiculos=ft.Column(expand=True)

def validar_dropdown():
    if not propietario_vehiculo.text:
        propietario_vehiculo.value=None
        #permite borrar los datos para las validaciones, aun no se ha comprobado si existe algun error
        propietario_vehiculo.text=None


def cargar_catalogos():
    #carga los datos de todos los dropdown ademas permite actualizar si exite nuevos registros
    marca_vehiculo.options=[
        ft.dropdown.Option(
            text=m[1], style=(ft.TextStyle(color="black"))
        ) for m in ctr_cat_veh.mostrar_marcas()
    ]
    color_vehiculo.options=[
        ft.dropdown.Option(
            text=c[1], style=(ft.TextStyle(color="black"))
        ) for c in ctr_cat_veh.mostrar_colores()
    ]
    tipo_vehiculo.options=[
        ft.dropdown.Option(
            text=t[1], style=(ft.TextStyle(color="black"))
        ) for t in ctr_cat_veh.mostrar_tipos_vehiculos()
    ]
    propietario_vehiculo.options=[
        ft.dropdown.Option(
            key=c["id_cliente"], text=f"{c['CEDULA']} - {c['APELLIDOS']} {c['NOMBRES']}", style=(ft.TextStyle(color="black"))
        ) for c in ctr_cat_veh.mostrar_clientes().values()
    ]

def cambiar_vista(nueva_vista):
    cargar_catalogos()
    ctr_veh.limpiar_formulario()
    ctr_rep.interfaz_checkbox_vehiculos()
    reparaciones_view.guardar_imagenes_vehiculos()
    pantalla_vehiculos.controls.clear()
    pantalla_vehiculos.controls.append(nueva_vista)
    pantalla_vehiculos.update()    
#variables que se usan para la interfax el formulario del vehiculo
boton_cancelar= ft.Button(
    content=Text("Cancelar",20, ft.Colors.BLACK),
    bgcolor=ft.Colors.GREY_300,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1))
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
    on_click= lambda e:[ ctr_veh.guardar_datos_vehiculos(e)]
)
marca_vehiculo= ft.Dropdown(
    width=300,
    hint_text="Seleccione una Marca de un Vehiculo",
    border_color=ft.Colors.BLACK,
    text="",
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    editable=True,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    ),
    on_select= lambda e: ctr_cat_veh.marca_change(e),
    on_blur= lambda e: ctr_cat_veh.marca_change(e)

)
modelo_vehiculo= ft.Dropdown(
    width=300,
    hint_text="Seleccione un Modelo de un Vehiculo",
    text="",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    editable= True,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    ),
    
)
placa_vehiculo=ft.TextField(
    hint_text="Ejemplo ABC-1234",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
año_vehiculo=ft.TextField(
    hint_text="Ejemplo: 2007",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    keyboard_type=ft.KeyboardType.NUMBER,
    max_length= 4,
    counter_style=(ft.TextStyle(size=0)),
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
tipo_vehiculo=ft.Dropdown(
    width=300,
    hint_text="Seleccione el Tipo de Vehiculo",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    text="",
    bgcolor=ft.Colors.WHITE,
    editable=True,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
    
)
color_vehiculo=ft.Dropdown(
    width=300,
    menu_height=220,
    hint_text="Selecione el Color del Vehiculo",
    text="",
    editable=True,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
propietario_vehiculo=ft.Dropdown(
    width=580,
    menu_height=180,
    hint_text="Seleccione el propietario del vehiculo o registre un nuevo propietario",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    editable=True,
    enable_filter=True,
    on_blur= lambda e: validar_dropdown(),
    bgcolor=ft.Colors.WHITE,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
boton_nuevo_cliente=ft.Button(
    Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
    bgcolor=ft.Colors.BLUE_700,
    on_click= lambda e: clientes_view.form_global_clientes(e)
)

#se separo para poder mostrar o no en el formulario
estado_veh=ft.Row(
    spacing=30,
    alignment=ft.MainAxisAlignment.CENTER,
    controls=[
        Text("Estado del Vehículo", 20, ft.Colors.BLACK, "w400"),
        ft.VerticalDivider(),
        ft.Container(width=420)
    ]
)
checkbox_agregar_reparacion=ft.Checkbox(
    label="Registrar una Reparación",
    value=True,
    label_style=ft.TextStyle(color=ft.Colors.BLACK),
    border_side=ft.BorderSide(2,ft.Colors.BLACK),
    on_change=ctr_rep.interfaz_checkbox_vehiculos
)
row_chekbox=ft.Row(
    spacing=30,
    alignment=ft.MainAxisAlignment.CENTER,
    controls=[
        checkbox_agregar_reparacion,
        ft.VerticalDivider(),
        ft.Container(width=420)
    ]
)
#formulario principal 
formulario_vehiculos=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
            expand=True,
            controls=[
                Text("Datos del Vehículo", 30, ft.Colors.BLACK, "w500"),
                ft.Row(
                    spacing=30,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                Text("Marca del Vehículo", 20, ft.Colors.BLACK, "400"),
                                marca_vehiculo
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Modelos de los Vehiculos", 20, ft.Colors.BLACK, "w400"),
                                modelo_vehiculo
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
                                Text("Placa del Vehículo", 20, ft.Colors.BLACK, "w400"),
                                placa_vehiculo
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Año del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                año_vehiculo
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
                                Text("Tipo Del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                tipo_vehiculo
                            ]
                        ),
                        ft.VerticalDivider(), 
                        ft.Column(
                            controls=[
                                Text("Color del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                color_vehiculo
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
                                Text("Propietario del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                propietario_vehiculo
                            ]
                        ),
                        ft.Column(
                            controls=[
                                Text("", 20, ft.Colors.BLACK, "w400"),
                                boton_nuevo_cliente
                            ]
                        )
                    ]
                ),
                estado_veh,
                row_chekbox
            ]
        )

def agregar_vehículo():
    #actualiza las interacciones de los botones para poder reutilizar
    boton_cancelar.on_click= lambda e: cambiar_vista(listado_vehiculos())
    boton_guardar.on_click= lambda e: ctr_veh.guardar_datos_vehiculos(e)
    estado_veh.visible=True
    row_chekbox.visible=True
    #aqui va lo principal que se necesita en el apartado de agregar un vehiculo, tal vez se modifique un poco para que sea mas estetico
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                Text("Registrar Nuevo Vehículo", 35, ft.Colors.BLACK, "w500" ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[
                        ft.Container(
                            bgcolor=ft.Colors.GREY_200,
                            width=800,
                            height=1000,
                            padding=15,
                            border_radius=15,
                            shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
                            content=(
                                ft.Column(
                                    scroll=ft.ScrollMode.AUTO,
                                    expand=True,
                                    controls=[
                                        formulario_vehiculos,
                                        reparaciones_view.formulario_reparaciones
                                    ]
                                )
                            )
                        )
                    ]
                ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        boton_cancelar,
                        boton_guardar
                    ]
                ) 
            ]
        )
    )


def crear_tarjeta(item):
    cedula= item["PROPIETARIO"][0]["CEDULA"] if item["PROPIETARIO"] else "Sin Popietario"
    return ft.Card(
        elevation=5,
        shadow_color=ft.Colors.WHITE,
        content=ft.Container(
            bgcolor=ft.Colors.GREY_100,
            padding=3,
            border=ft.border.all(2, ft.Colors.BLACK),
            border_radius=10,
            content=ft.ListTile(
                leading=ft.Icon(icon=ft.Icons.CAR_REPAIR, size=50),
                title=ft.Text(
                value=f"{item['PLACA']}",
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_500
                ),
                subtitle=ft.Text(
                    value=f"Marca: {item['MARCA']}    Modelo: {item['MODELO']}    Propietario: {cedula}",
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_400
                ),
                bgcolor=ft.Colors.GREY_100,
                on_click= lambda e: cambiar_vista(detalles_vehiculos(item))
            )
        )
)

def tabla_vehiculos_registrados():
     
    datos=ctr_veh.obtener_datos_vehiculos()
    
    lista_resultados=ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
    
    def actualizar_lista(e=None):
        busqueda=barra_busqueda.value.lower().strip()
        lista_resultados.controls.clear()
        for vehiculo in datos.values():
            if busqueda == "":
                nueva_tarjeta=crear_tarjeta(vehiculo)
                lista_resultados.controls.append(nueva_tarjeta)
                
    barra_busqueda= ft.TextField(
        width=600,
        border_radius=15,
        hint_text="Busqueda por Nombre o  Número de Cedula",
        prefix_icon=ft.Icons.SEARCH,
        on_change=actualizar_lista,
        border_color=ft.Colors.BLACK,
        color=ft.Colors.BLACK
    )
    tabla_principal= ft.Container(
        width=950,
        expand=True,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        barra_busqueda,
                    ]
                ),
                lista_resultados
            ]
        )
    )
    
    actualizar_lista()
    
    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                tabla_principal
            ]
        )
    )

def detalles_vehiculos(item):
    #agregaraui el historial de reparaciones, una tarjeta por cada reparacion en la que me va a salir la info
    #agregar una busuqeda por fecha
    
    global id_actual_veh
    id_actual_veh=item["id_vehiculo"]
    boton_editar=ft.Button(
        content=Text("Editar", 20, ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_600,
        on_click= lambda e: editar_veh(e,item)
    )
    boton_eliminar=ft.Button(
        content=Text("Eliminar", 20, ft.Colors.WHITE),
        bgcolor=ft.Colors.RED_700,
        on_click=lambda e: print(e)
    )
    imagen = ft.Container(
        width=150,
        height=160,
        border_radius=10,
        alignment=ft.Alignment.CENTER,
        content=ft.Icon(ft.Icons.CAR_CRASH, size=150, color=ft.Colors.GREY_400)
    )
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
        
    datos= ft.Column(
        spacing=12,
        controls=[
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.LABEL, "Placa", item["PLACA"]),
                    campo(ft.Icons.COMMUTE, "Tipo del Vehiculo", item["TIPO"])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.SELL, "Marca", item["MARCA"]),
                    campo(ft.Icons.CATEGORY, "Modelo", item["MODELO"])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.CALENDAR_MONTH, "Año", item["YEAR"]),
                    campo(ft.Icons.BORDER_COLOR, "Color", item["COLOR"])
                ]
            )
        ]
    )
    cedula_propietario= item["PROPIETARIO"][0]["CEDULA"] if item["PROPIETARIO"] else "Sin Popietario"
    nombres_propietario= item["PROPIETARIO"][0]["NOMBRES"] if item["PROPIETARIO"] else "Sin Popietario"
    apellidos_propietario= item["PROPIETARIO"][0]["APELLIDOS"] if item["PROPIETARIO"] else "Sin Popietario"
    telefono_propietario= item["PROPIETARIO"][0]["TELEFONO"] if item["PROPIETARIO"] else "Sin Popietario"
    
    datos_propietario=ft.Column(
        spacing=12,
        controls=[
            ft.Row(
                spacing=12,
                controls=[
                    ft.Text(
                        "Detalles del Propietario",
                        size=30,
                        weight="w500",
                        color=ft.Colors.BLACK
                    )
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.PERSON, "Nombres", nombres_propietario),
                    campo(ft.Icons.PERSON_OUTLINE, "Apellidos", apellidos_propietario)
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.BADGE, "Cédula", cedula_propietario),
                    campo(ft.Icons.PHONE, "Teléfono", telefono_propietario)
                ]
            )
        ]
    )
        
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    height=60,
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.symmetric(horizontal=20),
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color=ft.Colors.BLACK,
                                on_click=lambda e: cambiar_vista(listado_vehiculos())
                            ),
                            ft.Text(
                                "Detalles del Vehiculo",
                                size=20,
                                weight="bold",
                                color=ft.Colors.BLACK
                            ),
                        ]
                    )
                ),
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=950,
                                padding=25,
                                bgcolor=ft.Colors.GREY_200,
                                border_radius=20,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    color=ft.Colors.BLACK12
                                ),
                                content=ft.Column(
                                    scroll=ft.ScrollMode.AUTO,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=15,
                                    controls=[
                                        imagen,
                                        datos,
                                        datos_propietario,
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            controls=[
                                                boton_editar,
                                                boton_eliminar
                                            ]
                                        ),
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    )
def listado_vehiculos():
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        Text("Vehículos Registrados",35,ft.Colors.BLACK,"w500"),
                        ft.Container(expand=True),
                        ft.Button(
                            Text("Agregar Nuevo Vehículo", color=ft.Colors.WHITE),
                            Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                            bgcolor=ft.Colors.BLUE_700,
                            on_click= lambda e: cambiar_vista(agregar_vehículo())
                            )
                        ]
                    ),
                ft.Divider(height=10, color=ft.Colors.BLACK),
                tabla_vehiculos_registrados()
            ]
        )
    )

def editar_veh(e,item):
    #se llena los campos con los atos registrados esto es para poder editar sin tener que llenar todo
    estado_veh.visible=False
    row_chekbox.visible=False 
    marca_vehiculo.value=item["MARCA"]   
    marca_vehiculo.text=item["MARCA"]
    ctr_cat_veh.marca_change(item["MARCA"])
    modelo_vehiculo.value=item["MODELO"]
    placa_vehiculo.value=item["PLACA"]
    año_vehiculo.value=item["YEAR"]
    tipo_vehiculo.value=item["TIPO"]
    color_vehiculo.value=item["COLOR"]
    propietario_vehiculo.value=item["id_cliente"]
    form_global_veh(e)
    boton_cancelar.on_click= lambda e: e.page.pop_dialog()
    boton_guardar.on_click= lambda e: ctr_veh.guardar_datos_editados(e)

def view_vehiculos(page: ft.Page):
    #retorna al dashboard toda la pantalla principal(lsitado de vehiculos)
    pantalla_vehiculos.controls=[listado_vehiculos()]
    return pantalla_vehiculos




def form_global_veh(e):
    boton_cancelar.on_click= lambda e: e.page.pop_dialog()
    boton_guardar.on_click= lambda e: ctr_veh.guardar_datos_vehiculos(e,True)
    formulario_global=e.page.show_dialog(
        ft.AlertDialog(
            modal=True,
            open=True,
            bgcolor=ft.Colors.WHITE,
            content= ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls= [
                    formulario_vehiculos,
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