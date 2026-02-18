import flet as ft
from models import *

def view_reparaciones(page: ft.Page):
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=0,
        content=ft.Column( 
                controls=[
                    Text("Pantalla de Reparaciones",40,ft.Colors.BLACK),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT), # Espaciador
                ]
            )
    )