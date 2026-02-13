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
            ft.Row(
            [
            ft.Container(
                expand=1,
                bgcolor=ft.Colors.ORANGE_300
            ),
            ft.VerticalDivider(),
            ],
            width=400,
            height=800
        )]
    )
    