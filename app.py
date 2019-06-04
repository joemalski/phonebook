# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
import modules.skins as skins

def main(stdscr):

    curses.curs_set(False)

    skins.main(stdscr)

    stdscr.getch()

curses.wrapper(main)