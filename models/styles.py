import flet as ft
class Icon(ft.Icon):
    def __init__(self, icon, color, size=None):
        super().__init__(icon,color,size)
        self.icon=icon
        self.color=color
        self.size=size
        
class Text(ft.Text):
    def __init__(self, text, size,color=None , weight=None,height=None):
        super().__init__()
        self.value=text
        self.color=color
        self.size=size
        self.weight=weight
        self.height=height