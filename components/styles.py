import flet as ft
import asyncio
class Icon(ft.Icon):
    def __init__(self, icon, color, size=None):
        super().__init__(icon,color,size)
        self.icon=icon
        self.color=color
        self.size=size
        
class Text(ft.Text):
    def __init__(self, text, size=None,color=None , weight=None,height=None):
        super().__init__()
        self.value=text
        self.color=color
        self.size=size
        self.weight=weight
        self.height=height

async def alerta_error(e, text_error):

    dialog = ft.AlertDialog(
    modal=True,
    bgcolor=ft.Colors.WHITE,
    shape=ft.RoundedRectangleBorder(radius=15),

    content=ft.Container(
        width=350,
        height=250,
        padding=20,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            [
                ft.Container(
                    width=80,
                    height=80,
                    border_radius=50,
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.RED_50,
                    content=ft.Icon(
                        ft.Icons.ERROR_OUTLINE,
                        size=50,
                        color=ft.Colors.RED_400
                    )
                ),

                ft.Text(
                    "Error",
                    size=30,
                    weight="bold",
                    text_align="center",
                    color=ft.Colors.BLACK
                ),

                ft.Text(
                    "Ocurrió un error al procesar la solicitud",
                    size=17,
                    weight=ft.FontWeight.W_400,
                    text_align="center",
                    color=ft.Colors.GREY_700
                ),
                ft.Text(
                    text_error,
                    size=14,
                    text_align="center",
                    color=ft.Colors.GREY_700
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )
)

    e.page.show_dialog(dialog)
    dialog.open = True
    e.page.update()

    await asyncio.sleep(3)

    dialog.open = False
    e.page.update()
    
async def save_alert(e):
    dialog = ft.AlertDialog(
    modal=True,
    bgcolor=ft.Colors.WHITE,
    shape=ft.RoundedRectangleBorder(radius=15),

    content=ft.Container(
        width=350,
        height=250,
        padding=20,
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            [
                ft.Container(
                    width=80,
                    height=80,
                    border_radius=50,
                    alignment=ft.Alignment.CENTER,
                    bgcolor=ft.Colors.RED_50,
                    content=ft.Icon(
                        ft.Icons.CHECK_CIRCLE_OUTLINE,
                        size=50,
                        color=ft.Colors.GREEN_400
                    )
                ),

                ft.Text(
                    "¡Registro Exitoso!",
                    size=30,
                    weight="bold",
                    text_align="center",
                    color=ft.Colors.BLACK
                ),

                ft.Text(
                    "Los datos se guardaron correctamente en el sistema",
                    size=17,
                    weight=ft.FontWeight.W_400,
                    text_align="center",
                    color=ft.Colors.GREY_700
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )
)

    e.page.show_dialog(dialog)
    dialog.open = True
    e.page.update()

    await asyncio.sleep(3)

    dialog.open = False
    e.page.update()