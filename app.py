# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
from modules.gui import *

def main(stdscr):

    # w: 80, h: 25 (default window size)
    h, w = stdscr.getmaxyx()
    title = GuiObject(h, w,"Welcome!")
    stdscr.addstr(title.h_center(), title.w_center_text(), title.text)
    stdscr.getch()

curses.wrapper(main)