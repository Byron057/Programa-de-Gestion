import flet as ft
from models import *

def clientes_view(page: ft.Page):
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=0,
        content=(
            Text("Pantalla de Clientes", 40, ft.Colors.BLACK)
            
        )
        
    )