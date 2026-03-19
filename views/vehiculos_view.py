import flet as ft
from models import *
from views import *
import json
import datetime as dt
#variable que se edita para poder cambbiar entre pantalla sin modificar la barra superior o las notificacioes
pantalla_vehiculos=ft.Column(expand=True)

ruta=os.path.join("assets", "Config.json")
fecha_actual= dt.datetime.now().strftime('%d/%m/%Y')

def cargar_datos():
    with open(ruta, "r", encoding="UTF-8") as f:
        return json.load(f)

config=cargar_datos()
MARCAS_VEHICULOS=config["marcas_vehiculos"]
COLORES_VEHICULOS=config["colores_vehiculos"]
TIPOS_VEHICULOS= config["tipos_vehiculos"]
vehiculos_actuales=[]

#funcion temporal con json quye me permite agregar los modelos de los vehiculos segun la marca
#esto se debe hacer en un catalogo con la db para poder manejar de mejor maner ala info
def cargar_vehiculos(marca):
    validar_campos_llenos()
    if marca and marca in MARCAS_VEHICULOS:
        vehiculos_actuales.clear()
        for i in MARCAS_VEHICULOS[marca]:
            
            vehiculos_actuales.append(i)
        modelo_vehiculo.options=[ft.dropdown.Option(text= m, style=ft.TextStyle(color="black")) for m in vehiculos_actuales]
    else:
        modelo_vehiculo.options=[ft.dropdown.Option(text=[])]


