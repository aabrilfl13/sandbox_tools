import os
import glob
import shutil

# Get the list of all files and directories
PATH = "/Users/aabrilfl/Pictures/ViñaRock 2022"

dir_list = os.listdir(PATH)

print("Files and directories in '", PATH, "' :")
dir_list.sort()

items = list(glob.iglob(f'{PATH}/*.HEIC', recursive=True))
for item in list(glob.iglob(f'{PATH}/*.heic', recursive=True)):
    items.append(item)

for item in items:
    heic_filename = item.split('/')[-1:][0]
    heic_filename = heic_filename.split('.')[:-1][0]
    to_remove = list(glob.iglob(f'{PATH}/{heic_filename}.MOV', recursive=True))

    if to_remove:
        print(f'REMOVE: {to_remove}')
        os.remove(to_remove[0])
    else:
        print(f'File {heic_filename} not found in MOV')
