# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import modules.skins as skins
from modules.utility import Utility

def add(stdscr):

    # add skins
    stdscr.clear()
    skins.main(stdscr)
    skins.add(stdscr)
    stdscr.refresh()

    # get the current id
    current_id = Utility.get_id()
    stdscr.addstr(5, 26, current_id)

    Utility.cursor_display(1)

    # accept and validate name
    name = Utility.bytes_to_str(stdscr.getstr(6, 27, 30))
    while 1:
        if name == '':
            stdscr.addstr(6, 27, ' '*30)
            stdscr.addstr(23, 50, 'Name must not be empty.')
            stdscr.refresh()
            name = Utility.bytes_to_str(stdscr.getstr(6, 27, 30))
        else:
            skins.clear_message(stdscr)
            break

    # accept and validate phone
    phone = Utility.bytes_to_str(stdscr.getstr(7, 27, 7))
    numbers = set('0123456789')
    while 1:
        if phone == '':
            stdscr.addstr(7, 27, '       ')
            stdscr.addstr(23, 50, 'Number must not be empty.')
            stdscr.refresh()
            phone = Utility.bytes_to_str(stdscr.getstr(7, 27, 7))
        elif set(phone).issubset(numbers) == False or len(phone) < 7:
            stdscr.addstr(7, 27, '       ')
            stdscr.addstr(23, 50, 'Incorrect Number.')
            stdscr.refresh()
            phone = Utility.bytes_to_str(stdscr.getstr(7, 27, 7))
        else:
            break

        skins.clear_message(stdscr)

    Utility.cursor_display(0)
    Utility.save_record(stdscr, int(current_id), name, phone)

def main(stdscr):

    curses.curs_set(False)
    y, x = stdscr.getmaxyx()

    skins.main(stdscr)

    # record labels (static)
    stdscr.addstr(3, 20,  "ID  Name                                Phone")

    # reads first 15 records and displays them
    records = Utility.get_records(15)
    if records:
        Utility.show_records(stdscr, records)
    else:
        stdscr.addstr(23, 50, '0 records found')

    key = stdscr.getch()

    # main event loop
    while 1:

        # escape to exit
        if key == 27:
            break

        elif key == curses.KEY_F1:
            #stdscr.addstr(23, 50, 'Pressed F1      ')
            add(stdscr)

        elif key == curses.KEY_F2:
            stdscr.addstr(23, 50, 'Pressed F2      ')

        elif key == curses.KEY_F3:
            stdscr.addstr(23, 50, 'Pressed F3      ')

        # enter key
        elif key == 10:
            stdscr.addstr(23, 50, 'Pressed ENTER   ')

        elif key == curses.KEY_UP:
            stdscr.addstr(23, 50, 'Pressed Up Key  ')

        elif key == curses.KEY_DOWN:
            stdscr.addstr(23, 50, 'Pressed Down Key')

        elif key == curses.KEY_F4:
            stdscr.addstr(23, 50, 'Pressed PREVIOUS')

        elif key == curses.KEY_F5:
            stdscr.addstr(23, 50, 'Pressed NEXT    ')

        elif curses.is_term_resized(y, x) == True:
            stdscr.clear()
            curses.resizeterm(25, 80)
            skins.main(stdscr)
            Utility.show_records(stdscr, records)
            stdscr.refresh()

        key = stdscr.getch()


msg = Utility.check_files_exists()
if msg == True:
    curses.wrapper(main)
else:
    print(msg)

print('Exited Phonebook. Bye!')