import flet as ft
 
def view_inicio(page: ft.Page):
    return ft.Container(
            expand=True,
            bgcolor=ft.Colors.WHITE, # Fondo general oscuro
            padding=20,
            content=ft.Column( # 1. La Columna principal que organiza TODO el contenido
                controls=[
                    # Título de la sección
                    ft.Text("Gestión de Clientes", size=30, weight="bold", color=ft.Colors.WHITE),
                    
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT), # Espaciador
                    
                    # 2. Aquí puedes meter una FILA para poner varios cuadrados
                    ft.Row(
                        scroll=ft.ScrollMode.AUTO, # Por si pones muchos
                        controls=[
                            # Cuadrado 1
                            ft.Container(
                                width=200, height=150, 
                                bgcolor=ft.Colors.AMBER, 
                                border_radius=10,
                                content=ft.Column([
                                    ft.Icon(ft.Icons.PERSON, color=ft.Colors.BLACK),
                                    ft.Text("Nuevo Cliente", color=ft.Colors.BLACK)
                                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                            ),
                            # Cuadrado 2
                            ft.Container(
                                width=200, height=150, 
                                bgcolor=ft.Colors.BLUE_400, 
                                border_radius=10,
                                content=ft.Text("Lista Total", color=ft.Colors.BLACK)
                            ),
                        ]
                    ),
                    
                    ft.Divider(height=20, color=ft.Colors.GREY_800), # Línea divisoria
                    
                    # 3. Aquí podrías poner un área de texto o una tabla
                    ft.Text("Últimos registros:", size=20, color=ft.Colors.WHITE),
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