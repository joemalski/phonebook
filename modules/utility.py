# Filename: utility.py
# Date: June 5, 2019
# Description: Utility Class
# By: Joel F. Malinao

import pathlib as path
import ast
import curses
import math as m
from file_read_backwards import FileReadBackwards

class Utility:

    # class variables
    stdscr = None # holds the stdscr from the curses library
    sort_type = 0 # 0 - asending, 1 - descending
    
    current_page = 1 # the current page ofcourse!
    records_per_page = 4 # ideal value for 80 x 25 terminal size 

    selector = 1 # selector the indicator for the arrow up and arrow down
    records_on_page = 0 # save the current records (actual data) on the page
    total_records_on_page = 0 # save the total current records on the page
    phonebook_last_page = 0

    def __init__(self):
        pass

    # set last page
    @classmethod
    def set_last_page_phonebook(cls, file_to_read = 0):
        total = cls.get_total_records(file_to_read)
        cls.phonebook_last_page = m.ceil(total/cls.records_per_page)

    # show errors
    @classmethod
    def show_error(cls, error):
        # set the color pair, foreground, background
        cls.stdscr.attron(curses.color_pair(2))
        cls.stdscr.addstr(0, 0, "Error: {}".format(str(error)))
        cls.stdscr.attroff(curses.color_pair(2))
        cls.stdscr.getch()

    # phone search algorithm
    # basic search but you can modify it later to make it better
    @classmethod
    def check_phone(cls, phone, record):
        if record['phone'] == phone:
            return record

    # name search algorithm
    # basic search but you can modify it later to make it better
    @classmethod
    def check_name(cls, name, record):
        if record['name'] == name:
            return record

    # search name and write results to temp_search.txt
    @classmethod
    def search_name(cls, name):
        try:

            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            temp_search = raw_path / 'temp_search.txt'
            file_phonebook = open(phonebook, 'r')

            records = []
            for phone_record in file_phonebook.readlines():
                rec = cls.check_name(name, ast.literal_eval(phone_record))

                if rec:
                    records.append(rec)

            file_phonebook.close()

            file_temp_search = open(temp_search, 'w')
            for record in records:    
                file_temp_search.write(str(record)+'\n')

            file_temp_search.close()

        except Exception as e:
            cls.show_error(e)

    # search phone and write results to temp_search.txt
    @classmethod
    def search_phone(cls, phone_number):
        try:

            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            temp_search = raw_path / 'temp_search.txt'
            file_phonebook = open(phonebook, 'r')

            records = []
            for phone_record in file_phonebook.readlines():
                rec = cls.check_phone(phone_number, ast.literal_eval(phone_record))

                if rec:
                    records.append(rec)

            file_phonebook.close()

            file_temp_search = open(temp_search, 'w')
            for record in records:    
                file_temp_search.write(str(record)+'\n')

            file_temp_search.close()

        except Exception as e:
            cls.show_error(e)  

    # get total records
    @classmethod
    def get_total_records(cls, file_to_read = 0):
        try:
            raw_path = path.Path('flatfiles/')

            if file_to_read:
                phonebook = raw_path / 'temp_search.txt'
            else:
                phonebook = raw_path / 'phonebook.txt'

            file_phonebook = open(phonebook, 'r')

            total_lines = 0
            for phone in file_phonebook.readlines():
                total_lines +=1

            return total_lines

        except Exception as e:
            cls.show_error(e)  

    # check files if exists, if not create it
    @classmethod
    def check_files_exists(cls):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'
            phonebook = raw_path / 'phonebook.txt'
            temp_search = raw_path / 'temp_search.txt'
        
            if id.exists() != True:
                file_id = open(id, 'w+')
                file_id.write('current_id: 1')
                file_id.close()

            if phonebook.exists() != True:
                file_phonebook = open(phonebook, 'w+')
                file_phonebook.close()

            if temp_search.exists() != True:
                file_temp_search = open(temp_search, 'w+')
                file_temp_search.close()

            return True

        except Exception as e:
            cls.show_error(e)  

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
            cls.show_error(e)  

    # update current id on screen
    @classmethod
    def update_current_id(cls, current_id):
        try:
            raw_path = path.Path('flatfiles/')
            id = raw_path / 'id.txt'

            current_id = str(current_id + 1)
            current_id = 'current_id: ' + current_id
            file_id = open(id, 'w')
            file_id.write(current_id)
            file_id.close()

        except Exception as e:
            cls.show_error(e)  

    # get phone records returns list
    # Note: offset should not be > total records
    @classmethod
    def get_records(cls, lines = 0, offset = 0, file_to_read = 0):
        try:
            raw_path = path.Path('flatfiles/')

            if file_to_read:
                phonebook = raw_path / 'temp_search.txt'
            else:
                phonebook = raw_path / 'phonebook.txt'


            file_phonebook = open(phonebook, 'r')

            records = []
            count = 0
            index = 0

            if lines == 0:
                for phone in file_phonebook.readlines():
                    records.append(ast.literal_eval(phone)) # convert str to dict
            else:
                if offset == 0:
                    for phone in file_phonebook.readlines():
                        if (lines-1) >= count:
                            records.append(ast.literal_eval(phone)) # convert str to dict
                            count += 1
                        else:
                            break
                else:
                    for phone in file_phonebook.readlines():
                        if ((offset - 1) == index):
                            if (lines-1) >= count:
                                records.append(ast.literal_eval(phone)) # convert str to dict
                                count +=1
                            else:
                                break
                            offset += 1
                        index += 1

            return records

        except Exception as e:
            cls.show_error(e)  

    # get phone records in reverse order using the FileReadBackwards library
    # Note: offset should not be > total records
    @classmethod
    def get_records_reverse(cls, lines = 0, offset = 0, file_to_read = 0):
        try:
            raw_path = path.Path('flatfiles/')

            if file_to_read:
                phonebook = raw_path / 'temp_search.txt'
            else:
                phonebook = raw_path / 'phonebook.txt'

            with FileReadBackwards(phonebook, encoding="utf-8") as file_phonebook:

                records = []
                count = 0
                index = 0

                if lines == 0:
                    for phone in file_phonebook:
                        records.append(ast.literal_eval(phone)) # convert str to dict
                else:
                    if offset == 0:
                        for phone in file_phonebook:
                            if (lines-1) >= count:
                                records.append(ast.literal_eval(phone)) # convert str to dict
                                count += 1
                            else:
                                break
                    else:
                        for phone in file_phonebook:
                            if ((offset - 1) == index):
                                if (lines-1) >= count:
                                    records.append(ast.literal_eval(phone)) # convert str to dict
                                    count +=1
                                else:
                                    break
                                offset += 1
                            index += 1

                return records

        except Exception as e:
            cls.show_error(e)  

    # set selector to record, value are hardcoded and printed directly at location
    @classmethod
    def set_selector(cls, number):
        if number == 1:
            cls.selector = 1
            cls.stdscr.attron(curses.color_pair(1))
            cls.stdscr.addstr(5, 20, '|')
            cls.stdscr.addstr(6, 20, '|')
            cls.stdscr.addstr(7, 20, '|')
            cls.stdscr.attroff(curses.color_pair(1))

            cls.stdscr.addstr(9,  20, ' ')
            cls.stdscr.addstr(10, 20, ' ')
            cls.stdscr.addstr(11, 20, ' ')

        elif number == 2:
            cls.selector = 2

            cls.stdscr.addstr(5, 20, ' ')
            cls.stdscr.addstr(6, 20, ' ')
            cls.stdscr.addstr(7, 20, ' ')

            cls.stdscr.attron(curses.color_pair(1))
            cls.stdscr.addstr(9,  20, '|')
            cls.stdscr.addstr(10, 20, '|')
            cls.stdscr.addstr(11, 20, '|')
            cls.stdscr.attroff(curses.color_pair(1))

            cls.stdscr.addstr(13, 20, ' ')
            cls.stdscr.addstr(14, 20, ' ')
            cls.stdscr.addstr(15, 20, ' ')

        elif number == 3:
            cls.selector = 3

            cls.stdscr.addstr(9,  20, ' ')
            cls.stdscr.addstr(10, 20, ' ')
            cls.stdscr.addstr(11, 20, ' ')

            cls.stdscr.attron(curses.color_pair(1))
            cls.stdscr.addstr(13, 20, '|')
            cls.stdscr.addstr(14, 20, '|')
            cls.stdscr.addstr(15, 20, '|')
            cls.stdscr.attroff(curses.color_pair(1))

            cls.stdscr.addstr(17, 20, ' ')
            cls.stdscr.addstr(18, 20, ' ')
            cls.stdscr.addstr(19, 20, ' ')

        elif number == 4:
            cls.selector = 4

            cls.stdscr.addstr(13, 20, ' ')
            cls.stdscr.addstr(14, 20, ' ')
            cls.stdscr.addstr(15, 20, ' ')

            cls.stdscr.attron(curses.color_pair(1))
            cls.stdscr.addstr(17, 20, '|')
            cls.stdscr.addstr(18, 20, '|')
            cls.stdscr.addstr(19, 20, '|')
            cls.stdscr.attroff(curses.color_pair(1))

    # show records on main page
    @classmethod
    def show_records(cls, records):
        y_offset = 5
        x_offset = 22
        i = 0
        for record in records:
            cls.stdscr.addstr(y_offset, x_offset, "ID: {}".format(records[i]['id']))
            cls.stdscr.addstr(y_offset+1, x_offset, "NAME: {}".format(records[i]['name']))
            cls.stdscr.addstr(y_offset+2, x_offset, "PHONE: {}".format(records[i]['phone']))
            y_offset += 4
            i += 1

        # save current record on page and number of records
        cls.records_on_page = records
        cls.total_records_on_page = len(records)

    # save record
    @classmethod
    def save_record(cls, id, name, phone):

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
            cls.show_error(e)       

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

    # delete a record, basically skip the id then rewrite the files again
    @classmethod
    def delete_record(cls, id):
        try:
            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            file_phonebook = open(phonebook, 'r')

            records = []
            for phone in file_phonebook.readlines():
                record = ast.literal_eval(phone)
                if record['id'] != id:
                    records.append(phone)

            file_phonebook.close()

            file_phonebook = open(phonebook, 'w')
            file_phonebook.writelines(records)
            file_phonebook.close

        except Exception as e:
            cls.show_error(e)  

    # edit a record, basically check the id and replace it then rewrite the files again
    @classmethod
    def edit_record(cls, id, name, phone):
        try:

            edit_record = {
                'id': '',
                'name': '',
                'phone': ''
            }

            edit_record['id'] = str(id)
            edit_record['name'] = name
            edit_record['phone'] = phone

            raw_path = path.Path('flatfiles/')
            phonebook = raw_path / 'phonebook.txt'
            file_phonebook = open(phonebook, 'r')

            records = []
            for phone in file_phonebook.readlines():
                record = ast.literal_eval(phone)
                if record['id'] != id:
                    records.append(phone)
                else:
                    records.append(str(edit_record)+'\n')

            file_phonebook.close()
            
            file_phonebook = open(phonebook, 'w')
            file_phonebook.writelines(records)
            file_phonebook.close

        except Exception as e:
            cls.show_error(e)  