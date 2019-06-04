# Filename: app.py
# Date: June 3, 2019
# Description: The program's loader.
# By: Joel F. Malinao

import curses
from modules.gui import *

def main(stdscr):

    curses.curs_set(False)
    h, w = stdscr.getmaxyx()

    # title
    title = GuiObject(h, w, 'My Phonebook')
    stdscr.addstr(0, title.w_center_text(), title.text)

    # title line
    title_line = GuiObject(h, w, ('-' * 80))
    stdscr.addstr(1, 0, title_line.text)

    # add button
    add_btn = GuiObject(h, w, '[F1] ADD')
    stdscr.addstr(3, 2, add_btn.text)

    # search button
    search_btn = GuiObject(h, w, '[F2] SEARCH')
    stdscr.addstr(5, 2, search_btn.text)

    # sort by button
    sortby_btn = GuiObject(h, w, '[F3] SORT BY')
    stdscr.addstr(7, 2, sortby_btn.text)

    # exit button
    exit_btn = GuiObject(h, w, '[F4] EXIT')
    stdscr.addstr(9, 2, exit_btn.text)

    # menu line
    stdscr.addstr(11, 0, '-----------------')

    # previous button
    previous_btn = GuiObject(h, w, '[F5] PREVIOUS')
    stdscr.addstr(13, 2, previous_btn.text)

    # next button
    next_btn = GuiObject(h, w, '[F6] NEXT')
    stdscr.addstr(15, 2, next_btn.text)

    # footer line
    footer_line = GuiObject(h, w, ('-' * 80))
    stdscr.addstr(22, 0, footer_line.text)

    # footer label
    footer_lbl = GuiObject(h, w, 'Total Records: ')
    stdscr.addstr(23, 2, footer_lbl.text)

    stdscr.getch()

curses.wrapper(main)