import flet as ft
import asyncio
import views
def view_dashboard(page: ft.Page):
    barra_superior_derecha = ft.Container(
        height=60, # Altura fija para la barra
        bgcolor=ft.Colors.BLUE_GREY_50, # Un gris muy clarito o blanco
        padding=ft.padding.symmetric(horizontal=20),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.END, # Empuja el título a la izq y el botón a la der
            controls=[
                ft.Icon(
                    icon=ft.Icons.ACCOUNT_CIRCLE,
                    color=ft.Colors.BLACK_45, 
                    tooltip="Admin"
                ),
                ft.Text("Byron Velastegui  |",color=ft.Colors.BLACK),
                ft.PopupMenuButton(
                    icon=ft.Icon(ft.Icons.NOTIFICATIONS,color=ft.Colors.BLACK),
                    bgcolor=ft.Colors.WHITE,
                    tooltip="Notificaciones",
                    items=[
                        ft.PopupMenuItem(
                            ft.Text("Notificación de Prueba",color=ft.Colors.BLACK),
                            disabled=True
                            
                        )
                    ]
                ),
                ft.PopupMenuButton(
                    icon=ft.Icon(ft.Icons.MORE_VERT_ROUNDED, color=ft.Colors.BLACK),
                    bgcolor=ft.Colors.WHITE,
                    items=[
                        ft.PopupMenuItem(
                            ft.Text("Acerca de",color=ft.Colors.BLACK)
                        ),
                        ft.PopupMenuItem(
                            ft.Text("Configuración",color=ft.Colors.BLACK)
                        )
                        # Aquí puedes agregar más opciones fácilmente
                    ]
                )
                
            ]
        )
    )
    
    # Contenedor principal, va cambiando segun el menu
    cuerpo_contenido = ft.Column(
        expand=True,
        controls=[
            views.view_inicio(page)
        ]
    )
    
    columna_derecha = ft.Column(
        expand=True, # Esto hace que ocupe todo el ancho sobrante de la derecha
        spacing=0,# Cero espacio entre la barra y el contenido
        controls=[
            barra_superior_derecha,# La barra fija arriba
            cuerpo_contenido        # El contenido dinámico abajo (que también debe tener expand=True)
        ]
    )
    

    # Variable para indcar en que indice del menu nos encontramos(pinta segun el menu en el que iniciemos)
    pestana_actual = 0

    #Contenedor vacío para agregar botones, para poder agregar un boton se necesita: nombre_def.control()
    columna_botones = ft.Column(
        spacing=0
    )

    # Funcion que me permite cambiar entre indice(pestañas)
    def cambiar_pestana(indice):
        nonlocal pestana_actual #nonlocal permite modificar la variable que se encuentra fuera de las funciones
        pestana_actual=indice #(actualiza la variable)(si se elimina no se cambia la animacion del menu)
        
        #Cambia solo el contenido de cuerpo contenido(es necesario acceder con .controls[])
        if indice == 0:
            cuerpo_contenido.controls = [
                views.view_inicio(page)
            ]
        elif indice == 1:
            cuerpo_contenido.controls = [
               views.view_clientes(page)
            ]#Se creara diferentes archivos para cada apartado
        elif indice == 2:
            cuerpo_contenido.controls = [
               views.view_vehiculos(page)
            ]#Se creara diferentes archivos para cada apartado
        elif indice == 3:
           cuerpo_contenido.controls = [
               views.view_reparaciones(page)
           ]
        elif indice == 4:
            cuerpo_contenido.controls=[
                views.view_repuestos(page)
            ]
        elif indice == 5:
            cuerpo_contenido.controls=[
                views.view_personal(page)
            ]
        
        #Se llama a esta funcion para que se actualice de la pantalla
        actualizar_menu()

    # Crea los botones(similar a poo)
    def crear_boton(indice, icono, texto):
        esta_seleccionado = (indice == pestana_actual)#(compara si el indice es igual la pestaña actual y devuelve TRUE)(esta vinculado con las animaciones)
        #crea varios contenedores segun el indice y  las espicificaciones
        return ft.Container(
            content=ft.Row(
                controls=[
                    #crea el boton segun las espicificaciones que le pasemos
                    ft.Icon(icono, color=ft.Colors.WHITE, size=24),
                    ft.Text(texto, color=ft.Colors.WHITE, size=15, weight=ft.FontWeight.BOLD)
                ],
                # Alinea los botones a la derecha
                alignment=ft.MainAxisAlignment.START
            ),
            #mientras esta_seleccionado==True este se pinta de otro color
            bgcolor=ft.Colors.BLUE_700 if esta_seleccionado else ft.Colors.TRANSPARENT,
            #tamaño y espacio de los botones
            padding=ft.padding.symmetric(vertical=15, horizontal=20),
            ink=True, # Hace el efecto de onda al hacer clic
            # Al hacer clic, enviamos el número de este botón a la función maestra
            on_click=lambda e: cambiar_pestana(indice) 
        )

    #Función que carga los botones en la columna
    def actualizar_menu():
        columna_botones.controls = [
            crear_boton(0, ft.Icons.HOUSE, "Inicio"),
            crear_boton(1, ft.Icons.GROUPS, "Clientes"),
            crear_boton(2, ft.Icons.DIRECTIONS_CAR, "Vehiculos"),
            crear_boton(3, ft.Icons.CAR_REPAIR, "Reparaciones"),
            crear_boton(4, ft.Icons.INVENTORY, "Repuestos"),
            crear_boton(5, ft.Icons.PERSON, "Personal")
        ]
    
    # Dibujamos el menú por primera vez al cargar la pantalla
    actualizar_menu()

    #Distribución del menu izquierdo
    menu_izquierdo = ft.Container(
        width=250,
        bgcolor=ft.Colors.BLUE_900,
        content=ft.Column(
            controls=[
                # ENcabezado
                ft.Container(
                    height=60, 
                    bgcolor=ft.Colors.INDIGO_900,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Row( 
                    controls=[
                        ft.Icon(ft.Icons.SETTINGS_SHARP,size=45,color=ft.Colors.WHITE),
                        ft.Text("Gestión Mecánica",size=20,color=ft.Colors.WHITE,weight="w500")
                    ]
                )

                ),
                # Los botones dinámicos
                columna_botones,
                ft.Container(expand=True),#Metodo Resorte
                ft.Divider(),
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.LOGOUT, color=ft.Colors.WHITE, size=24),
                            ft.Text("Cerrar Sesion", color=ft.Colors.WHITE, size=15, weight=ft.FontWeight.BOLD)
                        ],
                        alignment=ft.MainAxisAlignment.START
                    ),
                    bgcolor=ft.Colors.TRANSPARENT,
                    padding=ft.padding.symmetric(vertical=15, horizontal=20),
                    ink=True,
                    on_click= lambda e: asyncio.create_task(page.push_route("/"))
                            
                            
                )
            ],
            spacing=0 # Sin espacios para que las franjas se toquen
        )
    )

    #Retorna todo los agregado para mostrar en pantalla
    return ft.View(
        route="/dashboard",
        padding=0,
        spacing=0,
        controls=[
            ft.Row(
                expand=True,
                spacing=0,
                controls=[
                    menu_izquierdo, 
                    columna_derecha
                ]
            )
        ]
    )