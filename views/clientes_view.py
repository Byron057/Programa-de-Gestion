import flet as ft
from models import *
 

def view_clientes(page: ft.Page):
   
    pantalla_clientes=ft.Column(expand=True)
    
    def agregar_clientes():
        return ft.Container(
            expand= True,
            bgcolor=ft.Colors.AMBER
        )
    def listado_clientes():
        return ft.Container(
            expand= True,
            bgcolor=ft.Colors.WHITE,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            Text("Clientes",35,ft.Colors.BLACK,"w500"),
                            ft.Container(expand=True),
                            ft.ElevatedButton(
                                Text("Agregar Nuevo Cliente", color=ft.Colors.WHITE),
                                Icon(ft.Icons.ADD, ft.Colors.WHITE,20),
                                bgcolor=ft.Colors.BLUE_700,
                                on_click= lambda e:( 
                                    pantalla_clientes.controls.clear(),
                                    pantalla_clientes.controls.append(agregar_clientes())
                                    )
                                )
                            ]
                        ),
                    ft.Divider(height=10, color=ft.Colors.BLACK)
                ]
            )
        )
    
    pantalla_clientes.controls=[listado_clientes()]
    return pantalla_clientes
    
