import flet as ft
import asyncio

def view_dashboard(page: ft.Page):
    
    # 1. Creamos el contenedor del contenido (el que va a cambiar)
    # Lo guardamos en una variable para poder manipularlo luego
    cuerpo_contenido = ft.Column(
        controls=[ft.Container(expand=True,padding=0)],
        alignment=ft.MainAxisAlignment.START,
        expand=True
    )

    # 2. Función que cambia el contenido sin recargar la página
    def cambiar_pestana(e):
        indice = e.control.selected_index
        if indice == 0:
            cuerpo_contenido.controls = [ft.Container(expand=True,padding=0)]
        elif indice == 1:
            cuerpo_contenido.controls = [ft.Text("Contenido de Libros", size=25)]
        elif indice == 2:
            cuerpo_contenido.controls = [ft.Text("Configuración del Sistema", size=25)]
        
       

    return ft.View(
        route="/dashboard",
        bgcolor=ft.Colors.WHITE,
        padding=0,
        spacing=0,# Para que la barra pegue al borde
        controls=[
            ft.Container(
                width=300,
                height=70,
                bgcolor=ft.Colors.INDIGO_900,
                content=ft.Row( 
                    controls=[
                        ft.Icon(ft.Icons.SETTINGS_SHARP,size=50),
                        ft.Text("Gestión Mecánica",size=25,weight=ft.FontWeight.W_700)
                    ]
                )
            ),
            ft.Row(
                expand=True,# Muy importante para que ocupe todo el alto
                controls=[
                    ft.NavigationRail(
                        selected_index=0,
                        label_type=ft.NavigationRailLabelType.ALL,
                        width=300,
                        extended=True, # Si es True, muestra nombres largos
                        bgcolor=ft.Colors.BLUE_900,
                        group_alignment=ft.MainAxisAlignment.START,
                        selected_label_text_style=ft.TextStyle(
                            color=ft.Colors.WHITE, 
                            weight=ft.FontWeight.BOLD,
                            size=30
                        ),
                        unselected_label_text_style=ft.TextStyle(
                            color=ft.Colors.GREY_400,
                            size=25
                        ),
                        indicator_color=ft.Colors.GREEN,
                        indicator_shape=ft.RoundedRectangleBorder(radius=5),
                        destinations=[
                            ft.NavigationRailDestination(
                                icon=ft.Icons.HOUSE,
                                label="Inicio",
                                
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icons.FAVORITE_BORDER,
                                selected_icon=ft.Icons.FAVORITE,
                                label="First",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icons.BOOKMARK_BORDER,
                                selected_icon=ft.Icons.BOOKMARK,
                                label="Second",
                            ),
                            ft.NavigationRailDestination(
                                icon=ft.Icons.SETTINGS_OUTLINED,
                                selected_icon=ft.Icons.SETTINGS,
                                label="Settings",
                            ),
                        ],
                        # 3. CONEXIÓN: Al cambiar, ejecutamos la función
                        on_change=cambiar_pestana 
                    ),
                    # 4. Aquí colocamos nuestra variable dinámica
                    cuerpo_contenido, 
                ],
            ),
            ft.Container(
                width=300,
                height=50,
                bgcolor=ft.Colors.BLUE_900,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.Text("Cerrar Sesión"),
                        ft.IconButton(
                            ft.Icons.LOGIN,
                            on_click= lambda e: asyncio.create_task(page.push_route("/"))
                        )
                    ]
                )
            )
        ]
    )