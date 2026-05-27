import flet as ft
from components import *
def view_inicio(page: ft.Page):
    from controls import controls_clientes, controls_vehiculos, controls_personal
    
    total_clientes=controls_clientes.total_clientes()
    total_vehiculos=controls_vehiculos.total_vehiculos()
    total_personal= controls_personal.total_personal()
    
    def crear_tarjeta_info(color1, color2, text, icon, total):
        return ft.Container(
            width=200,
            height=150,
            padding=0,
            border_radius=10,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Container(
                        bgcolor=color1,
                        alignment=ft.Alignment.CENTER,
                        width=200,
                        height=85,
                        content=Icon(icon, ft.Colors.WHITE,100)
                    ),
                    ft.Container(
                        width=200,
                        height=65,
                        bgcolor=color2,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                Text(total,45,ft.Colors.WHITE,"bold"),
                                ft.Column(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.START,
                                    spacing=0,
                                    controls=[
                                        Text(text,22,ft.Colors.WHITE),
                                        Text("Registrados",17,ft.Colors.WHITE),
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
    return ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE,
            padding=20,
            content=ft.Column( 
                controls=[
                    Text("Nombre Local...",60,ft.Colors.BLACK,"w900"),
                    ft.Divider(height=10, color=ft.Colors.BLACK), # Espaciador
                    ft.Column(
                        controls=[
                            Text("Resumen General",30, ft.Colors.BLACK),
                            ft.Row(
                                controls=[
                                    crear_tarjeta_info(
                                        ft.Colors.GREEN, ft.Colors.GREEN_900, 
                                        "Clientes", ft.Icons.GROUPS, total_clientes
                                    ),
                                    crear_tarjeta_info(
                                        ft.Colors.AMBER_800, ft.Colors.AMBER_900,
                                        "Vehiculos",ft.Icons.INVENTORY, total_vehiculos
                                    ),
                                    crear_tarjeta_info(
                                        ft.Colors.BLUE_400, ft.Colors.BLUE,
                                        "Personal", ft.Icons.PERSON, total_personal
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