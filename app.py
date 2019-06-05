# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import modules.skins as skins
from modules.utility import Utility

def main(stdscr):

    curses.curs_set(False)

    skins.main(stdscr)
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
            stdscr.addstr(23, 50, 'Pressed PREVIOUS')

        elif key == curses.KEY_DOWN:
            stdscr.addstr(23, 50, 'Pressed NEXT    ')

        key = stdscr.getch()

records = Utility.get_records(10)

for record in records:
    print(record)

'''
msg = Utility.check_files_exists()
if msg == True:
    curses.wrapper(main)
else:
    print(msg)
'''
print('Exited Phonebook. Bye!')