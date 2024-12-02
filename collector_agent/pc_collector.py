import psutil
from datetime import datetime

def collect_metrics(device_id):
    metrics = {
        "device_id": device_id,
        "cpu_usage": psutil.cpu_percent(interval=1),  # CPU usage percentage
        "memory_usage": psutil.virtual_memory().percent  # Memory usage percentage
    }
    metrics["timestamp"] = datetime.now()
    return metrics
