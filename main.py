import flet as ft
from config import *
inicializar_sistema()
from database import db_core
db_core.data_necesaria()
import views

def main(page:ft.Page):
    page.title="Mecasoft"
    page.window.width = 1400
    page.window.height = 900
    page.window.icon=ruta_recurso("assets/MecaSoft.ico")

    page.window.maximized = True
    def route_change():
        page.views.clear()
        page.views.append(views.view_login(page))
        if page.route=="/dashboard":
            page.views.append(views.view_dashboard(page))
        page.update()
    
    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
    
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()
ft.run(main, assets_dir="assets")
