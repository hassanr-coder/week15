'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 15 Assignment 1
Code Helper: Gemini AI
'''
import os
import shutil
import zipfile

def run_backup():
    source_dir = "data"
    target_dir = os.path.join(source_dir, "CSV_Files")
    zip_name = "data_backup.zip"
    
    try:
        # Task 1: Find All .csv Files
        if not os.path.exists(source_dir):
            print(f"Error: The folder '{source_dir}' does not exist.")
            return

        csv_files = [f for f in os.listdir(source_dir) if f.endswith('.csv')]
        print(f"Found {len(csv_files)} CSV files.")

        if len(csv_files) == 0:
            print("No files to move or backup.")
            return

        # Task 2: Move CSV Files to CSV_Files folder
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        moved_count = 0
        for file_name in csv_files:
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(target_dir, file_name)
            
            # Moving the file
            shutil.move(source_path, destination_path)
            moved_count += 1
        
        print(f"Moved {moved_count} CSV files to {target_dir}")

        # Task 3: Create a ZIP Archive
        # Create the zip in the root directory (where the script is)
        with zipfile.ZipFile(zip_name, 'w') as backup_zip:
            for folderName, subfolders, filenames in os.walk(target_dir):
                for filename in filenames:
                    file_path = os.path.join(folderName, filename)
                    # Add file to zip (arcname keeps the zip structure clean)
                    backup_zip.write(file_path, arcname=filename)
        
        print(f"Created archive: {zip_name}")

    except PermissionError:
        print("Error: Permission denied. Make sure the files aren't open in another program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_backup()