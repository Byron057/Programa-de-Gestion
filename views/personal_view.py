import flet as ft
from components import *
from controls import controls_personal as ctr_per
import os
import shutil

#variable que muestra la pantalla 
pantalla_personal=ft.Column(expand=True)

def cambiar_vista(nueva_vista):
    ctr_per.limpiar_formulario()
    pantalla_personal.controls.clear()
    pantalla_personal.controls.append(nueva_vista)
    pantalla_personal.update()


#variables que se usan en el formulario de los clientes
#falta asociar o no a un vehiculo esto se hara en el momento enel que tenga registtrado en la db

boton_cancelar= ft.Button(
    content=Text("Cancelar",20, ft.Colors.BLACK),
    bgcolor=ft.Colors.GREY_300,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
    on_click= lambda e: cambiar_vista(listado_personal())
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
    on_click= lambda e: [guardar_imagen(),ctr_per.guardar_datos_personal(e)]
)

ruta_anterior= None
nueva_ruta=None

def construir_stack_foto(foto_seleccionada):
    def eliminar_foto():
        global ruta_anterior
        ruta_anterior=""
        foto_integrante.content=[]
        foto_integrante.content=ctr_per.estado_incial_foto()
    
    foto=ft.Image(
                width=180,
                height=210,
                border_radius=10,
                src= foto_seleccionada
            )
    
    boton_x=ft.Container(
                content=ft.IconButton(
                    icon=ft.Icons.CANCEL,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e: eliminar_foto()
                )
            )
    foto_integrante.content=[]
    foto_integrante.on_click=False
    foto_integrante.content=ft.Stack(
        controls=[
            foto,
            boton_x
        ]
    )

async def  seleccionar_foto(e):
    global ruta_anterior
    
    
    file_picker=ft.FilePicker()
    
    foto_seleccionada= await file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)
    
    if foto_seleccionada:
        construir_stack_foto(foto_seleccionada[0].path)

    if foto_seleccionada:
        ruta_anterior= foto_seleccionada[0].path 
    else:
        ruta_anterior=""
ruta_anterior= None

def guardar_imagen():
    global nueva_ruta
    destino_imagen=os.path.join("assets","fotos_personal")
    if ruta_anterior:
        try:
            nueva_ruta = shutil.copy(ruta_anterior, destino_imagen)
        except shutil.SameFileError:
            nueva_ruta = ruta_anterior 
    else:
        nueva_ruta=""

