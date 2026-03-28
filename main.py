import asyncio
import flet as ft
from database import db_core
db_core.conn_db.data_necesaria()
import os
import views
def inicializar_carpetas_sistema():
    ruta_fotos = os.path.join("assets", "fotos_personal")
    
    os.makedirs(ruta_fotos, exist_ok=True)
    print("Directorios del sistema verificados.")
inicializar_carpetas_sistema()

def main(page:ft.Page):
    page.title="Gestion"
    page.window.maximized=True
    def route_change():
        page.views.clear()
        page.views.append(views.view_login(page))#cambiar entre login y dashboard cuando sea necesario
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

