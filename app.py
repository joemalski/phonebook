# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import math as m
import modules.skins as skins
from modules.utility import Utility

def search_by_name():
   
    # add skins
    Utility.stdscr.clear()
    skins.main()
    skins.search()

    # display cursor
    Utility.cursor_display(1)

    # accept and validate name search
    Utility.stdscr.addstr(6, 20, 'Name: ')
    Utility.stdscr.addstr(23, 50, 'Please enter a name.')
    name = Utility.bytes_to_str(Utility.stdscr.getstr(6, 26, 30))    
    while 1:
        if name == '':
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Name must not be empty.')
            Utility.stdscr.addstr(6, 27, ' '*30)
            Utility.stdscr.refresh()
            name = Utility.bytes_to_str(Utility.stdscr.getstr(6, 26, 30))
        else:
            break

    # add searchs results to temp_search.txt
    Utility.search_name(name)

    # hide cursor
    Utility.cursor_display(0)

    # load records
    load_main_details(Utility.records_per_page, 0, 1)   

    # set default selector value
    Utility.set_selector(1)

    # seach name event loop
    key = Utility.stdscr.getch()
    while 1:

        # add new records
        if key == curses.KEY_F1:
            # reset current page to 1
            Utility.current_page = 1
            add()

        # search records
        elif key == curses.KEY_F2:
            # reset current page to 1
            Utility.current_page = 1
            search()

        # sort order
        elif key == curses.KEY_F3:

            # toggle sort type value
            if Utility.sort_type == 0:
                Utility.sort_type = 1
            elif Utility.sort_type == 1:
                Utility.sort_type = 0
            
            # reset current page to 1
            Utility.current_page = 1

            # reload records
            load_main_details(Utility.records_per_page, 0, 1)

            # show currently selected sort type
            if Utility.sort_type == 0:
                sort_by = 'Ascending'
            elif Utility.sort_type == 1:
                sort_by = 'Descending'

            Utility.stdscr.addstr(23, 50, "Sort By: {}".format(sort_by))

        # show previous records
        elif key == curses.KEY_F4:
            previous_page(1)

        # show next records
        elif key == curses.KEY_F5:
            next_page(1)

        # escape to exit
        elif key == 27:
            break

        # enter key for selecting a record
        elif key == 10:
            Utility.stdscr.addstr(23, 50, 'Pressed ENTER   ')

        # navigating records using arrow up
        elif key == curses.KEY_UP:
            Utility.stdscr.addstr(23, 50, 'Pressed Up Key  ')

        # navigating records using arrow up
        elif key == curses.KEY_DOWN:
            Utility.stdscr.addstr(23, 50, 'Pressed Down Key')

        key = Utility.stdscr.getch()


def search_by_phone():

    # add skins
    Utility.stdscr.clear()
    skins.main()
    skins.search()

    # display cursor
    Utility.cursor_display(1)

    # accept and validate name search
    Utility.stdscr.addstr(6, 20, 'Phone: ')
    Utility.stdscr.addstr(23, 50, 'Please enter a phone number.')    
    phone = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 7))

    numbers = set('0123456789')
    while 1:
        if phone == '':
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Number must not be empty.')
            Utility.stdscr.addstr(6, 27, ' '*7)
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 7))
        elif set(phone).issubset(numbers) == False:
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Incorrect Number.')
            Utility.stdscr.addstr(6, 27, ' '*7)
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 7))
        else:
            break

    # add searchs results to temp_search.txt
    Utility.search_phone(phone)

    # hide cursor
    Utility.cursor_display(0)

    # load records
    load_main_details(Utility.records_per_page, 0, 1)   

    # set default selector value
    Utility.set_selector(1)

    # seach name event loop
    key = Utility.stdscr.getch()
    while 1:

        # add new records
        if key == curses.KEY_F1:
            # reset current page to 1
            Utility.current_page = 1
            add()

        # search records
        elif key == curses.KEY_F2:
            # reset current page to 1
            Utility.current_page = 1
            search()

        # sort order
        elif key == curses.KEY_F3:

            # toggle sort type value
            if Utility.sort_type == 0:
                Utility.sort_type = 1
            elif Utility.sort_type == 1:
                Utility.sort_type = 0
            
            # reset current page to 1
            Utility.current_page = 1

            # reload records
            load_main_details(Utility.records_per_page, 0, 1)

            # show currently selected sort type
            if Utility.sort_type == 0:
                sort_by = 'Ascending'
            elif Utility.sort_type == 1:
                sort_by = 'Descending'

            Utility.stdscr.addstr(23, 50, "Sort By: {}".format(sort_by))

        # show previous records
        elif key == curses.KEY_F4:
            previous_page(1)

        # show next records
        elif key == curses.KEY_F5:
            next_page(1)

        # escape to exit
        elif key == 27:
            break

        # enter key for selecting a record
        elif key == 10:
            Utility.stdscr.addstr(23, 50, 'Pressed ENTER   ')

        # navigating records using arrow up
        elif key == curses.KEY_UP:
            Utility.stdscr.addstr(23, 50, 'Pressed Up Key  ')

        # navigating records using arrow up
        elif key == curses.KEY_DOWN:
            Utility.stdscr.addstr(23, 50, 'Pressed Down Key')

        key = Utility.stdscr.getch()

