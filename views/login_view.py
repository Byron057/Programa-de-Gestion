import flet as ft
from decouple import config
import services
import views
def view_login(page: ft.Page):
     page.vertical_alignment="center"
     page.horizontal_alignment="center"
     page.bgcolor=ft.Colors.TRANSPARENT
     page.decoration=ft.BoxDecoration(
          image=ft.DecorationImage(
          src="assets/fondo_login.jpg",
          fit=ft.BoxFit.COVER)
     )
     #Funcion para validar datos registrados en el archivo .env
     def login_principal():
          #Iniciar los errores en None para no tener conflictos
          email.error=None
          password.error=None
          #Logica de Validaciom
          if not email.value:
               email.error="Campo Obligatorio"
          elif email.value!=config("Email"):
               
               email.error="Usuario Incorrecto"
          else:
               if not password.value:
                    password.error="Campo Obligatorio" 
               
               elif password.value!=config("Password"):
                    password.error="Contraseña Incorrecta"
               else:
                    #Limpia la pagina(Agregar una animacion de cargando y exportar el dashboard)
                    views.view_dashboard(page)
     def verificacion_email():
          codigo1="123"
          if ingresar_codigo.value != codigo1:
               ingresar_codigo.error="Codigo incorrecto"
          else:
               page.pop_dialog()
               cambio_contraseña()
          
     def proceso_recuperacion(e):
          global codigo
          #codigo=services.email_verificaion()
          columna = e.control.parent
          columna.controls.remove(e.control) # Eliminamos el botón de enviar
          columna.controls.append(ft.Text("Revisa tu Correo",color=ft.Colors.BLACK))
          columna.controls.append(ft.ElevatedButton("Verificar Código",on_click=verificacion_email)) # Agregamos el nuevo
          columna.update()
     #Funcion de Recuperacion de Contraseña
     def recuperar_contraseña():
          global ingresar_codigo
          ingresar_codigo=ft.TextField("",color=ft.Colors.BLACK,border_color=ft.Colors.BLACK)
          boton_recuperar=ft.ElevatedButton("Enviar Codigo de Verificación",on_click=proceso_recuperacion)
          page.show_dialog(
               ft.AlertDialog(
                    open=True,
                    bgcolor=ft.Colors.WHITE,
                    title=ft.Text("Recuperación de Contraseña",color=ft.Colors.BLACK,text_align="Center"),
                    content=ft.Container(
                         width=300,
                         height=300,
                         content=ft.Column([
                              ft.Text(
                                   f"Hemos enviado un código de verificación a tu correo electrónico registrado\n"
                                   f"{config("email_reciver")}.\n" 
                                   f"Por favor, ingrésalo a continuación para poder recuperar el Acceso al Sistema",
                                   color=ft.Colors.BLACK,
                                   text_align="center"),
                              ft.Text("Ingresa tu código de Verificación aqui:",color=ft.Colors.BLACK,weight="w500"),
                              ingresar_codigo,
                              boton_recuperar],
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER)),
                                    
                    actions=[ft.TextButton(
                         "Cancelar", on_click=lambda e: page.pop_dialog(),style=ft.ButtonStyle(color=ft.Colors.BLACK))],
               )          
          )
     def cambio_contraseña():
          page.show_dialog(ft.AlertDialog(
                    open=True,
                    bgcolor=ft.Colors.WHITE,
                    title=ft.Text("Cambio de Contraseña",color=ft.Colors.BLACK,text_align="Center"),
                    content= ft.Container(
                         width=300,
                         height=300,
                         content=ft.Column([
                              ft.Text("Ingresa tu Nueva Contraseña",color=ft.Colors.BLACK,text_align="Center"),
                              ft.TextField("",color=ft.Colors.BLACK,border_color=ft.Colors.BLACK)])
                         
                    )))
     #Recursosque se utiliza en el contenedor principal del Login
     icon_principal=ft.Image(
          src="assets\logo_principal.png",
          width=120,
          height=120,
     )
     text=ft.Text(
          "Iniciar Sesión",
          size=35,
          weight="w500"    
     )
     email=ft.TextField(
          label= "Correo",
          label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="w500"),
          border_color=ft.Colors.BLACK,
          width= 300,
          color=ft.Colors.BLACK,
          prefix_icon=ft.Icons.EMAIL   
     )
     password= ft.TextField(
          label="Conraseña",
          label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="w500"),
          border_color=ft.Colors.BLACK, 
          width=300,
          color=ft.Colors.BLACK,
          prefix_icon=ft.Icons.LOCK   
     )
     Boton=ft.ElevatedButton(
          content= ft.Text("Iniciar Sesión"),
          on_click=login_principal
          
     )
     recuperar_contraseña_text=ft.Row([
          ft.Text("Oldivaste tu contraseña  |",
               color=ft.Colors.BLACK),               
          
          ft.TextButton("Recuperar Contraseña",
               style=ft.ButtonStyle(color=ft.Colors.BLACK),
               on_click= recuperar_contraseña  
          ),     
     ],
          #Al ser un Row(Contenedor Horizontal), se alinea el contenido
          alignment=ft.MainAxisAlignment.CENTER
     )

     #Contenedor principal Login se Returna para llamar en el archivo main.py
     return ft.Container(
          #Caracteristicas del Coontenedror
          width=500,
          height=700,
          border_radius=20,
          bgcolor=ft.Colors.BLUE,
          #Almacena los widgets para poder mostrar de la manera correcta
          content= ft.Column(
               [ 
               icon_principal,      
               text,
               email,
               password,
               recuperar_contraseña_text,    
               Boton
               ],
               #Posicion y alineación  de los widgets 
               alignment= ft.MainAxisAlignment.CENTER,
               horizontal_alignment=ft.CrossAxisAlignment.CENTER,
               spacing=50    
          )
     ) 