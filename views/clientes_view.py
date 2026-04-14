import flet as ft
from components import *
from controls import controls_clientes as ctr_cln
import json
import os
#variable que muestra la pantalla 
pantalla_clientes=ft.Column(expand=True)

def cambiar_vista(nueva_vista):
    ctr_cln.limpiar_formulario()
    pantalla_clientes.controls.clear()
    pantalla_clientes.controls.append(nueva_vista)

boton_cancelar= ft.Button(
    content=Text("Cancelar",20, ft.Colors.BLACK),
    bgcolor=ft.Colors.GREY_300,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
    on_click= lambda e: cambiar_vista(listado_clientes())
)
boton_guardar=ft.Button(
    content=Text("Guardar", 20, ft.Colors.WHITE),
    style=ft.ButtonStyle(
        bgcolor={
            ft.ControlState.DISABLED: ft.Colors.GREY_400, 
            ft.ControlState.DEFAULT: ft.Colors.BLUE_700   
        },
        color={
            ft.ControlState.DISABLED: ft.Colors.GREY_600, 
            ft.ControlState.DEFAULT: ft.Colors.WHITE      
        },
        shape=ft.RoundedRectangleBorder(radius=1)
    ),
    on_click= lambda e: ctr_cln.guardar_datos_clientes(e)
)
nombres_cliente=ft.TextField(
    hint_text="Ejemplo: Luis Fernando",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
apellidos_cliente=ft.TextField(
    hint_text="Ejemplo: Pérez Salazar",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
cedula_cliente= ft.TextField(
    hint_text="Ejemplo: 0503456764",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    ),
    max_length=10,
    counter_style=ft.TextStyle(size=0)
    
    
) 
numero_telefono_cliente= ft.TextField(
    hint_text="Ejmplo: 0998743567",
    border_color= ft.Colors.BLACK,
    color= ft.Colors.BLACK,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    ),
    max_length=10,
    counter_style=ft.TextStyle(size=0)
)
text_correo=Text("Correo Electrónico", 20 , ft.Colors.BLACK, "w400")
correo_cliente=ft.TextField(
    width=675,
    hint_text="Ejemplo: automotrizvelastegui@gmail.com",
    border_color= ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
provincias= ft.Dropdown(
    menu_height=400,
    width= 300, 
    hint_text="Seleccione una Provincia",
    options=[ft.dropdown.Option(text=p[1], style=ft.TextStyle(color="black")) for p in ctr_cln.provincias],
    color= ft.Colors.BLACK,
    border_color= ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    on_select= lambda e: ctr_cln.provincia_change(e),
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
ciudades= ft.Dropdown(
    width= 300,
    hint_text="Seleccione una Ciudad",
    color= ft.Colors.BLACK,
    border_color= ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
direccion_cliente= ft.TextField(
    width=675,
    hint_text="Ejemplo: San Felipe, UTC",
    border_color= ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS
)   
check_box_correo=ft.Checkbox(
    value=True,
    label="Registrar un Correo Electrónico",
    label_style=ft.TextStyle(color=ft.Colors.BLACK),
    border_side=ft.BorderSide(2, ft.Colors.BLACK),
    on_change= ctr_cln.validacion_checkbox
    
    
)         

#principal, aqui se consruye todo par apoder mostrar en pantalla,
#se hizo asi para poder reutilizar codigo para editar la info
formulario=ft.Container(
    bgcolor=ft.Colors.GREY_200,
    width=800,
    height=1000,
    padding= 15,
    border_radius=15,
    shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
    content=(
        ft.Column(
            scroll= ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
            expand=True,
            controls=[
                Text("Datos del Cliente", 30, ft.Colors.BLACK, "w500"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        ft.Column(
                            controls=[
                                Text("Nombres", 20, ft.Colors.BLACK, "w400"),
                                nombres_cliente
                                
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Apellidos", 20, ft.Colors.BLACK, "w400"),
                                apellidos_cliente
                            ]
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30,
                    controls=[
                        ft.Column( 
                            controls=[
                                Text("Cédula del Cliente", 20, ft.Colors.BLACK, "w400"),
                                cedula_cliente      
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Número de Telefono", 20, ft.Colors.BLACK, "w400"),
                                numero_telefono_cliente
                            ]
                        )
                        
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        check_box_correo,
                        ft.VerticalDivider(),
                        ft.Container(width=420)
                        ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                text_correo,
                                correo_cliente
                            ]
                        )
                    ]
                ),
                ft.Row(
                    spacing=30,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                Text("Provincia", 20, ft.Colors.BLACK, "w400"),
                                provincias
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Ciudad", 20, ft.Colors.BLACK, "w400"),
                                ciudades
                            ]
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                Text("Dirección", 20, ft.Colors.BLACK, "w400"),
                                direccion_cliente,
                            ]
                        )
                    ]
                )
            ]
        )
    )
)