def search():
    
    # add skins
    Utility.stdscr.clear()
    skins.main()
    skins.search()

    # display selection
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(5, 20, '[1]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(5, 23, ' - SEARCH BY NAME')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(7, 20, '[2]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(7, 23, ' - SEARCH BY PHONE NUMBER')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(9, 20, '[ESC]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(9, 25, ' - CANCEL')

    # check user selection
    Utility.stdscr.addstr(23, 50, 'Search, select your option.')
    key = None
    # '1'=49 and '2'=50
    while (key != 49 and key != 50):
        key = Utility.stdscr.getch()

        if key == 49: # 1
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Search, by name')
            search_by_name()
            break

        elif key == 50: # 2
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Search, by phone')
            search_by_phone()
            break

        elif key == 27:
            break

    # refresh screen show records again
    Utility.stdscr.clear()
    load_main_details(Utility.records_per_page, 0)
    Utility.current_page = 1
    Utility.set_selector(1)


def next_page(file_to_read = 0):

    # get last page
    total_row_count = Utility.get_total_records(file_to_read)
    last_page = m.ceil(total_row_count/Utility.records_per_page)

    # get current page
    page_num = Utility.current_page

    # go to next page and check if > last page
    page_num += 1
    if page_num > last_page:
        page_num = last_page

    # update page number
    Utility.current_page = page_num

    # get records equivalent in page number, start and end record index
    end_index = page_num * Utility.records_per_page
    start_index = end_index - (Utility.records_per_page - 1)

    # show next page
    load_main_details(Utility.records_per_page, start_index, file_to_read)

def previous_page(file_to_read = 0):

    # get current page
    page_num = Utility.current_page

    # go to previous page and check if < 1
    page_num -= 1
    if page_num < 1:
        page_num = 1

    # update current page
    Utility.current_page = page_num
    
    # get records equivalent in page number, start and end record index
    end_index = page_num * Utility.records_per_page
    start_index = end_index - (Utility.records_per_page - 1)  

    # show next page
    load_main_details(Utility.records_per_page, start_index, file_to_read)

def add():

    # add skins
    Utility.stdscr.clear()
    skins.main()
    skins.add()

    # show total records
    lines = Utility.get_total_records()
    Utility.stdscr.addstr(23, 17, str(lines))
    Utility.stdscr.refresh()

    # get the current id
    current_id = Utility.get_id()
    Utility.stdscr.addstr(5, 26, current_id)

    # display cursor
    Utility.cursor_display(1)

    # accept and validate name
    Utility.stdscr.addstr(23, 50, 'Please enter a name.')
    name = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 30))
    while 1:
        if name == '':
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Name must not be empty.')
            Utility.stdscr.addstr(6, 27, ' '*30)
            Utility.stdscr.refresh()
            name = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 30))
        else:
            break

    # clear validation messages
    skins.clear_message()

    # accept and validate phone
    Utility.stdscr.addstr(23, 50, 'Please enter a 7-digit number.')
    phone = Utility.bytes_to_str(Utility.stdscr.getstr(7, 27, 7))
    numbers = set('0123456789')
    while 1:
        if phone == '':
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Number must not be empty.')
            Utility.stdscr.addstr(7, 27, ' '*7)
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(7, 27, 7))
        elif set(phone).issubset(numbers) == False or len(phone) < 7:
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Incorrect Number.')
            Utility.stdscr.addstr(6, 27, ' '*7)
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(7, 27, 7))
        else:
            break

    # clear validation messages
    skins.clear_message()

    # checks if user wants to save or cancel
    Utility.cursor_display(0)
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(10, 20, '[S]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(10, 23, ' - SAVE')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(12, 20, '[ESC]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(12, 25, ' - CANCEL')
    
    key = None
    
    # 's'=115, 'S'=83 and ESC = 27
    while (key != 83 and key != 115):

        key = Utility.stdscr.getch()
        
        if key == 115 or key == 83:
            Utility.save_record(int(current_id), name, phone)
            Utility.update_current_id(int(current_id))
            break

        elif key == 27:
            break

    # refresh screen show records again
    Utility.stdscr.clear()
    load_main_details(Utility.records_per_page, 0)
    Utility.set_selector(Utility.selector)
    Utility.current_page = 1

def delete(record):
    # show selected record skin
    Utility.stdscr.clear()
    skins.main()
    skins.selected_record()

    # show actual selected record
    Utility.stdscr.addstr(5, 27, str(record['id']))
    Utility.stdscr.addstr(6, 27, str(record['name']))
    Utility.stdscr.addstr(7, 27, str(record['phone']))

    Utility.stdscr.addstr(10, 20, 'ARE YOU SURE YOU WANT TO DELETE THIS RECORD ?')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(12, 20, '[Y]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(12, 23, ' - YES')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(14, 20, '[N]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(14, 23, ' - NO')

    # '121'=y, '89'='Y' and '110'=n, '78'=N
    while 1:
        key = Utility.stdscr.getch()
        if key == 89 or key == 121:
            Utility.delete_record(record['id'])
            break

        elif key == 78 or key == 110:
            break

def edit(record):
    # show selected record skin
    Utility.stdscr.clear()
    skins.main()
    skins.selected_record()

    # show actual selected record
    Utility.stdscr.addstr(5, 27, str(record['id']))
    Utility.stdscr.addstr(6, 27, str(record['name']))
    Utility.stdscr.addstr(7, 27, str(record['phone']))

    # display cursor
    Utility.cursor_display(1)

    # name label
    Utility.stdscr.addstr(10, 20, 'NEW NAME: ')

    # accept and validate name
    Utility.stdscr.addstr(23, 50, 'Please enter a name.')
    name = Utility.bytes_to_str(Utility.stdscr.getstr(10, 30, 30))
    while 1:
        if name == '':
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Name must not be empty.')
            Utility.stdscr.addstr(10, 30, ' '*30)
            Utility.stdscr.refresh()
            name = Utility.bytes_to_str(Utility.stdscr.getstr(10, 30, 30))
        else:
            break

    # phone label
    Utility.stdscr.addstr(11, 20, 'NEW PHONE: ')

    # accept and validate phone
    Utility.stdscr.addstr(23, 50, 'Please enter a phone number.')    
    phone = Utility.bytes_to_str(Utility.stdscr.getstr(11, 31, 7))

    numbers = set('0123456789')
    while 1:
        if phone == '':
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Number must not be empty.')
            Utility.stdscr.addstr(11, 31, ' '*7)
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(11, 31, 7))
        elif set(phone).issubset(numbers) == False or len(phone) < 7:
            skins.clear_message()
            Utility.stdscr.addstr(23, 50, 'Incorrect Number.')
            Utility.stdscr.addstr(11, 31, ' '*7)
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(11, 31, 7))
        else:
            break

    # remove cursor
    Utility.cursor_display(0)

    # edit the record
    Utility.edit_record(record['id'], name, phone)


