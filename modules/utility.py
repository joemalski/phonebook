# Filename: utility.py
# Date: June 5, 2019
# Description: Utility Class
# By: Joel F. Malinao

import pathlib as path
import ast

class Utility:

    def __init__(self):
        pass

    # check files if exists, if not create it
    @classmethod
    def check_files_exists(cls):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'
            phonebook = raw_path / 'phonebook.txt'
        
            if id.exists() != True:
                file_id = open(id, 'w+')
                file_id.write('current_id: 1')
                file_id.close()

            if phonebook.exists() != True:
                file_phonebook = open(phonebook, 'w+')
                file_phonebook.close()

            return True

        except Exception as e:
            return 'Exception: ' + str(e)

    # get phone records returns list
    @classmethod
    def get_records(cls, lines=0):
        try:
            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            file_phonebook = open(phonebook, 'r')

            records = []
            count = 0
            if lines == 0:
                for phone in file_phonebook.readlines():
                    records.append(ast.literal_eval(phone)) # convert str to dict
            else:
                for phone in file_phonebook.readlines():
                    if (lines-1) >= count:
                        records.append(ast.literal_eval(phone)) # convert str to dict
                        count += 1
                    else:
                        break

            return records

        except Exception as e:
            return 'Exception: ' + str(e)

