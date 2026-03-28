import flet as ft
from components import *
import json
import os
#variable que muestra la pantalla 
pantalla_repuestos=ft.Column(expand=True)

def limpiar_formulario():
    #reestablece los datos del formulario
    nombres_repuesto.value=""
    codigo_repuesto.value=""
    cantidad_repuesto.value=""
    precio_repuestp.value=""
    correo_personal.value=""
    text_correo.color=ft.Colors.BLACK
    correo_personal.color=ft.Colors.BLACK
    correo_personal.read_only=False
    check_box_correo.value=True

    foto_repuesto.content=estado_incial_foto()

def cambiar_vista(nueva_vista):
    boton_guardar.disabled=True
    limpiar_formulario()
    pantalla_repuestos.controls.clear()
    pantalla_repuestos.controls.append(nueva_vista)
    pantalla_repuestos.update()
#variable que me permite guardar temporalmente las ciudades

def validar_campos_llenos():
        #funcion incompleta en un futuro debe validar todos los campos
        if (
            nombres_repuesto.value
            and codigo_repuesto.value 
            and precio_repuestp.value
            and cantidad_repuesto.value 
            and correo_personal.value 
        ):
            boton_guardar.disabled=False
        else:
            boton_guardar.disabled=True

def validacion_checkbox():
    #funcion que me permite registtrar o no un correo electronico
    correo_personal.value = ""
    
    if check_box_correo.value:
        text_correo.color= ft.Colors.BLACK
        correo_personal.color= ft.Colors.BLACK
        correo_personal.read_only = False
        
    else:
        correo_personal.read_only = True
        correo_personal.color= ft.Colors.GREY_400
        text_correo.color=ft.Colors.GREY_400
        #por el momento me registra esto para no tener conflictos en las validaciones, posiblemente cambie la logica
        correo_personal.value = "N/A"

    validar_campos_llenos()

#variables que se usan en el formulario de los clientes
#falta asociar o no a un vehiculo esto se hara en el momento enel que tenga registtrado en la db

boton_cancelar= ft.Button(
    content=Text("Cancelar",20, ft.Colors.BLACK),
    bgcolor=ft.Colors.GREY_300,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
    on_click= lambda e: cambiar_vista(listado_repuestos())
)
boton_guardar=ft.Button(
    content=Text("Guardar", 20, ft.Colors.WHITE),
    disabled=True,
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
    on_click= lambda e: cambiar_vista(listado_repuestos())
)

async def  seleccionar_foto(e):
    
    def eliminar_foto():
        foto_repuesto.content=[]
        foto_repuesto.content=estado_incial_foto()
    file_picker=ft.FilePicker()
    foto_seleccionada= await file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE)
    if foto_seleccionada:
        image=ft.Image(
            width=180,
            height=210,
            border_radius=10,
            src= foto_seleccionada[0].path
        )
        boton_x=ft.Container(
                content=ft.IconButton(
                    icon=ft.Icons.CANCEL,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e: eliminar_foto()
                )
            )
        foto_repuesto.content=[]
        foto_repuesto.on_click=False
        foto_repuesto.content=ft.Stack(
            controls=[
                image,
                boton_x
            ]
        )
        
def estado_incial_foto():
    return ft.Container(
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(ft.Icons.UPLOAD, size=40, color=ft.Colors.GREY_400),
                ft.Text("Subir foto", size=12, color=ft.Colors.BLACK),
                ft.Text("JPG o PNG", size=10, color=ft.Colors.GREY_600)
            ]
        ),
        on_click= seleccionar_foto,
        ink=True
    )
foto_repuesto = ft.Container(
    width=180,
    height=210,
    border_radius=10,
      border=ft.border.all(1, ft.Colors.GREY_500),
    content=ft.Stack(
        controls=[
            estado_incial_foto()
        ]
    )
)

nombres_repuesto=ft.TextField(
    hint_text="",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    on_change= lambda e: validar_campos_llenos()
)
codigo_repuesto=ft.TextField(
    hint_text="",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    on_change= lambda e: validar_campos_llenos()
)
cantidad_repuesto= ft.TextField(
    hint_text="",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    on_change= lambda e: validar_campos_llenos()
    
) 
precio_repuestp= ft.TextField(
    hint_text="",
    border_color= ft.Colors.BLACK,
    color= ft.Colors.BLACK,
    on_change=lambda e: validar_campos_llenos()
)

#Pendiente
text_correo=Text("Correo Electrónico", 20 , ft.Colors.BLACK, "w400")
correo_personal=ft.TextField(
    width=675,
    hint_text="Ejemplo: automotrizvelastegui@gmail.com",
    border_color= ft.Colors.BLACK,
    color=ft.Colors.BLACK, 
    on_change=lambda e: validar_campos_llenos()
)
check_box_correo=ft.Checkbox(
    value=True,
    label="Registrar un Correo Electrónico",
    label_style=ft.TextStyle(color=ft.Colors.BLACK),
    border_side=ft.BorderSide(2, ft.Colors.BLACK),
    on_change= validacion_checkbox
)         

#principal, aqui se consruye todo par apoder mostrar en pantalla,
#se hizo asi para poder reutilizar codigo para editar la info
formulario=ft.Container(
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
                                foto_repuesto
                            )
                        )
                        ]),
                ft.Column(
                    scroll= ft.ScrollMode.AUTO,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    expand=True,
                    controls=[
                        Text("Datos del Nuevo Repuesto", 30, ft.Colors.BLACK, "w500"),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=30,
                            controls=[
                                ft.Column(
                                    controls=[
                                        Text("Nombre", 20, ft.Colors.BLACK, "w400"),
                                        nombres_repuesto
                                        
                                    ]
                                ),
                                ft.VerticalDivider(),
                                ft.Column(
                                    controls=[
                                        Text("Código", 20, ft.Colors.BLACK, "w400"),
                                        codigo_repuesto
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
                                        Text("Cantidad", 20, ft.Colors.BLACK, "w400"),
                                        cantidad_repuesto    
                                    ]
                                ),
                                ft.VerticalDivider(),
                                ft.Column(
                                    controls=[
                                        Text("Precio", 20, ft.Colors.BLACK, "w400"),
                                        precio_repuestp
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
                        )
                    ]
                )
            ]
        )
    )
)

def resgistrar_repuesto():
    #construye la pantalla para agregar clientes, si se necesit algo mas se puede agregar aqui               
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                Text("Registrar Nuevo Repuesto", 35, ft.Colors.BLACK, "w500" ),
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
def listado_repuestos():
    #misma logica que se estructuro para el listado de vehiculos
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        Text("Repuestos Registrados",35,ft.Colors.BLACK,"w500"),
                        ft.Container(expand=True),
                        ft.Button(
                            Text("Nuevo Repuesto", color=ft.Colors.WHITE),
                            Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                            bgcolor=ft.Colors.BLUE_700,
                            on_click= lambda e: cambiar_vista(resgistrar_repuesto())
                            )
                        ]
                    ),
                ft.Divider(height=10, color=ft.Colors.BLACK)
            ]
        )
    )


def view_repuestos(page: ft.Page):
    #retorna al dashboard
    pantalla_repuestos.controls=[listado_repuestos()]
    return pantalla_repuestos

#Faltan campo#corregir nombres de variables