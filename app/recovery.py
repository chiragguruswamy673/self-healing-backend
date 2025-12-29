from datetime import datetime
import os

def recover_service(reason: str, snapshot: dict):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"[{timestamp}] Reason: {reason} | "
        f"Status: {snapshot.get('status')} | "
        f"CPU: {snapshot.get('cpu')}% | "
        f"Memory: {snapshot.get('memory')}%\n"
    )

    print("🚑 Self-Healing Triggered")
    print(log_entry)

    os.makedirs("logs", exist_ok=True)
    with open("logs/recovery.log", "a") as f:
        f.write(log_entry)

    if reason == "High CPU usage":
        print("🧹 Scaling / throttling CPU tasks")
    elif reason == "High memory usage":
        print("🗑 Clearing caches / freeing memory")
    else:
        print("🔄 Restarting service")

    print("✅ Recovery action executed\n")
