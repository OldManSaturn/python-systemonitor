import flet as ft

def create_text_component(label, value):
    return ft.Text(f"{label}: {value}", size=14, weight=ft.FontWeight.NORMAL)

def create_heading(text):
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_500)
