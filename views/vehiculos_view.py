import flet as ft
from models import *
from views import *
 

def view_vehiculos(page: ft.Page):
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        content= ft.Column(
            controls=[
                Text("Pantalla de Vehiculos",40,ft.Colors.BLACK),
                ft.Divider(height=10,color=ft.Colors.TRANSPARENT),
                ft.Button("prueba", on_click= lambda e: Form_global(page))
            ]
        )
    )