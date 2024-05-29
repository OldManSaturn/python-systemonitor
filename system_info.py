import psutil
import platform

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
