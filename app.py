# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import modules.skins as skins
from modules.utility import Utility

def main(stdscr):

    curses.curs_set(False)
    y, x = stdscr.getmaxyx()

    skins.main(stdscr)

    # reads first 15 records and displays them
    records = Utility.get_records(15)
    Utility.show_records(stdscr, records)

    key = stdscr.getch()

    # main event loop
    while 1:

        # escape to exit
        if key == 27:
            break

        elif key == curses.KEY_F1:
            stdscr.addstr(23, 50, 'Pressed F1      ')

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