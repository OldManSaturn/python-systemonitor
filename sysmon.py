import psutil
import platform
import flet as ft


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


def main(page: ft.Page):
    page.title = "System Monitor"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    os_info = get_os_info()
    memory_info = get_memory_info()
    cpu_info = get_cpu_info()
    cpu_utilization = get_cpu_utilization()

    # System Info Column
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
        spacing=10
    )

    # CPU Utilization Column
    cpu_utilization_column = ft.Column(
        [
            create_heading("CPU Utilization Per Core")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    cpu_utilization_texts = []
    for i, utilization in enumerate(cpu_utilization):
        cpu_text = create_text_component(f"Core {i}", f"{utilization}%")
        cpu_utilization_texts.append(cpu_text)
        cpu_utilization_column.controls.append(cpu_text)

    # Refresh button to update CPU utilization
    def refresh_cpu_utilization(e):
        new_cpu_utilization = get_cpu_utilization()
        for i, utilization in enumerate(new_cpu_utilization):
            cpu_utilization_texts[i].value = f"Core {i}: {utilization}%"
        page.update()

    refresh_button = ft.ElevatedButton(text="Refresh CPU Utilization", on_click=refresh_cpu_utilization)
    cpu_utilization_column.controls.append(refresh_button)

    # Main Row to hold both columns
    main_row = ft.Row(
        [
            system_info_column,
            cpu_utilization_column
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=50
    )

    page.add(main_row)


if __name__ == "__main__":
    ft.app(target=main)