# Filename: skins.py
# Date: June 4, 2019
# Description: The window or "skins" of the program.
# By: Joel F. Malinao

import curses
from modules.gui import GuiObject

# main skin
def main(stdscr):

    # set the color pair, foreground, background
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    h, w = stdscr.getmaxyx()

    # title
    title = GuiObject(h, w, 'My Phonebook')
    stdscr.addstr(0, title.w_center_text(), title.text)

    # title line
    title_line = GuiObject(h, w, ('-' * 80))
    stdscr.addstr(1, 0, title_line.text)

    # add button
    add_btn = GuiObject(h, w, '[F1]')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(3, 2, add_btn.text)
    stdscr.attroff(curses.color_pair(1))
    add_btn_desc = GuiObject(h, w, ' ADD')
    stdscr.addstr(3, 6, add_btn_desc.text)

    # search button
    search_btn = GuiObject(h, w, '[F2]')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(5, 2, search_btn.text)
    stdscr.attroff(curses.color_pair(1))
    search_btn_desc = GuiObject(h, w, ' SEARCH')
    stdscr.addstr(5, 6, search_btn_desc.text)

    # sort by button
    sortby_btn = GuiObject(h, w, '[F3]')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(7, 2, sortby_btn.text)
    stdscr.attroff(curses.color_pair(1))
    sortby_btn_desc = GuiObject(h, w, ' SORT BY')
    stdscr.addstr(7, 6, sortby_btn_desc.text)

    # exit button
    exit_btn = GuiObject(h, w, '[ESC]')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(9, 2, exit_btn.text)
    stdscr.attroff(curses.color_pair(1))
    exit_btn_desc = GuiObject(h, w, ' EXIT')
    stdscr.addstr(9, 7, exit_btn_desc.text)

    # menu line
    stdscr.addstr(11, 0, '-----------------')

    # previous button
    previous_btn = GuiObject(h, w, '[F4]')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(13, 2, previous_btn.text)
    stdscr.attroff(curses.color_pair(1))
    previous_btn_desc = GuiObject(h, w, ' PREVIOUS')
    stdscr.addstr(13, 6, previous_btn_desc.text)

    # next button
    next_btn = GuiObject(h, w, '[F5]')
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(15, 2, next_btn.text)
    stdscr.attroff(curses.color_pair(1))
    next_btn_desc = GuiObject(h, w, ' NEXT')
    stdscr.addstr(15, 6, next_btn_desc.text)

    # footer line
    footer_line = GuiObject(h, w, ('-' * 80))
    stdscr.addstr(22, 0, footer_line.text)

    # footer label
    footer_lbl = GuiObject(h, w, 'TOTAL RECORDS: ')
    stdscr.addstr(23, 2, footer_lbl.text)

# add skin
def add(stdscr):
    # set the color pair, foreground, background
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    h, w = stdscr.getmaxyx()

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(3, 20, 'ADD NEW RECORD')
    stdscr.attroff(curses.color_pair(1))

    stdscr.addstr(5, 20, '   ID: ')
    stdscr.addstr(6, 20, ' NAME: ')
    stdscr.addstr(7, 20, 'PHONE: ')

# clear message line
def clear_message(stdscr):
    stdscr.addstr(23, 40, ' '*40)





