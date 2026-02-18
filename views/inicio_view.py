import flet as ft
from models import *
def view_inicio(page: ft.Page):
    return ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE, 
            padding=20,
            content=ft.Column( 
                controls=[
                    Text("Mecánica Automotriz Velastegui",70,ft.Colors.BLACK,"w900"),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT), # Espaciador
                    ft.Column(
                        controls=[
                            Text("Resumen General",24, ft.Colors.BLACK),
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        width=200,
                                        height=150,
                                        padding=0,
                                        border_radius=10,
                                        content=ft.Column(
                                            spacing=0,
                                            controls=[
                                                ft.Container(
                                                    bgcolor=ft.Colors.GREEN,
                                                    alignment=ft.Alignment.CENTER,
                                                    width=200,
                                                    height=85,
                                                    content=Icon(ft.Icons.GROUPS, ft.Colors.WHITE,100)
                                                ),
                                                ft.Container(
                                                    width=200,
                                                    height=65,
                                                    bgcolor=ft.Colors.GREEN_900,
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                        controls=[
                                                            Text("120",45,ft.Colors.WHITE,"bold"),
                                                            ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                                                spacing=0,
                                                                controls=[
                                                                    Text("Clientes",22,ft.Colors.WHITE,0),
                                                                    Text("Registrados",17,ft.Colors.WHITE,0),
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        ]
                    ),
                    
                    ft.Divider(height=20, color=ft.Colors.GREY_800), # Línea divisoria
                    
                    # 3. Aquí podrías poner un área de texto o una tabla
                    ft.Text("Últimos registros:", size=20, color=ft.Colors.BLACK),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.GREY_800,
                        border_radius=10,
                        padding=10,
                        content=ft.Text("Aquí irá la base de datos de SQLite pronto...", color=ft.Colors.GREY_400)
                    )
                ]
            )
        )