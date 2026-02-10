import flet as ft

from views import view_dashboard, view_login


def main(page: ft.Page):
    page.title = "Gestion"
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.DARK

    def route_change(route: ft.RouteChangeEvent):
        page.views.clear()

        routes = {
            "/": view_login,
            "/login": view_login,
            "/dashboard": view_dashboard,
        }

        builder = routes.get(page.route)
        if builder is None:
            page.views.append(
                ft.View(
                    route=page.route,
                    controls=[
                        ft.Text("Página no encontrada"),
                        ft.ElevatedButton("Ir al login", on_click=lambda e: page.go("/login")),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        else:
            page.views.append(builder(page))

        page.update()

    def view_pop(view: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/login")


ft.app(target=main)
