import flet as ft
from models import *
import json
import os
ruta= os.path.join("assets", "config.json")

def cargar_datos():
    with open(ruta, "r", encoding="UTF-8") as f:
        return json.load(f)

config= cargar_datos()
DATA_ECUADOR= config["ubicaciones"]

def view_clientes(page: ft.Page):

    pantalla_clientes=ft.Column(expand=True)
    
    def cambiar_vista(nueva_vista):
        pantalla_clientes.controls.clear()
        pantalla_clientes.controls.append(nueva_vista)
        pantalla_clientes.update()
    
    def agregar_clientes():
        ciudades_actuales=[] 
        
        global formulario
        
        def cargar_ciudades(provincia):
            ciudades_actuales.clear()
            for i in DATA_ECUADOR[provincia]:
                ciudades_actuales.append(i)
            ciudades.options= [ft.dropdown.Option(text= c,style= ft.TextStyle(color="black")) for c in ciudades_actuales]
            
        provincias= ft.Dropdown(
            width= 300, 
            hint_text="Seleccione una Provincia",
            options=[ft.dropdown.Option(text=p, style=ft.TextStyle(color="black")) for p in DATA_ECUADOR],
            color= ft.Colors.BLACK,
            border_color= ft.Colors.BLACK,
            bgcolor=ft.Colors.WHITE,
            on_select= lambda e: cargar_ciudades(provincias.value)
        )
        ciudades= ft.Dropdown(
            width= 300,
            hint_text="Seleccione una Ciudad",
            color= ft.Colors.BLACK,
            border_color= ft.Colors.BLACK,
            bgcolor=ft.Colors.WHITE
        )
                
                
        boton_cancelar= ft.Button(
                        content=Text("Cancelar",20, ft.Colors.BLACK),
                        bgcolor=ft.Colors.GREY_300,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
                        on_click= lambda e: cambiar_vista(listado_clientes())
                    )
        boton_guardar=ft.Button(
                    content=Text("Guardar", 20, ft.Colors.WHITE),
                    disabled=True,
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
                    on_click= lambda e: cambiar_vista(listado_clientes())
                )
        
        nombres_cliente=ft.TextField(
                        hint_text="Ejemplo: Luis Fernando",
                        border_color=ft.Colors.BLACK,
                        color=ft.Colors.BLACK,
                        capitalization=ft.TextCapitalization.WORDS,
                        on_change= lambda e: validar_campos_llenos()
                    )
        apellidos_cliente=ft.TextField(
            hint_text="Ejemplo: Pérez Salazar",
            border_color=ft.Colors.BLACK,
            color=ft.Colors.BLACK,
            capitalization=ft.TextCapitalization.WORDS,
            on_change= lambda e: validar_campos_llenos()
        )
        cedula_cliente= ft.TextField(
            hint_text="Ejemplo: 0503456764",
            border_color=ft.Colors.BLACK,
            color=ft.Colors.BLACK,
            on_change= lambda e: validar_campos_llenos()
            
        ) 
        numero_telefono_cliente= ft.TextField(
            hint_text="Ejmplo: 0998743567",
            border_color= ft.Colors.BLACK,
            color= ft.Colors.BLACK,
            on_change=lambda e: validar_campos_llenos()
        )
        correo_clientes=ft.TextField(
            width=675,
            hint_text="Ejemplo: automotrizvelastegui@gmail.com",
            border_color= ft.Colors.BLACK,
            color=ft.Colors.BLACK,
            on_change=lambda e: validar_campos_llenos()
        )
        direccion_cliente= ft.TextField(
            width=675,
            hint_text="Ejemplo: San Felipe, UTC",
            border_color= ft.Colors.BLACK,
            color=ft.Colors.BLACK,
            on_change= lambda e: validar_campos_llenos()
        )            
        formulario=ft.Container(
                            bgcolor=ft.Colors.GREY_200,
                            width=800,
                            height=1000,
                            padding= 15,
                            border_radius=15,
                            shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
                            content=(
                                ft.Column(
                                    scroll= ft.ScrollMode.AUTO,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=5,
                                    expand=True,
                                    controls=[
                                        Text("Datos del Cliente", 30, ft.Colors.BLACK, "w500"),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=30,
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        Text("Nombres del Cliente", 20, ft.Colors.BLACK, "w400"),
                                                        nombres_cliente
                                                        
                                                    ]
                                                ),
                                                ft.VerticalDivider(),
                                                ft.Column(
                                                    controls=[
                                                        Text("Apellidos del Cliente", 20, ft.Colors.BLACK, "w400"),
                                                        apellidos_cliente
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=30,
                                            controls=[
                                                ft.Column( 
                                                    controls=[
                                                      Text("Cédula del Cliente", 20, ft.Colors.BLACK, "w400"),
                                                      cedula_cliente      
                                                    ]
                                                ),
                                                ft.VerticalDivider(),
                                                ft.Column(
                                                    controls=[
                                                        Text("Número de Telefono", 20, ft.Colors.BLACK, "w400"),
                                                        numero_telefono_cliente
                                                    ]
                                                )
                                                
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        Text("Correo Electrónico", 20 , ft.Colors.BLACK, "w400"),
                                                        correo_clientes
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
                                                        Text("Provincia", 20, ft.Colors.BLACK, "w400"),
                                                        provincias
                                                    ]
                                                ),
                                                ft.VerticalDivider(),
                                                ft.Column(
                                                    controls=[
                                                        Text("Ciudad", 20, ft.Colors.BLACK, "w400"),
                                                        ciudades
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Column(
                                                    controls=[
                                                        Text("Dirección", 20, ft.Colors.BLACK, "w400"),
                                                        direccion_cliente,
                                                    ]
                                                )
                                            ]
                                        )
                                    ]
                                )
                            )
                        )
        
        
        def validar_campos_llenos():
            if nombres_cliente.value != "" and apellidos_cliente.value != "":
                boton_guardar.disabled=False
            else:
                boton_guardar.disabled=True
            
                
        return ft.Container(
            expand= True,
            bgcolor=ft.Colors.WHITE,
            padding=20,
            content=ft.Column(
                expand=True,
                controls=[
                    Text("Agregar Cliente", 30, ft.Colors.BLACK, "w500" ),
                    ft.Divider(),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=True,
                        controls=[formulario]
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
    def listado_clientes():
        return ft.Container(
            expand= True,
            bgcolor=ft.Colors.WHITE,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            Text("Clientes",35,ft.Colors.BLACK,"w500"),
                            ft.Container(expand=True),
                            ft.Button(
                                Text("Agregar Nuevo Cliente", color=ft.Colors.WHITE),
                                Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                                bgcolor=ft.Colors.BLUE_700,
                                on_click= lambda e: cambiar_vista(agregar_clientes())
                                )
                            ]
                        ),
                    ft.Divider(height=10, color=ft.Colors.BLACK)
                ]
            )
        )
    
    pantalla_clientes.controls=[listado_clientes()]
    return pantalla_clientes
    


def Form_global(page: ft.Page):
    formulario_global=page.show_dialog(
        ft.AlertDialog(
            content=formulario
        )
    )
    return formulario_global