#funcion temporal que guarda los datos en un jsonn, en un futurop esto se tiene que almcenar en una db, logica de prueba
def guardar_datos(marca="", modelo="",tipo_nuevo="" ,color_nuevo=""):
    if marca and marca not in MARCAS_VEHICULOS and marca != "":
        config["marcas_vehiculos"][marca]= []
        marca_vehiculo.options.append(
            ft.dropdown.Option(text=marca, style=(ft.TextStyle(color="black")))
        )
 
    if modelo and marca and modelo not in MARCAS_VEHICULOS[marca] and modelo != "":
        MARCAS_VEHICULOS[marca].append(modelo)
        modelo_vehiculo.options.append(
            ft.dropdown.Option(text=modelo, style=ft.TextStyle(color="black"))
        )
    
    if tipo_nuevo and tipo_nuevo not in TIPOS_VEHICULOS and tipo_nuevo != "":
        TIPOS_VEHICULOS.append(tipo_nuevo)
        tipo_vehiculo.options.append(
            ft.dropdown.Option(text=tipo_nuevo, style=ft.TextStyle(color="black"))
        )
        
    if color_nuevo and color_nuevo not in COLORES_VEHICULOS and color_nuevo != "":
        COLORES_VEHICULOS.append(color_nuevo)
        color_vehiculo.options.append(
            ft.dropdown.Option(text=color_nuevo, style=ft.TextStyle(color="black"))
        )    
    with open(ruta, "w", encoding="UTF-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    

#funcion de prueba valida solo campos llenos, en un futuro tiene que validar todo y enviar un error
def validar_campos_llenos():
    if (marca_vehiculo.text
        and modelo_vehiculo.text
        and placa_vehiculo.value
        and año_vehiculo.value
        and tipo_vehiculo.text
        and color_vehiculo.text
        ):
        boton_guardar.disabled=False
    else:
        boton_guardar.disabled=True    
    
        
def limpiar_formulario():
    #agregar aqui todo para poder restablecer el formulario y poder seguir guardando datos, ojo(faltan algunos datos)
    marca_vehiculo.value=""
    modelo_vehiculo.value=""
    placa_vehiculo.value=""
    año_vehiculo.value=""
    tipo_vehiculo.value=""
    color_vehiculo.value=""
    
    checkbox_agregar_reparacion.value=True
    
    text_fecha_entrada.color=ft.Colors.BLACK
    fecha_entrada.color=ft.Colors.BLACK
    calendario_entrada.disabled=False
    calendario_entrada.icon_color=ft.Colors.BLUE_700
    fecha_entrada.value=fecha_actual
    
    text_fecha_entrega.color=ft.Colors.BLACK
    fecha_entrega.color=ft.Colors.BLACK
    calendario_entrega.icon_color=ft.Colors.BLUE_700
    calendario_entrega.disabled=False
    fecha_entrega.value=fecha_actual
    
    suffix_kilometraje_actual.color=ft.Colors.BLACK
    text_kilometraje_actual.color=ft.Colors.BLACK
    kilometraje_actual.color=ft.Colors.BLACK
    kilometraje_actual.read_only= False
    kilometraje_actual.value=""
    
    suffix_siguiente_kilometraje.color=ft.Colors.BLACK
    text_siguiente_kilometraje.color=ft.Colors.BLACK
    siguiente_kilometraje.color=ft.Colors.BLACK
    siguiente_kilometraje.read_only=False
    siguiente_kilometraje.value=""
    
    lista_reparaciones_realizadas.controls.clear()
    
    
    
def cambiar_vista(nueva_vista):
    boton_guardar.disabled=True
    limpiar_formulario()
    pantalla_vehiculos.controls.clear()
    pantalla_vehiculos.controls.append(nueva_vista)
    pantalla_vehiculos.update()    

#variables que se usan para la interfax el formulario del vehiculo
boton_cancelar= ft.Button(
    content=Text("Cancelar",20, ft.Colors.BLACK),
    bgcolor=ft.Colors.GREY_300,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=1)),
    on_click= lambda e: cambiar_vista(listado_vehiculos())
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
    on_click= lambda e: [cambiar_vista(listado_vehiculos()),guardar_datos(
        marca_vehiculo.text,
        modelo_vehiculo.text,
        tipo_vehiculo.text,
        color_vehiculo.text
        )
    ]
)
marca_vehiculo= ft.Dropdown(
    width=300,
    hint_text="Seleccione una Marca de un Vehiculo",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    editable=True,
    options=[ft.dropdown.Option(text= v, style=(ft.TextStyle(color="black"))) for v in MARCAS_VEHICULOS],
    on_select= lambda e: cargar_vehiculos(marca_vehiculo.text),
    on_blur= lambda e: cargar_vehiculos(marca_vehiculo.text)
)
modelo_vehiculo= ft.Dropdown(
    width=300,
    hint_text="Seleccione un Modelo de un Vehiculo",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    on_text_change= lambda e: validar_campos_llenos(),
    editable= True,
    
)
placa_vehiculo=ft.TextField(
    hint_text="Ejemplo ABC-1234",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    on_change= lambda e: validar_campos_llenos()
)
año_vehiculo=ft.TextField(
    hint_text="Ejemplo: 2007",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    keyboard_type=ft.KeyboardType.NUMBER,
    max_length= 4,
    counter_style=(ft.TextStyle(size=0)),
    on_change= lambda e: validar_campos_llenos()
)
tipo_vehiculo=ft.Dropdown(
    width=300,
    hint_text="Seleccione el Tipo de Vehiculo",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    editable=True,
    options=[
        ft.dropdown.Option(text=t, style=ft.TextStyle(color="black"))for t in TIPOS_VEHICULOS
    ],
    on_text_change= lambda e: validar_campos_llenos()
    
)
color_vehiculo=ft.Dropdown(
    width=300,
    menu_height=220,
    hint_text="Selecione el Color del Vehiculo",
    editable=True,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    bgcolor=ft.Colors.WHITE,
    options=[
        ft.dropdown.Option(text=c, style=ft.TextStyle(color="black"))for c in COLORES_VEHICULOS
    ],
    on_text_change= lambda e: validar_campos_llenos()
)

