import flet as ft
from components import *
from views import *
#codigo qu eno se utilizar apor el momento, tal vez en un futuro se agregue una funcion nueva
pantalla_reparaciones=ft.Column(expand=True)

def cambiar_vista(nueva_vista):
    pantalla_reparaciones.controls.clear()
    pantalla_reparaciones.controls.append(nueva_vista)
    pantalla_reparaciones.update()

boton_cancelar= ft.Button(
                        content=Text("Cancelar",20, ft.Colors.BLACK),
                        bgcolor=ft.Colors.GREY_300,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
                        on_click= lambda e: cambiar_vista(listado_reparaciones())
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
            on_click= lambda e: cambiar_vista(listado_reparaciones())
        )

def registrar_reparación():
    
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                Text("Agregar Cliente", 35, ft.Colors.BLACK, "w500" ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
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

def listado_reparaciones():
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        Text("Reparaciones Registradas",35,ft.Colors.BLACK,"w500"),
                        ft.Container(expand=True),
                        ft.Button(
                            Text("Agregar Nuevo Cliente", color=ft.Colors.WHITE),
                            Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                            bgcolor=ft.Colors.BLUE_700,
                            on_click= lambda e: cambiar_vista(registrar_reparación())
                            )
                        ]
                    ),
                ft.Divider(height=10, color=ft.Colors.BLACK)
            ]
        )
    )
def view_reparaciones(page: ft.Page):
    pantalla_reparaciones.controls=[listado_reparaciones()]
    return pantalla_reparaciones