import flet as ft
from models import *

def view_reparaciones(page: ft.Page):
    return ft.Container(
        expand=True,
        bgcolor=ft.Colors.WHITE,
        padding=0,
        content=(
            Text("Pantalla de Reparaiones", 40, ft.Colors.BLACK)
        )
    )