# Filename: utility.py
# Date: June 5, 2019
# Description: Utility Class
# By: Joel F. Malinao

import pathlib as path
import ast
import curses
from file_read_backwards import FileReadBackwards

class Utility:

    # class variables

    # 0 - asending, 1 - descending
    sort_type = 0

    def __init__(self):
        pass

    # get total records
    @classmethod
    def get_total_records(cls):
        try:
            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            file_phonebook = open(phonebook, 'r')

            total_lines = 0
            for phone in file_phonebook.readlines():
                total_lines +=1

            return total_lines

        except Exception as e:
            return 'Exception: ' + str(e)

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
    def update_current_id(cls, stdscr, current_id):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'

            current_id = str(current_id + 1)
            current_id = 'current_id: ' + current_id
            file_id = open(id, 'w')
            file_id.write(current_id)
            file_id.close()

        except Exception as e:
            stdscr.addstr(23, 50, str(e))
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

    # get phone records in reverse order using the FileReadBackwards library
    @classmethod
    def get_records_reverse(cls, lines=0):
        try:
            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            with FileReadBackwards(phonebook, encoding="utf-8") as file_phonebook:

                records = []
                count = 0
                if lines == 0:
                    for phone in file_phonebook:
                        records.append(ast.literal_eval(phone)) # convert str to dict
                else:
                    for phone in file_phonebook:
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
        y_offset = 3
        x_offset = 20
        i = 0
        for record in records:
            stdscr.addstr(y_offset, x_offset, "ID: {}".format(records[i]['id']))
            stdscr.addstr(y_offset+1, x_offset, "Name: {}".format(records[i]['name']))
            stdscr.addstr(y_offset+2, x_offset, "Phone: {}".format(records[i]['phone']))
            y_offset += 4
            i += 1

    # save record
    @classmethod
    def save_record(cls, stdscr, id, name, phone):

        new_record = {
            'id': '',
            'name': '',
            'phone': ''
        }

        new_record['id'] = str(id)
        new_record['name'] = name
        new_record['phone'] = phone

        try:
            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            file_phonebook = open(phonebook, 'a')

            file_phonebook.write(str(new_record)+'\n')            
            file_phonebook.close()

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



















