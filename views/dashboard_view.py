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
            ft.NavigationRail(

        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.DIRECTIONS_CAR, 
                label="Vehículos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS, 
                label="Configuración"
            ),
        ]
    )
        ])