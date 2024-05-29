import psutil
import platform
import flet as ft
import threading

def get_cpu_info():
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    uname = platform.uname()
    cpu_architecture = uname.machine
    cpu_model = uname.processor

    cpu_info = {
        "cpu_count": cpu_count,
        "cpu_count_logical": cpu_count_logical,
        "uname": uname,
        "cpu_architecture": cpu_architecture,
        "cpu_model": cpu_model
    }

    return cpu_info

def get_memory_info():
    virtual_memory = psutil.virtual_memory()
    total_memory_gb = virtual_memory.total / (1024.0 ** 3)

    memory_info = {
        "total_memory_gb": total_memory_gb,
    }

    return memory_info

def get_os_info():
    os_info = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version()
    }

    return os_info

def get_cpu_utilization():
    cpu_utilization = psutil.cpu_percent(interval=1, percpu=True)
    return cpu_utilization

def create_text_component(label, value):
    return ft.Text(f"{label}: {value}", size=14, weight=ft.FontWeight.NORMAL)

def create_heading(text):
    return ft.Text(text, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_500)

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

    def update_cpu_utilization():
        if tabs.selected_index == 0:  # Only update if System Info tab is active
            new_cpu_utilization = get_cpu_utilization()
            for i, utilization in enumerate(new_cpu_utilization):
                cpu_utilization_texts[i].value = f"Core {i}: {utilization}%"
            page.update()
        threading.Timer(1, update_cpu_utilization).start()

    # Start the periodic update
    threading.Timer(1, update_cpu_utilization).start()

if __name__ == "__main__":
    ft.app(target=main)
