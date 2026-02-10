import flet as ft
from decouple import config


def view_login(page: ft.Page) -> ft.View:
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(src="assets/fondo_login.jpg", fit=ft.BoxFit.COVER)
    )

    def login_principal(_):
        email.error = None
        password.error = None

        if not email.value:
            email.error = "Campo Obligatorio"
        elif email.value != config("Email"):
            email.error = "Usuario Incorrecto"
        else:
            if not password.value:
                password.error = "Campo Obligatorio"
            elif password.value != config("Password"):
                password.error = "Contraseña Incorrecta"
            else:
                page.go("/dashboard")

        page.update()

    def verificacion_email(_):
        codigo1 = "123"
        if ingresar_codigo.value != codigo1:
            ingresar_codigo.error = "Codigo incorrecto"
            ingresar_codigo.update()
        else:
            page.pop_dialog()
            cambio_contrasena()

    def proceso_recuperacion(e):
        columna = e.control.parent
        columna.controls.remove(e.control)
        columna.controls.append(ft.Text("Revisa tu Correo", color=ft.Colors.BLACK))
        columna.controls.append(
            ft.ElevatedButton("Verificar Código", on_click=verificacion_email)
        )
        columna.update()

    def recuperar_contrasena(_):
        nonlocal ingresar_codigo
        ingresar_codigo = ft.TextField(
            "", color=ft.Colors.BLACK, border_color=ft.Colors.BLACK
        )
        boton_recuperar = ft.ElevatedButton(
            "Enviar Codigo de Verificación", on_click=proceso_recuperacion
        )

        page.show_dialog(
            ft.AlertDialog(
                open=True,
                bgcolor=ft.Colors.WHITE,
                title=ft.Text(
                    "Recuperación de Contraseña",
                    color=ft.Colors.BLACK,
                    text_align="Center",
                ),
                content=ft.Container(
                    width=300,
                    height=300,
                    content=ft.Column(
                        [
                            ft.Text(
                                "Hemos enviado un código de verificación a tu correo electrónico registrado\n"
                                f"{config('email_reciver')}.\n"
                                "Por favor, ingrésalo a continuación para poder recuperar el Acceso al Sistema",
                                color=ft.Colors.BLACK,
                                text_align="center",
                            ),
                            ft.Text(
                                "Ingresa tu código de Verificación aqui:",
                                color=ft.Colors.BLACK,
                                weight="w500",
                            ),
                            ingresar_codigo,
                            boton_recuperar,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                actions=[
                    ft.TextButton(
                        "Cancelar",
                        on_click=lambda e: page.pop_dialog(),
                        style=ft.ButtonStyle(color=ft.Colors.BLACK),
                    )
                ],
            )
        )

    def cambio_contrasena():
        page.show_dialog(
            ft.AlertDialog(
                open=True,
                bgcolor=ft.Colors.WHITE,
                title=ft.Text(
                    "Cambio de Contraseña", color=ft.Colors.BLACK, text_align="Center"
                ),
                content=ft.Container(
                    width=300,
                    height=300,
                    content=ft.Column(
                        [
                            ft.Text(
                                "Ingresa tu Nueva Contraseña",
                                color=ft.Colors.BLACK,
                                text_align="Center",
                            ),
                            ft.TextField(
                                "", color=ft.Colors.BLACK, border_color=ft.Colors.BLACK
                            ),
                        ]
                    ),
                ),
            )
        )

    ingresar_codigo = ft.TextField()

    icon_principal = ft.Image(src="assets/logo_principal.png", width=120, height=120)
    text = ft.Text("Iniciar Sesión", size=35, weight="w500")
    email = ft.TextField(
        label="Correo",
        label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="w500"),
        border_color=ft.Colors.BLACK,
        width=300,
        color=ft.Colors.BLACK,
        prefix_icon=ft.Icons.EMAIL,
    )
    password = ft.TextField(
        label="Conraseña",
        label_style=ft.TextStyle(color=ft.Colors.BLACK, weight="w500"),
        border_color=ft.Colors.BLACK,
        width=300,
        color=ft.Colors.BLACK,
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
    )

    boton = ft.ElevatedButton(content=ft.Text("Iniciar Sesión"), on_click=login_principal)

    recuperar_contrasena_text = ft.Row(
        [
            ft.Text("Olvidaste tu contraseña  |", color=ft.Colors.BLACK),
            ft.TextButton(
                "Recuperar Contraseña",
                style=ft.ButtonStyle(color=ft.Colors.BLACK),
                on_click=recuperar_contrasena,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    login_container = ft.Container(
        width=500,
        height=700,
        border_radius=20,
        bgcolor=ft.Colors.BLUE,
        content=ft.Column(
            [
                icon_principal,
                text,
                email,
                password,
                recuperar_contrasena_text,
                boton,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=50,
        ),
    )

    return ft.View(
        route="/login",
        controls=[login_container],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