foto_integrante = ft.Container(
    width=180,
    height=210,
    border_radius=10,
    border=ft.border.all(1, ft.Colors.GREY_500),
    content=ft.Stack(
        controls=[
            ctr_per.estado_incial_foto()
        ]
    )
)
nombres_personal=ft.TextField(
    hint_text="Luis Fernando",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
apellidos_personal=ft.TextField(
    hint_text="Pérez Salazar",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
cedula_personal= ft.TextField(
    hint_text="0503456764",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    max_length=10,
    counter_style=ft.TextStyle(size=0),
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
    
) 
numero_telefono_personal= ft.TextField(
    hint_text="0998743567",
    border_color= ft.Colors.BLACK,
    color= ft.Colors.BLACK,
    max_length=10,
    counter_style=ft.TextStyle(size=0),
    error_style=ft.TextStyle(
        color=ft.Colors.RED_ACCENT_700,
        weight=ft.FontWeight.W_500,
        font_family="Roboto-Medium"
    )
)
text_correo=Text("Correo Electrónico", 20 , ft.Colors.BLACK, "w400")
correo_personal=ft.TextField(
    width=675,
    hint_text="automotrizvelastegui@gmail.com",
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
    options=[ft.dropdown.Option(data=str(p[0]),text=p[1], style=ft.TextStyle(color="black")) for p in ctr_per.provincias],
    color= ft.Colors.BLACK,
    border_color= ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    on_select= lambda e: ctr_per.provincia_change(e),
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
direccion_personal= ft.TextField(
    width=675,
    hint_text="San Felipe, UTC",
    border_color= ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization= ft.TextCapitalization.WORDS
)   
check_box_correo=ft.Checkbox(
    value=True,
    label="Registrar un Correo Electrónico",
    label_style=ft.TextStyle(color=ft.Colors.BLACK),
    border_side=ft.BorderSide(2, ft.Colors.BLACK),
    on_change= ctr_per.validacion_checkbox
    
    
)         

#principal, aqui se consruye todo par apoder mostrar en pantalla,
#se hizo asi para poder reutilizar codigo para editar la info
formulario_personal=ft.Container(
    bgcolor=ft.Colors.GREY_200,
    width=950,
    height=1000,
    padding= 15,
    border_radius=15,
    shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
    content=(
        ft.Row(
            controls=[
                ft.Column(
                    width=200,
                    controls=[
                        ft.Container(
                            padding=10,
                            expand=True,
                            margin=ft.margin.only(top=50),
                            content=ft.Column(
                                controls=
                                foto_integrante
                            )
                        )
                        ]),
                ft.Column(
                    scroll= ft.ScrollMode.AUTO,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    expand=True,
                    controls=[
                        Text("Datos del Personal", 30, ft.Colors.BLACK, "w500"),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=30,
                            controls=[
                                ft.Column(
                                    controls=[
                                        Text("Nombres", 20, ft.Colors.BLACK, "w400"),
                                        nombres_personal
                                        
                                    ]
                                ),
                                ft.VerticalDivider(),
                                ft.Column(
                                    controls=[
                                        Text("Apellidos", 20, ft.Colors.BLACK, "w400"),
                                        apellidos_personal
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
                                        Text("Cédula de Identidad ", 20, ft.Colors.BLACK, "w400"),
                                        cedula_personal     
                                    ]
                                ),
                                ft.VerticalDivider(),
                                ft.Column(
                                    controls=[
                                        Text("Número de Telefono", 20, ft.Colors.BLACK, "w400"),
                                        numero_telefono_personal
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
                                        correo_personal
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
                                        direccion_personal,
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )
)

def agregar_personal():
    boton_cancelar.on_click= lambda e: cambiar_vista(listado_personal())
    boton_guardar.on_click= lambda e: [guardar_imagen(),ctr_per.guardar_datos_personal(e)]
    formulario_personal.bgcolor=ft.Colors.GREY_200
    formulario_personal.shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                Text("Registrar Nuevo Cliente", 35, ft.Colors.BLACK, "w500" ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[formulario_personal]
                ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        boton_cancelar,
                        boton_guardar,
                    ]
                ) 
            ]
        )
    )

def crear_tarjeta(item):
    if item[9]:  # si hay imagen
        imagen = ft.Image(
            src=item[9],
            width=150,
            height=160,
            fit=ft.BoxFit.COVER,
            border_radius=10
        )
    else:  
        imagen = ft.Container(
            width=150,
            height=160,
            border=ft.border.all(1, ft.Colors.GREY_500),
            border_radius=10,
            alignment=ft.Alignment.CENTER,
            content=ft.Icon(ft.Icons.PERSON, size=50, color=ft.Colors.GREY_400)
        )

    return ft.Container(
       expand=True,
        bgcolor=ft.Colors.GREY_200,
        border_radius=20,
        on_click= lambda e: cambiar_vista(detalles_personal(item)),
        padding=20,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,  
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                imagen,
                ft.Text(item[2], size=18, weight="bold", color= ft.Colors.BLACK)
            ]
        )
    )


def tabla_personal_registrado():
    datos= ctr_per.obtener_datos_personal()
    
    tabla_principal= ft.GridView(
        expand= True,
        max_extent=200,
        child_aspect_ratio=0.8,
        controls=[
            crear_tarjeta(item) for item in datos
        ]
    )
    
    return ft.Container(
        expand=True,
        padding=20,
        content=(tabla_principal)
    )

def listado_personal():
    #misma logica que se estructuro para el listado de vehiculos
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        Text("Equipo Técnico",35,ft.Colors.BLACK,"w500"),
                        ft.Container(expand=True),
                        ft.Button(
                            Text("Nuevo Integrante", color=ft.Colors.WHITE),
                            Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                            bgcolor=ft.Colors.BLUE_700,
                            on_click= lambda e: cambiar_vista(agregar_personal())
                            )
                        ]
                    ),
                ft.Divider(height=10, color=ft.Colors.BLACK),
                tabla_personal_registrado()
            ]
        )
    )

