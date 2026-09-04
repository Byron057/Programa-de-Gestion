import flet as ft
import services
from decouple import config
import asyncio
from database import db_core
from controls import control_login as cl

datos = db_core.datos_login()

def view_login(page: ft.Page):
     page.theme_mode = ft.ThemeMode.DARK
     
     ingresar_codigo = ft.TextField("", color=ft.Colors.BLACK, border_color=ft.Colors.BLACK)

     # Función para validar llamando al controlador
     def validar_login(e):
          # Limpiamos los errores visuales
          email.error = None
          password.error = None
          
          # Pasamos los valores al controlador
          es_valido, campo, mensaje = cl.login_principal(email.value, password.value)
          
          if es_valido:
               asyncio.create_task(page.push_route("/dashboard"))
          else:
               # Mostramos el error en el campo correspondiente
               if campo == "email":
                    email.error = mensaje
               elif campo == "password":
                    password.error = mensaje
          
          page.update()
                    
     def verificacion_email(e):
          codigo1 = "123"
          if ingresar_codigo.value != codigo1:
               ingresar_codigo.error = "Codigo incorrecto"
               page.update()
          else:
               page.pop_dialog()
               cambio_contraseña()
          
     def proceso_recuperacion(e):
          columna = e.control.parent
          columna.controls.remove(e.control) 
          columna.controls.append(ft.Text("Revisa tu Correo", color=ft.Colors.BLACK))
          columna.controls.append(ft.ElevatedButton("Verificar Código", on_click=verificacion_email)) 
          columna.update()

     def recuperar_contraseña(e):
          boton_recuperar = ft.ElevatedButton("Enviar Codigo de Verificación", on_click=proceso_recuperacion)
          page.show_dialog(
               ft.AlertDialog(
                    open=True,
                    bgcolor=ft.Colors.WHITE,
                    title=ft.Text("Recuperación de Contraseña", color=ft.Colors.BLACK, text_align="Center"),
                    content=ft.Container(
                         width=300,
                         height=300,
                         content=ft.Column([
                              ft.Text(
                                   f"Hemos enviado un código de verificación a tu correo electrónico registrado\n"
                                   f"{datos[0][2]}.\n" 
                                   f"Por favor, ingrésalo a continuación para poder recuperar el Acceso al Sistema",
                                   color=ft.Colors.BLACK,
                                   text_align="center"
                              ),
                              ft.Text("Ingresa tu código de Verificación aqui:", color=ft.Colors.BLACK, weight="w500"),
                              ingresar_codigo,
                              boton_recuperar
                         ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                    ),
                    actions=[
                         ft.TextButton("Cancelar", on_click=lambda e: page.pop_dialog(), style=ft.ButtonStyle(color=ft.Colors.BLACK))
                    ],
               )          
          )

     def cambio_contraseña():
          page.show_dialog(
               ft.AlertDialog(
                    open=True,
                    bgcolor=ft.Colors.WHITE,
                    title=ft.Text("Cambio de Contraseña", color=ft.Colors.BLACK, text_align="Center"),
                    content= ft.Container(
                         width=300,
                         height=300,
                         content=ft.Column([
                              ft.Text("Ingresa tu Nueva Contraseña", color=ft.Colors.BLACK, text_align="Center"),
                              ft.TextField("", color=ft.Colors.BLACK, border_color=ft.Colors.BLACK)
                         ])
                    )
               )
          )

     def toggle_password(e):
        password.password = not password.password
        boton_ojo.icon = ft.Icons.VISIBILITY_OFF if password.password else ft.Icons.VISIBILITY
        page.update()

     def mostrar_ojo(e):
        boton_ojo.icon_color = ft.Colors.BLACK
        boton_ojo.disabled = False
        page.update()

     def ocultar_ojo(e):
        boton_ojo.icon_color = ft.Colors.TRANSPARENT
        boton_ojo.disabled = True
        password.password = True
        boton_ojo.icon = ft.Icons.VISIBILITY_OFF
        page.update()
     
     boton_ojo = ft.IconButton(
        icon=ft.Icons.VISIBILITY_OFF,
        icon_color=ft.Colors.TRANSPARENT,
        disabled=True,
        on_click=toggle_password
     )
     
     icon_principal = ft.Image(
          src=r"assets\logo_principal.png",
          width=120,
          height=120,
     )
     text = ft.Text(
          "Iniciar Sesión",
          size=35,
          weight="w500"    
     )
     email = ft.TextField(
          width=300,
          label="Correo",
          label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="w500"),
          border_color=ft.Colors.BLACK,
          color=ft.Colors.BLACK,
          prefix_icon=ft.Icons.EMAIL   
     )
     password = ft.TextField(
          width=300,
        label="Contraseña",
        label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="w500"),
        border_color=ft.Colors.BLACK,
        prefix_icon=ft.Icons.LOCK,  
        password=True,
        color=ft.Colors.BLACK,
        suffix_icon=boton_ojo,
        on_focus=mostrar_ojo,
        on_blur=ocultar_ojo
     )

     Boton = ft.ElevatedButton(
          content=ft.Text("Iniciar Sesión"),
          on_click=validar_login
     )

     recuperar_contraseña_text = ft.Row([
          ft.Text("Mecasoft© 2026  |", color=ft.Colors.BLACK),              
          ft.Text("Version 1.0", color=ft.Colors.BLACK),              
          #ft.TextButton(
               #"Recuperar Contraseña",
               #style=ft.ButtonStyle(color=ft.Colors.BLACK),
               #on_click=recuperar_contraseña 
          #),     
     ], alignment=ft.MainAxisAlignment.CENTER)
     
     
     return ft.View( 
          route="/",
          vertical_alignment="center",
          horizontal_alignment="center",
          bgcolor=ft.Colors.TRANSPARENT,
          decoration=ft.BoxDecoration(
               image=ft.DecorationImage(
                    src="assets/fondo_login.jpg",
                    fit=ft.BoxFit.COVER
               )
          ),
          controls=[
               ft.Container(
                    width=min(500, page.width -40),
                    height=min(700, page.height -40),
                    border_radius=20,
                    bgcolor=ft.Colors.BLUE,
                    content= ft.Column(
                         [ 
                              icon_principal,      
                              text,
                              email,
                              password,
                              recuperar_contraseña_text,    
                              Boton
                         ],
                         alignment=ft.MainAxisAlignment.CENTER,
                         horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                         spacing=50
                    )
               )
          ]
     )