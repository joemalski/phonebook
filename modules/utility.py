# Filename: utility.py
# Date: June 5, 2019
# Description: Utility Class
# By: Joel F. Malinao

import pathlib as path
import ast
import curses

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

    # get current id
    @classmethod
    def get_id(cls):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'
            file_id = open(id, 'r')
            current_id = file_id.readline()
            return current_id[11:]

        except Exception as e:
            return 'Exception: ' + str(e)

    # update current id
    @classmethod
    def update_current_id(current_id):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'

            file_id = open(id, 'w')
            current_id = str(current_id + 1)
            current_id = 'current_id: ' + current_id
            file_id.write(current_id)
            file_id.close()

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

    # show records on main page
    @classmethod
    def show_records(cls, stdscr, records):
        y_offset = 4
        x_offset = 20
        i = 0
        for record in records:
            stdscr.addstr(y_offset, x_offset,  "{}   {}                            {}".
                format(records[i]['id'], records[i]['name'], records[i]['phone']))
            y_offset += 1
            i += 1

    # save record
    @classmethod
    def save_record(cls, id, name, phone):

        new_record = {
            'id': '',
            'name': '',
            'phone': ''
        }

        new_record['id'] = id
        new_record['name'] = name
        new_record['phone'] = phone

        try:
            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            file_phonebook = open(phonebook, 'a')

            file_phonebook.write(str(new_record)+'\n')
            file_phonebook.close()

            Utility.update_current_id(id)

        except Exception as e:
            return 'Exception: ' + str(e)        

    # convert bytes to plain string
    @classmethod
    def bytes_to_str(cls, bytes):
        temp = str(bytes)
        temp = temp[2:] # removes first 2 index
        temp_len = len(temp)
        return temp[0:temp_len-1] # returns all characters except the last

    # control cursor diplay
    @classmethod
    def cursor_display(cls, option):
        
        # display cursor and echo
        if option == 0:
            curses.curs_set(0)
            curses.noecho()

        # no cursor, no echo
        elif option == 1:
            curses.curs_set(1)
            curses.echo()



















