import flet as ft
class container:
    def __init___(self):
        pass
def hola(page: ft.Page):
    page.clean()
    page.bgcolor=ft.Colors.WHITE
    page.add(ft.Text("Hola Mundo"))