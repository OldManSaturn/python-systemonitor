import flet as ft
from system_info import get_os_info, get_memory_info, get_cpu_info, get_cpu_utilization
from ui_components import create_text_component, create_heading

def create_system_info_tab(cpu_utilization_texts):
    os_info = get_os_info()
    memory_info = get_memory_info()
    cpu_info = get_cpu_info()
    cpu_utilization = get_cpu_utilization()

    system_info_column = ft.Column(
        [
            create_heading("System Information"),
            create_text_component("Operating System", os_info['platform']),
            create_text_component("OS Release", os_info['platform_release']),
            create_text_component("OS Version", os_info['platform_version']),
            create_text_component("Total Installed Memory", f"{memory_info['total_memory_gb']:.2f} GB"),
            create_text_component("Total Physical CPU Cores", cpu_info['cpu_count']),
            create_text_component("Total Logical CPU Cores", cpu_info['cpu_count_logical']),
            create_text_component("CPU Architecture", cpu_info['cpu_architecture']),
            create_text_component("CPU Model", cpu_info['cpu_model']),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
    )

    system_info_container = ft.Container(
        content=system_info_column,
        border=ft.border.all(1, color=ft.colors.BLACK),
        padding=5,
        border_radius=5,
        alignment=ft.alignment.center
    )

    cpu_utilization_column = ft.Column(
        [
            create_heading("CPU Utilization Per Core")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
    )

    for i, utilization in enumerate(cpu_utilization):
        cpu_text = create_text_component(f"Core {i}", f"{utilization}%")
        cpu_utilization_texts.append(cpu_text)
        cpu_utilization_column.controls.append(cpu_text)

    cpu_utilization_container = ft.Container(
        content=cpu_utilization_column,
        border=ft.border.all(1, color=ft.colors.BLACK),
        padding=5,
        border_radius=5,
        alignment=ft.alignment.center
    )

    main_row = ft.Row(
        [
            system_info_container,
            cpu_utilization_container
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    return main_row

def create_process_list_tab():
    process_column = ft.Column(
        [
            create_heading("Current Running Processes"),
            ft.Text("This page will display the list of current running processes.")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=5
    )

    process_container = ft.Container(
        content=process_column,
        border=ft.border.all(1, color=ft.colors.BLACK),
        padding=5,
        border_radius=5,
        alignment=ft.alignment.center
    )

    return process_container
