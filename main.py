import flet as ft
import threading
from tabs import create_system_info_tab, create_process_list_tab
from util import update_cpu_utilization

def main(page: ft.Page):
    page.title = "System Monitor"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    cpu_utilization_texts = []

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="System Info", content=create_system_info_tab(cpu_utilization_texts)),
            ft.Tab(text="Running Processes", content=create_process_list_tab())
        ],
        expand=1
    )

    footer = ft.Container(
        content=ft.Text("Footer Text", size=16),
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.WHITE10,
        border=ft.border.all(1, color=ft.colors.BLACK),
        height=50
    )

    page.add(ft.Column([tabs, footer], expand=True))

    # Start the periodic update
    threading.Timer(1, update_cpu_utilization(cpu_utilization_texts, page)).start()

if __name__ == "__main__":
    ft.app(target=main)
