# Filename: utility.py
# Date: June 5, 2019
# Description: Utility Class
# By: Joel F. Malinao

import pathlib as path

class Utility:

    def __init__(self):
        pass

    # 'w+' - check files if exists, if not create it
    @classmethod
    def check_files_exists(cls):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'
            phonebook = raw_path / 'phonebook.txt'
        
            file_id = open(id, 'w+')
            file_id.write('current_id: 1')
            file_id.close()

            file_phonebook = open(phonebook, 'w+')
            file_phonebook.close()

            return True

        except Exception as e:
            return 'Exception: ' + str(e)

