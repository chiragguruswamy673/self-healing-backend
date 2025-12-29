import time
import requests
import psutil
from decision_engine import decide_action

SERVICE_URL = "http://127.0.0.1:8000/health"

CPU_THRESHOLD = 80     # percent
MEM_THRESHOLD = 80     # percent

def monitor_service():
    print("📡 Health & metrics monitor started...")

    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        try:
            response = requests.get(SERVICE_URL, timeout=2).json()
            status = response.get("status")
        except Exception as e:
            status = "ERROR"

        health_snapshot = {
            "status": status,
            "cpu": cpu,
            "memory": memory
        }

        if (
            status != "UP"
            or cpu > CPU_THRESHOLD
            or memory > MEM_THRESHOLD
        ):
            decide_action(health_snapshot)

        time.sleep(5)

if __name__ == "__main__":
    monitor_service()
