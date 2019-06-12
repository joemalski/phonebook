# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import modules.skins as skins
from modules.utility import Utility

def add():

    # add skins
    Utility.stdscr.clear()
    skins.main()
    skins.add()

    lines = Utility.get_total_records()
    Utility.stdscr.addstr(23, 17, str(lines))
    
    Utility.stdscr.refresh()

    # get the current id
    current_id = Utility.get_id()
    Utility.stdscr.addstr(5, 26, current_id)

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

    Utility.cursor_display(0)
    Utility.stdscr.addstr(10, 27, '[ y ] - Save [ n ] Cancel')
    key = None
    
    # check if user wants to save it or not
    # 'y'=121 and 'n'=110
    while (key != 121 and key != 110):

        key = Utility.stdscr.getch()
        
        if key == 121:
            Utility.save_record(int(current_id), name, phone)
            Utility.update_current_id(int(current_id))
            break

        elif key == 110:
            break

    Utility.stdscr.clear()
    load_main_details()


def load_main_details():

    Utility.stdscr.clear()
    skins.main()

    # reads first 4 records and displays them and
    # check the sort_type
    if Utility.sort_type == 0:
        records = Utility.get_records(4)
    elif Utility.sort_type == 1:
        records = Utility.get_records_reverse(4)

    # show records    
    if records:
        Utility.show_records(records)

        # print total records at the bottom
        lines = Utility.get_total_records()
        Utility.stdscr.addstr(23, 17, str(lines))
    else:
        Utility.stdscr.addstr(23, 50, '0 records found')

def main(stdscr):

    # pass stdscr to Utility stdscr property
    Utility.stdscr = stdscr

    curses.curs_set(False)
    y, x = Utility.stdscr.getmaxyx()

    load_main_details()

    key = Utility.stdscr.getch()

    # main event loop
    while 1:

        # escape to exit
        if key == 27:
            break

        # add new records
        elif key == curses.KEY_F1:
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

            # reload records
            load_main_details()

            Utility.stdscr.addstr(23, 50, "sort_type: {}".format(Utility.sort_type))

        # enter key
        elif key == 10:
            Utility.stdscr.addstr(23, 50, 'Pressed ENTER   ')

        elif key == curses.KEY_UP:
            Utility.stdscr.addstr(23, 50, 'Pressed Up Key  ')

        elif key == curses.KEY_DOWN:
            Utility.stdscr.addstr(23, 50, 'Pressed Down Key')

        elif key == curses.KEY_F4:
            Utility.stdscr.addstr(23, 50, 'Pressed PREVIOUS')

        elif key == curses.KEY_F5:
            Utility.stdscr.addstr(23, 50, 'Pressed NEXT    ')

        elif curses.is_term_resized(y, x) == True:
            Utility.stdscr.clear()
            curses.resizeterm(25, 80)
            load_main_details()

        key = Utility.stdscr.getch()


msg = Utility.check_files_exists()
if msg == True:
    curses.wrapper(main)
else:
    print(msg)

print('Exited Phonebook. Bye!')