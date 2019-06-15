# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import math as m
import modules.skins as skins
from modules.utility import Utility

def next_record():

    # get last page
    total_row_count = Utility.get_total_records()
    last_page = m.ceil(total_row_count/Utility.records_per_page)

    # get current page
    page_num = Utility.current_page

    # go to next page and check if > last page
    page_num += 1
    if page_num == last_page:
        page_num = last_page - 1

    # update page number
    Utility.current_page = page_num

    # get records equivalent in page number, start and end record index
    end_index = page_num * Utility.records_per_page
    start_index = end_index - (Utility.records_per_page - 1)
    next_page_index = end_index + 1

    # show next page
    load_main_details(Utility.records_per_page, next_page_index)

def previous_record():

    # get current page
    page_num = Utility.current_page

    # go to previous page and check if < 1
    page_num -= 1
    if page_num == 0:
        page_num = 1

    # update current page
    Utility.current_page = page_num
    
    # get records equivalent in page number, start and end record index
    end_index = page_num * Utility.records_per_page
    start_index = end_index - (Utility.records_per_page - 1)  

    # show next page
    load_main_details(Utility.records_per_page, start_index)

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
    name = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 30))
    while 1:
        if name == '':
            Utility.stdscr.addstr(6, 27, ' '*30)
            Utility.stdscr.addstr(23, 50, 'Name must not be empty.')
            Utility.stdscr.refresh()
            name = Utility.bytes_to_str(Utility.stdscr.getstr(6, 27, 30))
        else:
            skins.clear_message()
            break

    # accept and validate phone
    phone = Utility.bytes_to_str(Utility.stdscr.getstr(7, 27, 7))
    numbers = set('0123456789')
    while 1:
        if phone == '':
            Utility.stdscr.addstr(7, 27, '       ')
            Utility.stdscr.addstr(23, 50, 'Number must not be empty.')
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(7, 27, 7))
        elif set(phone).issubset(numbers) == False or len(phone) < 7:
            Utility.stdscr.addstr(7, 27, '       ')
            Utility.stdscr.addstr(23, 50, 'Incorrect Number.')
            Utility.stdscr.refresh()
            phone = Utility.bytes_to_str(Utility.stdscr.getstr(7, 27, 7))
        else:
            break

        skins.clear_message()

    # checks if user wants to save or cancel
    Utility.cursor_display(0)
    Utility.stdscr.addstr(10, 27, '[ y ] - Save [ n ] Cancel')
    key = None
    
    # 'y'=121 and 'n'=110
    while (key != 121 and key != 110):

        key = Utility.stdscr.getch()
        
        if key == 121:
            Utility.save_record(int(current_id), name, phone)
            Utility.update_current_id(int(current_id))
            break

        elif key == 110:
            break

    # refresh screen show records again
    Utility.stdscr.clear()
    load_main_details(Utility.records_per_page, 0)
    Utility.current_page = 1


def load_main_details(records_per_page, offset):

    # clear screen
    Utility.stdscr.clear()
    skins.main()

    # check the sort_type
    if Utility.sort_type == 0:
        records = Utility.get_records(records_per_page, offset)
    elif Utility.sort_type == 1:
        records = Utility.get_records_reverse(records_per_page, offset)

    # show records    
    if records:
        Utility.show_records(records)

        # print total records at the bottom
        total = Utility.get_total_records()
        Utility.stdscr.addstr(23, 17, "{} | PAGE: {}".format(total, Utility.current_page))
    else:        
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

    # main event loop
    key = Utility.stdscr.getch()
    while 1:

        # add new records
        if key == curses.KEY_F1:
            add()

        # search records
        elif key == curses.KEY_F2:
            Utility.stdscr.addstr(23, 50, 'Pressed F2      ')

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

            Utility.stdscr.addstr(23, 50, "Sort By: {}".format(sort_by))

        # escape to exit
        elif key == 27:
            break

        # show previous records
        elif key == curses.KEY_F4:
            previous_record()

        # show next records
        elif key == curses.KEY_F5:
            next_record()

        # enter key for selecting a record
        elif key == 10:
            Utility.stdscr.addstr(23, 50, 'Pressed ENTER   ')

        # navigating records using arrow up
        elif key == curses.KEY_UP:
            Utility.stdscr.addstr(23, 50, 'Pressed Up Key  ')

        # navigating records using arrow up
        elif key == curses.KEY_DOWN:
            Utility.stdscr.addstr(23, 50, 'Pressed Down Key')

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