'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 15 Assignment 3
Code Helper: Gemini AI
'''
import requests
from datetime import datetime

def check_uptime():
    # 1. Define the website to monitor
    url = "https://www.google.com"
    log_file = "uptime_log.txt"
    
    try:
        # 2. Send a GET request with a timeout (Task 2)
        # Timeout ensures the script doesn't hang forever if the site is slow
        response = requests.get(url, timeout=5)
        
        # 3. Check status code (Task 3)
        if response.status_code == 200:
            status = "UP"
        else:
            status = f"DOWN (Status Code: {response.status_code})"
            
    except requests.exceptions.RequestException:
        # 4. Handle connection errors gracefully (Task 4)
        status = "DOWN (Connection Error)"

    # 5. Log the result (Task 5)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {url} is {status}\n"
    
    try:
        with open(log_file, "a") as f:
            f.write(log_entry)
        
        # Print for visual confirmation in terminal
        print(f"Checked {url}: {status}")
        print("Status logged successfully.")
        
    except PermissionError:
        print("Error: Could not write to log file. Check file permissions.")

if __name__ == "__main__":
    check_uptime()