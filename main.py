import flet as ft
import asyncio
import views

def main(page:ft.Page):
    page.title="Gestion"
    page.window.maximized=True
    page.theme_mode=ft.ThemeMode.DARK
    def route_change():
        page.views.clear()
        page.views.append(views.view_dashboard(page))#cambiar entre login y dashboard cuando sea necesario
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
ft.run(main)
