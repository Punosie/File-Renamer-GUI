import os
from pathlib import Path
import re

def rename_file(root_folder_path, regex_pattern):
    root_folder_path = Path(root_folder_path)
    renamed = False
    
    for folder_name, _, files in os.walk(root_folder_path):
        for file_name in files:
            file_name_without_extension = Path(file_name).stem
            match = re.search(regex_pattern, file_name_without_extension)
            if match:
                episode_number = match.group(1)
                new_file_name = f"Episode {episode_number}"
                old_file_path = Path(folder_name) / file_name
                new_file_path = Path(folder_name) / (new_file_name + old_file_path.suffix)
                if old_file_path != new_file_path:
                    old_file_path.rename(new_file_path)
                    renamed = True

    if renamed:
        return 'Renaming process completed.'
    else:
        return 'Files are already renamed.'