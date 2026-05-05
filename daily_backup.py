'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 15 Assignment 2
Code Helper: Gemini AI
'''
import os
import zipfile
from datetime import datetime

def run_daily_backup():
    source_dir = "important_files"
    backup_dir = "backups"
    log_file = "backup_log.txt"
    
    try:
        # Task 1: Create a Backup Folder
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print(f"Created directory: {backup_dir}")

        # Check if source folder exists
        if not os.path.exists(source_dir):
            print(f"Error: Source folder '{source_dir}' not found.")
            return

        # Task 2: Create a Timestamped ZIP Backup
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        zip_filename = f"backup_{timestamp}.zip"
        zip_path = os.path.join(backup_dir, zip_filename)

        files_to_backup = os.listdir(source_dir)
        num_files = len(files_to_backup)

        if num_files == 0:
            print("No files found in source folder to backup.")
            return

        with zipfile.ZipFile(zip_path, 'w') as backup_zip:
            for file in files_to_backup:
                file_path = os.path.join(source_dir, file)
                backup_zip.write(file_path, arcname=file)
        
        # Required Output: Backup created: <path> Files backed up: <count>
        print(f"Backup created: {zip_path} Files backed up: {num_files}")

        # Task 3: Log the Backup (Append mode 'a')
        log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - Created {zip_path} ({num_files} files)\n"
        with open(log_file, "a") as log:
            log.write(log_entry)
        
        print("Backup logged successfully.")

    # Task 4: Error Handling
    except PermissionError:
        print("Error: Permission denied. Make sure files aren't open in another program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_daily_backup()