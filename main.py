import flet as ft
import views
def main(page:ft.Page):
    page.title="Gestion"
    page.window.maximized=True
    page.theme_mode=ft.ThemeMode.DARK
    page.add(views.view_dashboard(page))
    page.update()
ft.app(target=main)
