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

    records = Utility.get_records(10)
    stdscr.addstr(3, 25,  "ID  Name                    Phone")
    stdscr.addstr(4, 25,  "{}   {}                {}".format(records[0]['id'], records[0]['name'], records[0]['phone']))
    stdscr.addstr(5, 25,  "{}   {}                {}".format(records[1]['id'], records[1]['name'], records[1]['phone']))
    stdscr.addstr(6, 25,  "{}   {}                {}".format(records[2]['id'], records[2]['name'], records[2]['phone']))
    stdscr.addstr(7, 25,  "{}   {}                {}".format(records[3]['id'], records[3]['name'], records[3]['phone']))
    stdscr.addstr(8, 25,  "{}   {}                {}".format(records[4]['id'], records[4]['name'], records[4]['phone']))
    stdscr.addstr(9, 25,  "{}   {}                {}".format(records[5]['id'], records[5]['name'], records[5]['phone']))
    stdscr.addstr(10, 25, "{}   {}                {}".format(records[6]['id'], records[6]['name'], records[6]['phone']))
    stdscr.addstr(11, 25, "{}   {}                {}".format(records[7]['id'], records[7]['name'], records[7]['phone']))
    stdscr.addstr(12, 25, "{}   {}                {}".format(records[8]['id'], records[8]['name'], records[8]['phone']))
    stdscr.addstr(13, 25, "{}   {}                {}".format(records[9]['id'], records[9]['name'], records[9]['phone']))

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

        elif curses.is_term_resized(y, x) == True:
            stdscr.clear()
            curses.resizeterm(25, 80)
            skins.main(stdscr)
            stdscr.refresh()

        key = stdscr.getch()


msg = Utility.check_files_exists()
if msg == True:
    curses.wrapper(main)
else:
    print(msg)

print('Exited Phonebook. Bye!')