def interfaz_checkbox_vehiculos():
    #restablece algunos campos funciona de la misma manera que la funcion de limpiar campos
    fecha_entrada.value=fecha_actual
    fecha_entrega.value=fecha_actual
    kilometraje_actual.value=""
    siguiente_kilometraje.value=""
    
    #desabilitar y habilitar los campos de trabajos
    #ojo faltan algunos campos
    if checkbox_agregar_reparacion.value==True:
        
        text_fecha_entrada.color=ft.Colors.BLACK
        fecha_entrada.color=ft.Colors.BLACK
        calendario_entrada.icon_color=ft.Colors.BLUE_700
        calendario_entrada.disabled=False
        
        text_fecha_entrega.color=ft.Colors.BLACK
        fecha_entrega.color=ft.Colors.BLACK
        calendario_entrega.icon_color=ft.Colors.BLUE_700
        calendario_entrega.disabled=False
        
        suffix_kilometraje_actual.color=ft.Colors.BLACK
        text_kilometraje_actual.color=ft.Colors.BLACK
        kilometraje_actual.color=ft.Colors.BLACK
        kilometraje_actual.read_only= False
        
        suffix_siguiente_kilometraje.color=ft.Colors.BLACK
        text_siguiente_kilometraje.color=ft.Colors.BLACK
        siguiente_kilometraje.color=ft.Colors.BLACK
        siguiente_kilometraje.read_only=False
        
        boton_agregar_reparacion.disabled=False 
        boton_eliminar_reparacion.disabled=False  
        
    else:
        
        text_fecha_entrada.color=ft.Colors.GREY_400
        fecha_entrada.color=ft.Colors.GREY_400
        calendario_entrada.icon_color=ft.Colors.GREY_400
        calendario_entrada.disabled=True
        
        text_fecha_entrega.color=ft.Colors.GREY_400
        fecha_entrega.color=ft.Colors.GREY_400
        calendario_entrega.icon_color=ft.Colors.GREY_400
        calendario_entrega.disabled=True
        
        suffix_kilometraje_actual.color=ft.Colors.GREY_400
        text_kilometraje_actual.color=ft.Colors.GREY_400
        kilometraje_actual.color=ft.Colors.GREY_400
        kilometraje_actual.read_only= True
        
        suffix_siguiente_kilometraje.color=ft.Colors.GREY_400
        text_siguiente_kilometraje.color=ft.Colors.GREY_400
        siguiente_kilometraje.color=ft.Colors.GREY_400
        siguiente_kilometraje.read_only=True

        boton_agregar_reparacion.disabled=True
        boton_eliminar_reparacion.disabled=True

#def para poder abrir los calendario y poder elegir una fecha 
def abrir_calendario(e, campo_text):
    
    def poner_fecha_en_texto(evt):
        
        if evt.control.value:
            campo_text.value = evt.control.value.strftime('%d/%m/%Y')
    #empíeza asi para poder agregar segun el campo que se ncesite, se puede usar en un futuro
    first_date = None
    last_date = None
    #agrega los limites de fechas segun el data de la variable que almacena el texfield para ingresar la fecha
    if campo_text.data == "entrada":
        first_date = dt.datetime(2026, 1, 1)
        last_date = dt.datetime.now()
    elif campo_text.data == "entrega":
        first_date = dt.datetime.now()
    
    calendario_dinamico = ft.DatePicker(
        on_change=poner_fecha_en_texto,
        locale=ft.Locale("es","ES"),
        cancel_text="Cancelar",
        confirm_text="Confirmar",
        entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
        first_date=first_date,
        last_date=last_date
    )
    
    e.page.overlay.append(calendario_dinamico)
    e.page.update()
    calendario_dinamico.open = True
    e.page.update()


    
#Variables para el formulario de agregar Reparaciones
checkbox_agregar_reparacion=ft.Checkbox(
    label="Registrar una Reparación",
    value=True,
    label_style=ft.TextStyle(color=ft.Colors.BLACK),
    border_side=ft.BorderSide(2,ft.Colors.BLACK),
    on_change=interfaz_checkbox_vehiculos
)

text_fecha_entrada=Text("Fecha de Ingreso", 20, ft.Colors.BLACK, "w400" )
calendario_entrada=ft.IconButton(
    icon=ft.Icons.CALENDAR_MONTH, 
    icon_color=ft.Colors.BLUE_700,
    style=ft.ButtonStyle(
        overlay_color=ft.Colors.BLUE_100
    ),
    disabled=False,
    on_click= lambda e: abrir_calendario(e, fecha_entrada)
)
fecha_entrada= ft.TextField(
    hint_text="DD/MM/YYYY",
    height=50,
    value= fecha_actual,
    suffix=calendario_entrada,
    color= ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only= True,
    data="entrada"
)

text_fecha_entrega=Text("Fecha de Entrega", 20, ft.Colors.BLACK, "w400")
calendario_entrega=ft.IconButton(
    icon=ft.Icons.CALENDAR_MONTH, 
    icon_color=ft.Colors.BLUE_700,
    style=ft.ButtonStyle(
        overlay_color=ft.Colors.BLUE_100
    ),
    disabled=False,
    on_click= lambda e: abrir_calendario(e, fecha_entrega)
)
fecha_entrega=ft.TextField(
    hint_text="DD/MM/YYYY",
    height=50,
    suffix=calendario_entrega,
    value=fecha_actual,
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only=True,
    data="entrega"
)

