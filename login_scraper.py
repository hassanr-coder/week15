'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 15 Assignment 4
Code Helper: Gemini AI
'''
import psutil
import logging
from datetime import datetime

# 1. Configure logging to save to a file (Task 4 & 5)
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def monitor_system():
    print("--- System Health Monitor ---")
    
    try:
        # 2. Collect System Metrics (Task 2)
        # cpu_percent interval=1 gives a more accurate reading
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # 3. Check Thresholds and Build Alerts (Task 3)
        alerts = []
        if cpu_usage > 80:
            alerts.append(f"High CPU: {cpu_usage}%")
        if memory.percent > 80:
            alerts.append(f"High Memory: {memory.percent}%")
        if disk.percent > 90:
            alerts.append(f"Low Disk Space: {disk.percent}% used")

        # 4. Create the Health Report
        report = f"CPU: {cpu_usage}% | RAM: {memory.percent}% | Disk: {disk.percent}%"
        print(report)
        logging.info(report)

        # 5. Handle Alerts (Task 3)
        if alerts:
            for alert in alerts:
                print(f"ALERT: {alert}")
                logging.warning(alert)
        else:
            print("All systems healthy.")

    # 6. Error Handling (Task 6)
    except PermissionError:
        msg = "Error: Access denied. Try running as Administrator/Sudo."
        print(msg)
        logging.error(msg)
    except Exception as e:
        msg = f"An unexpected error occurred: {e}"
        print(msg)
        logging.error(msg)

if __name__ == "__main__":
    monitor_system()