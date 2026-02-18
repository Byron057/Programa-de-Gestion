import flet as ft 
from models import *

def view_personal(page: ft.Page):
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        padding=0,
        content= ft.Column(
            controls=[
                Text("Pantalla del Personal", 40, ft.Colors.BLACK),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT)
            ]
        )
    )