import os
import re
from pathlib import Path
import rarfile

class FileManager:
    
    def exist_obj(self, path, name, is_file=False):
        full_path = os.path.join(path, name)
        if not os.path.exists(full_path):
            ImportWarning(f'{full_path}, It not alrady have')
            if is_file:
                Path(full_path).touch()
                ImportWarning(f'Complete create file {name}')
            else:
                Path(full_path).mkdir()
        else:
            print() # TODO: contines from this?
            
        return full_path

    def validate_files(self, input_path, target_file_pattern):
        valid_files = []
        
        for path in os.listdir(input_path):
            filename = os.path.basename(path)
            if re.match(target_file_pattern, filename):
                valid_files.append(path)

        return valid_files

    def access_rar(self, file_paths, target_file):
        pattern = r'\d{4}_?.*\w(?=.rar)'
        with rarfile.RarFile(file_paths, 'r') as rf:
            target_file = [file for file in rf.namelist() if re.search(r'.*\.html', file)][0]
            if target_file in rf.namelist():
                with rf.open(target_file, 'r') as file:
                    return file.read()
            else:
                raise FileNotFoundError(f"{target_file} not found in the RAR archive.")

class FileOparetion:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contents = self.read_file()

    def read_file(self):
        if not os.path.exists(self.file_path):
            print(f'Create {self.file_path}!')
            Path(self.file_path).touch()
            return ''
        
        with open(self.file_path, 'r') as file:
            return file.read()
 
    def get_content(self):
        return self.contents