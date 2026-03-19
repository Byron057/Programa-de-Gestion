import flet as ft
from models import *
import json
import os
#variable que muestra la pantalla 
pantalla_clientes=ft.Column(expand=True)

ruta= os.path.join("assets", "config.json")

def cargar_datos():
    with open(ruta, "r", encoding="UTF-8") as f:
        return json.load(f)

config= cargar_datos()
DATA_ECUADOR= config["ubicaciones"]


def limpiar_formulario():
    #reestablece los datos del formulario
    nombres_cliente.value=""
    apellidos_cliente.value=""
    cedula_cliente.value=""
    numero_telefono_cliente.value=""
    correo_clientes.value=""
    text_correo.color=ft.Colors.BLACK
    correo_clientes.color=ft.Colors.BLACK
    correo_clientes.read_only=False
    provincias.value=""
    ciudades.value=""
    direccion_cliente.value=""
    check_box_correo.value=True

def cambiar_vista(nueva_vista):
    boton_guardar.disabled=True
    limpiar_formulario()
    pantalla_clientes.controls.clear()
    pantalla_clientes.controls.append(nueva_vista)
    pantalla_clientes.update()
#variable que me permite guardar temporalmente las ciudades
ciudades_actuales=[] 

def cargar_ciudades(provincia):
    #carga las ciudades segun la provincia
    if provincia:
        ciudades_actuales.clear()
        ciudades.value=""
        validar_campos_llenos()
        for i in DATA_ECUADOR[provincia]:
            ciudades_actuales.append(i)
        
        if len(ciudades_actuales)>10:
            ciudades.menu_height=400
        else:
            ciudades.menu_height= None
        
        ciudades.options= [ft.dropdown.Option(text= c,style= ft.TextStyle(color="black")) for c in ciudades_actuales]

def validar_campos_llenos():
        #funcion incompleta en un futuro debe validar todos los campos
        if (
            nombres_cliente.value
            and apellidos_cliente.value 
            and cedula_cliente.value
            and numero_telefono_cliente.value 
            and correo_clientes.value 
            and provincias.value
            and ciudades.value
            and direccion_cliente.value
        ):
            boton_guardar.disabled=False
        else:
            boton_guardar.disabled=True

def validacion_checkbox():
    #funcion que me permite registtrar o no un correo electronico
    correo_clientes.value = ""
    
    if check_box_correo.value:
        text_correo.color= ft.Colors.BLACK
        correo_clientes.color= ft.Colors.BLACK
        correo_clientes.read_only = False
        
    else:
        correo_clientes.read_only = True
        correo_clientes.color= ft.Colors.GREY_400
        text_correo.color=ft.Colors.GREY_400
        #por el momento me registra esto para no tener conflictos en las validaciones, posiblemente cambie la logica
        correo_clientes.value = "N/A"

    validar_campos_llenos()

#variables que se usan en el formulario de los clientes
#falta asociar o no a un vehiculo esto se hara en el momento enel que tenga registtrado en la db

boton_cancelar= ft.Button(
    content=Text("Cancelar",20, ft.Colors.BLACK),
    bgcolor=ft.Colors.GREY_300,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
    on_click= lambda e: cambiar_vista(listado_clientes())
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
    on_click= lambda e: cambiar_vista(listado_clientes())
)
nombres_cliente=ft.TextField(
    hint_text="Ejemplo: Luis Fernando",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    on_change= lambda e: validar_campos_llenos()
)
apellidos_cliente=ft.TextField(
    hint_text="Ejemplo: Pérez Salazar",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    capitalization=ft.TextCapitalization.WORDS,
    on_change= lambda e: validar_campos_llenos()
)
cedula_cliente= ft.TextField(
    hint_text="Ejemplo: 0503456764",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    on_change= lambda e: validar_campos_llenos()
    
) 
numero_telefono_cliente= ft.TextField(
    hint_text="Ejmplo: 0998743567",
    border_color= ft.Colors.BLACK,
    color= ft.Colors.BLACK,
    on_change=lambda e: validar_campos_llenos()
)
text_correo=Text("Correo Electrónico", 20 , ft.Colors.BLACK, "w400")
correo_clientes=ft.TextField(
    width=675,
    hint_text="Ejemplo: automotrizvelastegui@gmail.com",
    border_color= ft.Colors.BLACK,
    color=ft.Colors.BLACK, 
    on_change=lambda e: validar_campos_llenos()
)
provincias= ft.Dropdown(
    menu_height=400,
    width= 300, 
    hint_text="Seleccione una Provincia",
    options=[ft.dropdown.Option(text=p, style=ft.TextStyle(color="black")) for p in DATA_ECUADOR],
    color= ft.Colors.BLACK,
    border_color= ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    on_select= lambda e: cargar_ciudades(provincias.value),
    on_text_change= lambda e: validar_campos_llenos()
)
ciudades= ft.Dropdown(
    width= 300,
    hint_text="Seleccione una Ciudad",
    color= ft.Colors.BLACK,
    border_color= ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    on_blur=lambda e: validar_campos_llenos(),
    on_text_change= lambda e: validar_campos_llenos()
)
direccion_cliente= ft.TextField(
    width=675,
    hint_text="Ejemplo: San Felipe, UTC",
    border_color= ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    on_change= lambda e: validar_campos_llenos()
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
                                Text("Nombres del Cliente", 20, ft.Colors.BLACK, "w400"),
                                nombres_cliente
                                
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Apellidos del Cliente", 20, ft.Colors.BLACK, "w400"),
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
                                correo_clientes
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
                ft.Divider(height=10, color=ft.Colors.BLACK)
            ]
        )
    )


def view_clientes(page: ft.Page):
    #retorna al dashboard
    pantalla_clientes.controls=[listado_clientes()]
    return pantalla_clientes
    
def Form_global(page: ft.Page):
    #prueba para ver el funcionamiento, debe agregarse botones de cancelar y guardar
    #ademas los campos se deben llenar automaticamente coon la info ya registrada para poder editar
    formulario_global=page.show_dialog(
        ft.AlertDialog(
            content=formulario
        )
    )
    return formulario_global