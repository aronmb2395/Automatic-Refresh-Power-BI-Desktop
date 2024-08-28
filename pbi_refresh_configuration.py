import subprocess
import time
import pyautogui
import shutil
import os
os.chdir(r'D:\Users\USER\miniconda3\Lib\site-packages')




 # Establish the path to the source code of your pbi report
source_file_path = r'C:\Users\USER\Documents\PowerBI Automate Refresh\tablas_exportadas\usuarios.csv'

# Replace 'path_to_your_file.pbix' with the actual path to your PBIX file
pbix_file_path = r'C:\Users\USER\Documents\PowerBI Automate Refresh\data.pbix'


# Replace 'path_to_power_bi_executable' with the actual path to your Power BI Desktop executable
power_bi_executable_path = r'C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe'

destination_directory = r'C:\Users\USER\Documents\POWERBI'
    


def pbi_automatic_refresh (source_file_path, power_bi_executable_path, pbix_file_path, destination_directory):
    
    # Get the size of the file in bytes
    source_file_size = os.path.getsize(source_file_path)
    pbix_file_size = os.path.getsize(pbix_file_path)

    # Convert the size to a human-readable format (e.g., kilobytes or megabytes)

    open_time = 10 + round((pbix_file_size / (1024 * 1024)) * 6.0)          # Size in megabytes
    refresh_time = 10 + round((source_file_size / (1024 * 1024)) * 1.1)     # Size in megabytes

       
    # Command to open the PBIX file with Power BI Desktop
    command = [power_bi_executable_path, pbix_file_path]

    # Open the PBIX file with Power BI Desktop
    subprocess.Popen(command, shell=True)

    # Add a brief delay to switch to the desired window
    time.sleep(open_time)

    # Press hotkey combination
    pyautogui.press("alt")
    time.sleep(2)
    pyautogui.press("h")
    time.sleep(2)
    pyautogui.press("r")

    time.sleep(refresh_time)
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)
    pyautogui.hotkey('alt', 'fn', 'f4')
    time.sleep(5)

 

    # Copy the file to the destination directory
    shutil.copy(pbix_file_path, destination_directory)


 # Execute the function so the subprocess can call the execution

pbi_automatic_refresh(source_file_path, power_bi_executable_path, pbix_file_path, destination_directory)