def calcular_kilometraje():
    #funcion que me permite calcular automaticamente el proximo km sumandole el estandar que es 5000
    valor_ingresado= kilometraje_actual.value
    if valor_ingresado == "":
        siguiente_kilometraje.value=""
        return
    
    try:
        km_actual = int(valor_ingresado)
        km_calculado = km_actual + 5000
        
        siguiente_kilometraje.value = str(km_calculado)
    except ValueError:
        #permite que no me salte ningun error y se cierre el programa
        #añadir en mensaje de error para que se ingresen correctamente los diferentes campos
        pass
    
suffix_kilometraje_actual=Text("km", 20, ft.Colors.BLACK)
text_kilometraje_actual=Text("Kilometraje Actual", 20, ft.Colors.BLACK, "w400")
kilometraje_actual=ft.TextField(
    hint_text="10005",
    on_change=calcular_kilometraje,
    suffix=suffix_kilometraje_actual,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False
)

suffix_siguiente_kilometraje=Text("km", 20, ft.Colors.BLACK)
text_siguiente_kilometraje =Text("Siguiente Kilometraje", 20 ,ft.Colors.BLACK, "w400")
siguiente_kilometraje=ft.TextField(
    hint_text="15005",
    suffix=suffix_siguiente_kilometraje,
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False
)

def agregar_nueva_reparacion():
    #funcion que me permite agregar mas text field para poder agregar mas reparaciones y su costo
    #agregar funcion que permita calcular el total "tambien el precio de repuestos"
    lista_reparaciones_realizadas.controls.append(
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    hint_text="Detalles de la reparación realizada",
                    border_color=ft.Colors.BLACK,
                    color=ft.Colors.BLACK,
                    read_only=False
                ),
                ft.VerticalDivider(),
                ft.TextField(
                    hint_text="25",
                    suffix=suffix_precio_reparacion,
                    color=ft.Colors.BLACK,
                    border_color=ft.Colors.BLACK,
                    read_only=False
                )
            ]
        )
    )
    
    if len(lista_reparaciones_realizadas.controls) > 0:
        boton_eliminar_reparacion.disabled=False


def eliminar_campos_reparaciones():
    #permite eliminar el ultimo campo de reaparacion ademas desabilita el boton de eliminar
    if len(lista_reparaciones_realizadas.controls) > 0:
        boton_eliminar_reparacion.disabled=False
        lista_reparaciones_realizadas.controls.pop(-1)

    if len(lista_reparaciones_realizadas.controls) == 0:
        boton_eliminar_reparacion.disabled=True


def print_prueba():
    #logica de prueba para poder almacenar los datos de las reparaciones y costos en una lista,
    #tiene que recorrer los value y estos agregar en una sola lista ademas de borrarse todo en el apartado de limpiar formulario
    
    print(reaparacion_obligatorio.value)
    for e in lista_reparaciones_realizadas.controls:
        print(e.controls[0].value)

text_reparaciones=Text("Reparaciones Realizadas", 20, ft.Colors.BLACK, "w400")
lista_reparaciones_realizadas=ft.Column()
reaparacion_obligatorio=ft.TextField(
    hint_text="Detalles de la reparación realizada",
    border_color=ft.Colors.BLACK,
    color=ft.Colors.BLACK,
    read_only=False
)

suffix_precio_reparacion=Text("$", 20, ft.Colors.BLACK)
text_precio_reparacion=Text("Precio", 20, ft.Colors.BLACK,"w400")
precio_reaparacion=ft.TextField(
    hint_text="25",
    suffix=suffix_precio_reparacion,
    color=ft.Colors.BLACK,
    border_color=ft.Colors.BLACK,
    read_only=False
)

boton_agregar_reparacion=ft.Button(
    content=Text("Agregar Nueva Reparación", 15, ft.Colors.WHITE, "w500"),
    icon= Icon(ft.Icons.ADD, ft.Colors.WHITE, 25),
    bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.GREEN,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
        
    },
    on_click=lambda e: agregar_nueva_reparacion()
)