def agregar_clientes():
    #construye la pantalla para agregar clientes, si se necesit algo mas se puede agregar aqui  
    boton_cancelar.on_click= lambda e: cambiar_vista(listado_clientes())
    boton_guardar.on_click= lambda e: ctr_cln.guardar_datos_clientes(e)
    formulario.bgcolor=ft.Colors.GREY_200
    formulario.shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                Text("Agregar Cliente", 35, ft.Colors.BLACK, "w500" ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[formulario]
                ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        boton_cancelar,
                        boton_guardar
                    ]
                ) 
            ]
        )
    )

def crear_tarjeta(item):

    vehiculos_registrados= len(item["VEHICULOS"]) if item["VEHICULOS"] else "Sin Vehiculo"
    return ft.Card(
        elevation=5,
        shadow_color=ft.Colors.WHITE,
        content=ft.Container(
            bgcolor=ft.Colors.GREY_100,
            padding=3,
            border=ft.border.all(2, ft.Colors.BLACK),
            border_radius=10,
            content=ft.ListTile(
                leading=ft.Icon(icon=ft.Icons.PERSON, size=50),
                title=ft.Text(
                value=f"{item["APELLIDOS"]} {item["NOMBRES"]}",
                color=ft.Colors.BLACK,
                weight=ft.FontWeight.W_500
                ),
                subtitle=ft.Text(
                    value=f"Cedula: {item["CEDULA"]}    Telefono: {item["TELEFONO"]}    Vehiculo: {vehiculos_registrados}",
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_400
                ),
                bgcolor=ft.Colors.GREY_100,
                on_click= lambda e: cambiar_vista(detalles_clientes(item))
            )
        )
)

def tabla_clientes_registrados():
     
    datos=ctr_cln.obtener_datos_clientes()
    
    lista_resultados=ft.Column(expand=True, scroll=ft.ScrollMode.AUTO)
    
    def actualizar_lista(e=None):
        busqueda=barra_busqueda.value.lower().strip()
        lista_resultados.controls.clear()
        for cliente in datos.values():
            if busqueda in cliente["NOMBRES"].lower() or busqueda in cliente["APELLIDOS"].lower() or busqueda in cliente["CEDULA"]:
                nueva_tarjeta=crear_tarjeta(cliente)
                lista_resultados.controls.append(nueva_tarjeta)
                
    barra_busqueda= ft.TextField(
        width=600,
        border_radius=15,
        hint_text="Busqueda por Nombre o  Número de Cedula",
        prefix_icon=ft.Icons.SEARCH,
        on_change=actualizar_lista,
        border_color=ft.Colors.BLACK,
        color=ft.Colors.BLACK
    )
    tabla_principal= ft.Container(
        width=950,
        expand=True,
        content=ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        barra_busqueda,
                    ]
                ),
                lista_resultados
            ]
        )
    )
    
    actualizar_lista()
    
    return ft.Container(
        expand=True,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                tabla_principal
            ]
        )
    )


    
