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
            ft.AppBar(
                title=ft.Text("Hola",color=ft.Colors.BLUE_GREY_800),
                bgcolor=ft.Colors.GREY_200,
                actions=[
                ft.IconButton(
                    ft.Icons.WB_SUNNY_OUTLINED,
                    icon_color=ft.Colors.BLUE_GREY_800
                ),
                
                ft.IconButton(ft.Icons.FILTER_3
                
                )]    
            ),
            ft.Divider(),
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
    