def selected_record():

    # show selected record skin
    Utility.stdscr.clear()
    skins.main()
    skins.selected_record()    

    # show actual selected record
    selected_record = Utility.records_on_page[Utility.selector - 1]
    Utility.stdscr.addstr(5, 27, str(selected_record['id']))
    Utility.stdscr.addstr(6, 27, str(selected_record['name']))
    Utility.stdscr.addstr(7, 27, str(selected_record['phone']))

    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(10, 20, '[E]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(10, 23, ' - EDIT')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(12, 20, '[D]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(12, 23, ' - DELETE')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(14, 20, '[ESC]')
    Utility.stdscr.attroff(curses.color_pair(1))
    Utility.stdscr.addstr(14, 25, ' - CANCEL')

    # selected_record event loop
    key = Utility.stdscr.getch()
    while 1:

        # 'e'=101 and 'E'=69
        if key == 69 or key == 101:
            edit(selected_record)
            break

        # 'd'=100 and 'D'=68
        elif key == 100 or key == 68:
            delete(selected_record)            
            break

        elif key == 27:
            break

    # refresh screen show records again
    Utility.stdscr.clear()
    load_main_details(Utility.records_per_page, 0)
    Utility.current_page = 1

def load_main_details(records_per_page, offset, file_to_read = 0):

    # clear screen
    Utility.stdscr.clear()

    # load appropriate skin based on file_to_read
    if file_to_read:
        skins.main()
        skins.search()
    else:
        skins.main()

    # check the sort_type
    if Utility.sort_type == 0:
        records = Utility.get_records(records_per_page, offset, file_to_read)
    elif Utility.sort_type == 1:
        records = Utility.get_records_reverse(records_per_page, offset, file_to_read)

    # show records    
    if records:
        Utility.show_records(records)

        # print total records at the bottom
        total = Utility.get_total_records(file_to_read)
        Utility.stdscr.addstr(23, 17, "{} | PAGE: {}".format(total, Utility.current_page))
    else:
        Utility.stdscr.addstr(23, 17, '0')
        Utility.stdscr.addstr(23, 50, '0 records found')

    # refresh screen
    Utility.stdscr.refresh()

def main(stdscr):

    # pass stdscr to Utility stdscr property
    Utility.stdscr = stdscr

    # hide cursor and get screen size
    curses.curs_set(False)
    y, x = Utility.stdscr.getmaxyx()

    # load records
    load_main_details(Utility.records_per_page, 0)

    # set default selector value and last page
    Utility.set_selector(1)
    Utility.set_last_page_phonebook()

    # main event loop
    key = Utility.stdscr.getch()
    while 1:

        # add new records
        if key == curses.KEY_F1:
            # reset current page to 1
            Utility.current_page = 1
            add()
            Utility.set_selector(1)
            Utility.set_last_page_phonebook()

        # search records
        elif key == curses.KEY_F2:
            # reset current page to 1
            Utility.current_page = 1
            search()

        # sort order
        elif key == curses.KEY_F3:

            # toggle sort type value
            if Utility.sort_type == 0:
                Utility.sort_type = 1
            elif Utility.sort_type == 1:
                Utility.sort_type = 0
            
            # reset current page to 1
            Utility.current_page = 1

            # reload records
            load_main_details(Utility.records_per_page, 0)

            # show currently selected sort type
            if Utility.sort_type == 0:
                sort_by = 'Ascending'
            elif Utility.sort_type == 1:
                sort_by = 'Descending'

            # set selector
            Utility.set_selector(1)

            Utility.stdscr.addstr(23, 50, "Sort By: {}".format(sort_by))

        # escape to exit
        elif key == 27:
            break

        # show previous records
        elif key == curses.KEY_F4:
            previous_page()
            Utility.set_selector(1)

        # show next records
        elif key == curses.KEY_F5:
            next_page()
            Utility.set_selector(1)

        # enter key for selecting a record
        elif key == 10:            
            selected_record()
            Utility.set_selector(1)

        # navigating records using arrow up
        elif key == curses.KEY_UP:
            if Utility.selector > 1: # greater than the first page
                Utility.selector -= 1
                Utility.set_selector(Utility.selector)
            else:
                if Utility.current_page != 1:
                    previous_page()
                    Utility.selector = Utility.total_records_on_page
                    Utility.set_selector(Utility.selector)

        # navigating records using arrow down
        elif key == curses.KEY_DOWN:
            if Utility.selector < Utility.total_records_on_page: # less than the last page
                Utility.selector += 1
                Utility.set_selector(Utility.selector)
            else:
                if Utility.current_page != Utility.phonebook_last_page:
                    next_page()
                    Utility.selector = 1
                    Utility.set_selector(Utility.selector)

        # checks for window resize event
        elif curses.is_term_resized(y, x) == True:
            Utility.stdscr.clear()
            curses.resizeterm(25, 80)
            load_main_details(Utility.records_per_page, 0)

        # capture keypress for main event loop
        key = Utility.stdscr.getch()


# check files if it exist then run main wrapper of curses library
msg = Utility.check_files_exists()
if msg == True:
    curses.wrapper(main)
else:
    print(msg)

# exit program message
print('Exited Phonebook. Bye!')