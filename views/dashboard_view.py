import flet as ft
import asyncio
class container:
    def __init___(self):
        pass
def view_dashboard(page: ft.Page):
    return ft.View(
        route="/dashboard",
        bgcolor=ft.Colors.WHITE,
        controls=[
            ft.AppBar(
                title=ft.Text("Hola",color=ft.Colors.BLUE_GREY_400),
                bgcolor=ft.Colors.GREY_200,
                actions=[
                ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
                ft.IconButton(ft.Icons.FILTER_3),
            ]
                
            
                
            )
        ]
    )
    