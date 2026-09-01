import flet as ft
from database import db_core
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
                    Text("Automotriz Velastegui",60,ft.Colors.BLACK,"w900"),
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
                    ft.Text("Últimos Registros del Sistema", size=20, color=ft.Colors.BLACK, weight="w600"),
                    ft.Container(
                        expand=True,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=10,
                        border=ft.border.all(1.5, ft.Colors.BLACK87), # Borde estilo MecaSoft
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        padding=0,
                        content=ft.Column(
                            expand=True,
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.DataTable(
                                    width=float("inf"),
                                    heading_row_color=ft.Colors.BLUE_900,
                                    heading_row_height=50,
                                    data_row_min_height=75, # Hacemos las filas más altas para que llenen el espacio vertical
                                    data_row_max_height=75,
                                    divider_thickness=0.5,
                                    # IMPORTANTE: Forzamos el ancho de las columnas para que llenen el espacio a la derecha
                                    columns=[
                                        ft.DataColumn(ft.Container(content=ft.Text("TIPO DE REGISTRO", color=ft.Colors.WHITE, weight="bold"), width=230)),
                                        ft.DataColumn(ft.Container(content=ft.Text("DETALLE", color=ft.Colors.WHITE, weight="bold"), width=350)),
                                        ft.DataColumn(ft.Container(content=ft.Text("IDENTIFICADOR", color=ft.Colors.WHITE, weight="bold"), width=200)),
                                    ],
                                    rows=[
                                        ft.DataRow(cells=[
                                            ft.DataCell(
                                                ft.Row([
                                                    ft.Icon(
                                                        ft.Icons.PERSON if fila[0] == 'Nuevo Cliente' else (ft.Icons.DIRECTIONS_CAR if fila[0] == 'Nuevo Vehículo' else ft.Icons.BUILD_CIRCLE),
                                                        color=ft.Colors.GREEN_600 if fila[0] == 'Nuevo Cliente' else (ft.Colors.ORANGE_600 if fila[0] == 'Nuevo Vehículo' else ft.Colors.BLUE_600),
                                                    ),
                                                    ft.Text(str(fila[0]), color=ft.Colors.BLACK87, weight="w600")
                                                ])
                                            ), 
                                            ft.DataCell(ft.Text(str(fila[1]), color=ft.Colors.BLACK87)),
                                            ft.DataCell(
                                                ft.Container(
                                                    padding=ft.padding.symmetric(horizontal=12, vertical=6),
                                                    bgcolor=ft.Colors.GREY_100,
                                                    border_radius=6,
                                                    border=ft.Border.all(1, ft.Colors.GREY_300),
                                                    content=ft.Text(str(fila[2]), color=ft.Colors.BLACK87, weight="bold")
                                                )
                                            ),
                                        ])
                                        for fila in db_core.obtener_actividad_reciente()
                                    ]
                                )
                            ]
                        )
                    )
                    
                ]
            )
        )