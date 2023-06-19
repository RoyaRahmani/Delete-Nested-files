import os
import shutil

main_directory = 'SGB_genome_fastas_part2'
new_directory = 'SGB_genome_fastas_partAA'

if not os.path.exists(new_directory):
    os.makedirs(new_directory)


fasta_files = []

for folder in os.listdir(main_directory):
    folder_path = os.path.join(main_directory,folder)
    
    if os.path.isdir(folder_path):

        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path,file)
            if file.endswith('.fa'):
                fasta_files.append(file_path)
                shutil.copy(file_path,new_directory)