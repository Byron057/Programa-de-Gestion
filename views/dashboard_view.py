import flet as ft


def view_dashboard(page: ft.Page) -> ft.View:
    page.bgcolor = ft.Colors.WHITE

    return ft.View(
        route="/dashboard",
        appbar=ft.AppBar(title=ft.Text("Dashboard"), bgcolor=ft.Colors.BLUE_700),
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    [
                        ft.Text("Hola Mundo", color=ft.Colors.BLACK, size=28),
                        ft.ElevatedButton(
                            "Cerrar sesión", on_click=lambda e: page.go("/login")
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        ],
    )