def detalles_clientes(item):
    global id_actual
    id_actual=item["id_cliente"]
    boton_editar=ft.Button(
        content=Text("Editar", 20, ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_600,
        on_click= lambda e: editar_clientes(e,item)
    )
    boton_eliminar=ft.Button(
        content=Text("Eliminar", 20, ft.Colors.WHITE),
        bgcolor=ft.Colors.RED_700,
        on_click=lambda e: ctr_cln.eliminar_datos_cliente()
    )
    imagen = ft.Container(
        width=150,
        height=160,
        border_radius=10,
        alignment=ft.Alignment.CENTER,
        content=ft.Icon(ft.Icons.PERSON, size=150, color=ft.Colors.GREY_400)
    )
    
    def crear_tarjeta(item):
        placa=item["VEHICULOS"][0]["PLACA"]
        return ft.Card(
            elevation=5,
            shadow_color=ft.Colors.WHITE,
            content=ft.Container(
                bgcolor=ft.Colors.GREY_100,
                padding=3,
                border=ft.border.all(2, ft.Colors.BLACK),
                border_radius=10,
                content=ft.ListTile(
                    leading=ft.Icon(icon=ft.Icons.CAR_REPAIR, size=50),
                    title=ft.Text(
                    value=f"{placa}",
                    color=ft.Colors.BLACK,
                    weight=ft.FontWeight.W_500
                    ),
                    subtitle=ft.Text(
                        value=f"TIPO:   Modelo: " ,
                        color=ft.Colors.BLACK,
                        weight=ft.FontWeight.W_400
                    ),
                    bgcolor=ft.Colors.GREY_100,
                )
            )
        )
            
    def vehiculos_registrados(item):
        
        vehiculos=ft.Column()
        sin_vehiculo=ft.Text(
            "No Existen Vehiculos Registrados a Este Cliente",
            size=20,
            color=ft.Colors.GREY_400
        )
        if item["VEHICULOS"]:
            for v in item["VEHICULOS"]:
                vehiculo_registrado=crear_tarjeta(item)
                vehiculos.controls.append(vehiculo_registrado)
        else:
            vehiculos.controls.append(sin_vehiculo)  
        return ft.Column(
            expand=True,
            controls=[
                vehiculos
            ]
        )
    

    def campo(icono, titulo, valor):
        return ft.Container(
            expand=True,
            padding=12,
            border_radius=12,
            bgcolor=ft.Colors.GREY_100,
            border=ft.border.all(1, ft.Colors.GREY_300),
            content=ft.Row(
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=35,
                        height=35,
                        border_radius=8,
                        bgcolor=ft.Colors.BLUE_100,
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(icono, size=18, color=ft.Colors.BLUE_700)
                    ),
                    ft.Column(
                        spacing=2,
                        expand=True,
                        controls=[
                            Text(titulo, 12, ft.Colors.BLACK),
                            Text(valor, 16, ft.Colors.GREY_600 ,"bold")
                        ]
                    )
                ]
            )
        )
    
    datos= ft.Column(
        spacing=12,
        controls=[
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.PERSON, "Nombres", item["NOMBRES"]),
                    campo(ft.Icons.PERSON_OUTLINE, "Apellidos", item["APELLIDOS"])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.BADGE, "Cédula", item["CEDULA"]),
                    campo(ft.Icons.PHONE, "Teléfono", item["TELEFONO"])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.EMAIL, "Correo", item["CORREO"]),
                    campo(ft.Icons.LOCATION_ON, "Provincia", item["PROVINCIA"])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.MAP, "Ciudad", item["CIUDAD"]),
                    campo(ft.Icons.HOME, "Dirección", item["DIRECCION"])
                ]
            ),
        ]
    )
    
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Container(
                    height=60,
                    bgcolor=ft.Colors.WHITE,
                    padding=ft.padding.symmetric(horizontal=20),
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color=ft.Colors.BLACK,
                                on_click=lambda e: cambiar_vista(listado_clientes())
                            ),
                            ft.Text(
                                "Detalles del Cliente",
                                size=20,
                                weight="bold",
                                color=ft.Colors.BLACK
                            ),
                        ]
                    )
                ),
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Container(
                                width=950,
                                padding=25,
                                bgcolor=ft.Colors.GREY_200,
                                border_radius=20,
                                shadow=ft.BoxShadow(
                                    blur_radius=15,
                                    color=ft.Colors.BLACK12
                                ),
                                content=ft.Column(
                                    scroll=ft.ScrollMode.AUTO,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=15,
                                    controls=[
                                        imagen,
                                        datos,
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            controls=[
                                                boton_editar,
                                                boton_eliminar,
                                            ]
                                        ),
                                        ft.Text(
                                            "Vehiculos Registrados",
                                            size=20,
                                            weight="bold",
                                            color=ft.Colors.GREY_800
                                        ),
                                        vehiculos_registrados(item)
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        )
    )

def listado_clientes():
    #misma logica que se estructuro para el listado de vehiculos
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        Text("Clientes Registrados",35,ft.Colors.BLACK,"w500"),
                        ft.Container(expand=True),
                        ft.Button(
                            Text("Agregar Nuevo Cliente", color=ft.Colors.WHITE),
                            Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                            bgcolor=ft.Colors.BLUE_700,
                            on_click= lambda e: cambiar_vista(agregar_clientes())
                        )
                    ]
                ),
                ft.Divider(height=10, color=ft.Colors.BLACK),
                tabla_clientes_registrados()
            ]
        )
    )


def editar_clientes(e,item):
    formulario.shadow=None
    nombres_cliente.value=item["NOMBRES"]
    apellidos_cliente.value=item["APELLIDOS"]
    cedula_cliente.value=item["CEDULA"]
    numero_telefono_cliente.value=item["TELEFONO"]
    correo_cliente.value=item["CORREO"]
    provincias.value=item["PROVINCIA"]
    ctr_cln.provincia_change(item["PROVINCIA"])
    ciudades.value=item["CIUDAD"]
    direccion_cliente.value=item["DIRECCION"]
    form_global_clientes(e)
    boton_cancelar.on_click= lambda e: e.page.pop_dialog()
    boton_guardar.on_click= lambda : ctr_cln.guardar_datos_modificados(e)
    

def view_clientes(page: ft.Page):
    #retorna al dashboard
    pantalla_clientes.controls=[listado_clientes()]
    return pantalla_clientes
    


def form_global_clientes(e):
    boton_cancelar.on_click= lambda e: e.page.pop_dialog()
    boton_guardar.on_click= lambda : ctr_cln.guardar_datos_clientes(e,True)
    formulario.shadow=None
    formulario_global=e.page.show_dialog(
        ft.AlertDialog(
            modal=True,
            open=True,
            bgcolor=ft.Colors.GREY_200,
            content= ft.Column(
                controls= [
                    ft.Container(
                    width=750,
                    height=580,
                    content=formulario
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            expand=True,
                            controls=[
                                boton_cancelar,
                                boton_guardar
                            ]
                        )
                    )  
                ]
            )
        )
    )
    return formulario_global