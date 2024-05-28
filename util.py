from system_info import get_cpu_utilization
import threading

def update_cpu_utilization(cpu_utilization_texts, page):
    def update():
        new_cpu_utilization = get_cpu_utilization()
        for i, utilization in enumerate(new_cpu_utilization):
            cpu_utilization_texts[i].value = f"Core {i}: {utilization}%"
        page.update()
        threading.Timer(1, update).start()
    return update
