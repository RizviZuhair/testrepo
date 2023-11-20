import os
import shutil
import atexit

def delete_temp_files():
    temp_folder = "C:/temp"  # Replace with the path to your temporary folder
    
    if os.path.exists(temp_folder):
        for root, dirs, files in os.walk(temp_folder):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    
        shutil.rmtree(temp_folder)
        print(f"Temporary files deleted successfully.")
    else:
        print("Temporary folder does not exist.")

atexit.register(delete_temp_files)

# Rest of your program code goes here...