def detalles_personal(item):
    global id_actual
    id_actual=item[0]
    
    boton_editar=ft.Button(
        content=Text("Editar", 20, ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE_600,
        on_click= lambda e: formulario_global(e, item)
    )
    boton_eliminar=ft.Button(
        content=Text("Eliminar", 20, ft.Colors.WHITE),
        bgcolor=ft.Colors.RED_700,
        on_click= lambda e: ctr_per.eliminar_datos_personal()
    )
    
    if item[9]:
        imagen = ft.Image(
            src=item[9],
            width=150,
            height=160,
            fit=ft.BoxFit.COVER,
            border_radius=10
        )
    else:
        imagen = ft.Container(
            width=150,
            height=160,
            border=ft.border.all(1, ft.Colors.GREY_500),
            border_radius=10,
            alignment=ft.Alignment.CENTER,
            content=ft.Icon(ft.Icons.PERSON, size=50, color=ft.Colors.GREY_400)
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

    datos = ft.Column(
        spacing=12,
        controls=[
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.PERSON, "Nombres", item[2]),
                    campo(ft.Icons.PERSON_OUTLINE, "Apellidos", item[3])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.BADGE, "Cédula", item[1]),
                    campo(ft.Icons.PHONE, "Teléfono", item[4])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.EMAIL, "Correo", item[5]),
                    campo(ft.Icons.LOCATION_ON, "Provincia", item[6])
                ]
            ),
            ft.Row(
                spacing=12,
                controls=[
                    campo(ft.Icons.MAP, "Ciudad", item[7]),
                    campo(ft.Icons.HOME, "Dirección", item[8])
                ]
            ),
        ]
    )

    return ft.Container(
        expand=True,
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
                                on_click=lambda e: cambiar_vista(listado_personal())
                            ),
                            ft.Text(
                                "Detalles del Cliente",
                                size=20,
                                weight="bold",
                                color=ft.Colors.BLACK
                            )
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
                                                boton_eliminar
                                            ]
                                        ),

                                        ft.Divider(),

                                        ft.Text(
                                            "Historial de trabajo",
                                            size=18,
                                            weight="bold"
                                        )
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]
        )
    )

def view_personal(page: ft.Page):
    #retorna al dashboard
    pantalla_personal.controls=[listado_personal()]
    return pantalla_personal
    
def formulario_global(e, item):
    global ruta_anterior
    formulario_personal.bgcolor=ft.Colors.WHITE
    formulario_personal.shadow=None
    nombres_personal.value= item[2]
    apellidos_personal.value= item[3]
    cedula_personal.value= item[1]
    numero_telefono_personal.value= item[4]
    correo_personal.value=item[5]
    provincias.value=item[6]
    ctr_per.provincia_change(item[6])
    ciudades.value=item[7]
    direccion_personal.value=item[8]
    if item[9] !="":
        ruta_anterior=item[9]
        construir_stack_foto(item[9])
    else:
        foto_integrante.content= ctr_per.estado_incial_foto()
    boton_guardar.on_click=lambda e: [guardar_imagen(),ctr_per.guardar_datos_modificados(e)]
    boton_cancelar.on_click= lambda e: e.page.pop_dialog()
    return e.page.show_dialog(
        ft.AlertDialog(
            modal=True,
            open=True,
            bgcolor=ft.Colors.WHITE,
            content= ft.Column(
                controls= [
                    ft.Container(
                    width=920,
                    height=580,
                    content=formulario_personal
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
    
#FALTA AGREGAR HISTORIAL DE REPARACIONES ADEMAS DE CORREGIR ERRORES QUE SE PRESENTEN EN EL FUTUR    O