from system_info import get_cpu_utilization
import threading
import psutil

def update_cpu_utilization(cpu_utilization_texts, page):
    def update():
        new_cpu_utilization = get_cpu_utilization()
        for i, utilization in enumerate(new_cpu_utilization):
            cpu_utilization_texts[i].value = f"Core {i}: {utilization}%"
        page.update()
        threading.Timer(1, update).start()
    return update

def get_process_list():
    process_list = psutil.process_iter()
    process_data = []

    for process in process_list:
        process_data.append([
            process.pid,
            process.name(),
            process.status(),
            process.cpu_percent(),
            process.memory_info().rss
        ])

    return process_data