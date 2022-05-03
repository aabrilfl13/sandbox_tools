import os
import glob
import shutil

SOURCE_PATH = '/Users/aabrilfl/Pictures/ViñaRock 2022'

for file_path in glob.iglob(f'{SOURCE_PATH}/**/*.*', recursive=True):
    print(file_path)
    destination = SOURCE_PATH
    filename = file_path.split('/')[-1:]
    
    if os.path.isfile(file_path):
        try:
            shutil.move(file_path, destination)
            print(f'Moved: {filename}')
        except Exception as e: 
            print(f'ERROR ({filename}): {e}')