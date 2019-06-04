# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import modules.skins as skins

def main(stdscr):

    curses.curs_set(False)

    skins.main(stdscr)
    key = stdscr.getch()

    # main event loop
    while 1:

        # escape to exit
        if key == 27:
            # code here ...
            break

        elif key == curses.KEY_F1:
            stdscr.addstr(23, 50, 'Pressed F1   ')

        elif key == curses.KEY_F2:
            stdscr.addstr(23, 50, 'Pressed F2   ')

        elif key == curses.KEY_F3:
            stdscr.addstr(23, 50, 'Pressed F3   ')

        # enter key
        elif key == 10:
            stdscr.addstr(23, 50, 'Pressed ENTER')

        key = stdscr.getch()

curses.wrapper(main)

print('Exited Phonebook. Bye!')