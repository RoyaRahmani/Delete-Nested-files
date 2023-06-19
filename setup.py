import os
import shutil

#  Provide the path to the nested file.
main_directory = 'path/to/main/directory'

# Specify the desired location for saving your new file.
new_directory = 'path/to/new/directory'

# Make sure to create the new directory if it does not already exist.
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

#  Iterate through the folders in the main directory
for folder in os.listdir(main_directory):
    
    folder_path = os.path.join(main_directory,folder)
    if os.path.isdir(folder_path):
        
        # Iterate through the files in the folder
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path,file)
            
            # Verify if the file format is as expected.
            if file.endswith('.fa'):
                
                # Copy the file to the new directory
                shutil.copy(file_path,new_directory)