boton_eliminar_reparacion=ft.Button(
    content=Text("Eliminar Última Reparación", 15, ft.Colors.WHITE, "w500"),
    icon=Icon(ft.Icons.DELETE, ft.Colors.WHITE, 25),
    bgcolor={
        ft.ControlState.DEFAULT: ft.Colors.RED,
        ft.ControlState.DISABLED: ft.Colors.GREY_400
    },
    disabled=True,
    on_click= lambda e: eliminar_campos_reparaciones()
    
    
)
formulario_reparaciones=ft.Column(
    #aqui se agregan los campos necesarios para poder registrar nuevas reparaciones, 
    #asignado en una variable diferente para poder agregar en un alert dialog
    expand=True,
    controls=[
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        text_fecha_entrada,
                        ft.Row(
                            controls=[
                                fecha_entrada
                            ]
                        )
                        
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_fecha_entrega,
                        ft.Row(
                            controls=[
                                fecha_entrega
                            ]
                        )
                        
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
                        text_kilometraje_actual,
                        kilometraje_actual
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_siguiente_kilometraje,
                        siguiente_kilometraje
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
                        text_reparaciones,
                        reaparacion_obligatorio,
                    ]
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        text_precio_reparacion,
                        precio_reaparacion
                        
                    ]
                )
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                lista_reparaciones_realizadas
            ]
        ),
        ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                boton_agregar_reparacion,
                boton_eliminar_reparacion,
                ft.Button(
                    "hola",on_click= lambda e: print_prueba()
                )
            ]
        )
    ]
    
)
formulario_vehiculos=ft.Container(
    #permite agregar los campos necesarios para poder registrar un vehiculo, son campos necesario
    #falt agregar la asociacion de un cliente, esto se hara caundos e tenga los datos almacenados en la db
    bgcolor=ft.Colors.GREY_200,
    width=800,
    height=1000,
    padding=15,
    border_radius=15,
    shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
    content=(
        ft.Column(
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
            expand=True,
            controls=[
                Text("Datos del Vehículo", 30, ft.Colors.BLACK, "w500"),
                ft.Divider(),
                ft.Row(
                    spacing=30,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Column(
                            controls=[
                                Text("Marca del Vehículo", 20, ft.Colors.BLACK, "400"),
                                marca_vehiculo
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Modelos de los Vehiculos", 20, ft.Colors.BLACK, "w400"),
                                modelo_vehiculo
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
                                Text("Placa del Vehículo", 20, ft.Colors.BLACK, "w400"),
                                placa_vehiculo
                            ]
                        ),
                        ft.VerticalDivider(),
                        ft.Column(
                            controls=[
                                Text("Año del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                año_vehiculo
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
                                Text("Tipo Del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                tipo_vehiculo
                            ]
                        ),
                        ft.VerticalDivider(), 
                        ft.Column(
                            controls=[
                                Text("Color del Vehiculo", 20, ft.Colors.BLACK, "w400"),
                                color_vehiculo
                            ]
                        )
                    ]
                ),
                ft.Row(
                    spacing=30,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        checkbox_agregar_reparacion,
                        ft.VerticalDivider(),
                        ft.Container(width=420)
                    ]
                ),
                formulario_reparaciones 
            ]
        )
    )
)

def agregar_vehículo():
    #aqui va lo principal que se necesita en el apartado de agregar un vehiculo, tal vez se modifique un poco para que sea mas estetico
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                Text("Registrar Nuevo Vehículo", 35, ft.Colors.BLACK, "w500" ),
                ft.Divider(),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True,
                    controls=[formulario_vehiculos]
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

def listado_vehiculos():
    #aqui se agregara la lista de vehiculos registrados, ademas de poder aditar la informacion de los datos registrados
    #IDEA: crear varias filas en la que aparezca el nombre o modelo del vehiculo y en el momento de hacer clickk se pueda 
    #editar la info registrada, por eso separe algunos campos, esperemos funcione :(
    return ft.Container(
        expand= True,
        bgcolor=ft.Colors.WHITE,
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        Text("Vehículos Registrados",35,ft.Colors.BLACK,"w500"),
                        ft.Container(expand=True),
                        ft.Button(
                            Text("Agregar Nuevo Vehículo", color=ft.Colors.WHITE),
                            Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                            bgcolor=ft.Colors.BLUE_700,
                            on_click= lambda e: cambiar_vista(agregar_vehículo())
                            )
                        ]
                    ),
                ft.Divider(height=10, color=ft.Colors.BLACK)
            ]
        )
    )

def view_vehiculos(page: ft.Page):
    #retorna al dashboard toda la pantalla principal(lsitado de vehiculos)
    pantalla_vehiculos.controls=[listado_vehiculos()]
    return pantalla_vehiculos