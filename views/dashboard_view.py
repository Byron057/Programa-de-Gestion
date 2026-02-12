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
            ft.Container(
                width=300,
                height=300,
                bgcolor=ft.Colors.AMBER
            ),
            ft.Button(
                "Regresar", on_click= lambda: asyncio.create_task(page.push_route("/"))
            )
        ]
    )