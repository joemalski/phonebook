# Filename: skins.py
# Date: June 4, 2019
# Description: The window or "skins" of the program.
# By: Joel F. Malinao

import curses
from modules.utility import Utility
from modules.gui import GuiObject

# main skin
def main():

    # set the color pair, foreground, background
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    h, w = Utility.stdscr.getmaxyx()

    # title
    title = GuiObject(h, w, 'M Y   P H O N E B O O K   v 1 . 0')
    Utility.stdscr.addstr(0, title.w_center_text(), title.text)

    # title line
    title_line = GuiObject(h, w, ('-' * 80))
    Utility.stdscr.addstr(1, 0, title_line.text)

    # search header label
    Utility.stdscr.addstr(3, 20, '                 ')
    Utility.stdscr.attron(curses.color_pair(1))    
    Utility.stdscr.addstr(3, 20, 'ALL PHONE RECORDS')
    Utility.stdscr.attroff(curses.color_pair(1))

    # add button
    add_btn = GuiObject(h, w, '[F1]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(3, 2, add_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    add_btn_desc = GuiObject(h, w, ' ADD')
    Utility.stdscr.addstr(3, 6, add_btn_desc.text)

    # search button
    search_btn = GuiObject(h, w, '[F2]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(5, 2, search_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    search_btn_desc = GuiObject(h, w, ' SEARCH')
    Utility.stdscr.addstr(5, 6, search_btn_desc.text)

    # sort by button
    sortby_btn = GuiObject(h, w, '[F3]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(7, 2, sortby_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    sortby_btn_desc = GuiObject(h, w, ' SORT BY')
    Utility.stdscr.addstr(7, 6, sortby_btn_desc.text)

    # exit button
    exit_btn = GuiObject(h, w, '[ESC]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(9, 2, exit_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    exit_btn_desc = GuiObject(h, w, ' EXIT')
    Utility.stdscr.addstr(9, 7, exit_btn_desc.text)

    # menu line
    Utility.stdscr.addstr(11, 0, '-----------------')

    # previous button
    previous_btn = GuiObject(h, w, '[F4]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(13, 2, previous_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    previous_btn_desc = GuiObject(h, w, ' PREVIOUS')
    Utility.stdscr.addstr(13, 6, previous_btn_desc.text)

    # next button
    next_btn = GuiObject(h, w, '[F5]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(15, 2, next_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    next_btn_desc = GuiObject(h, w, ' NEXT')
    Utility.stdscr.addstr(15, 6, next_btn_desc.text)

    # arrows up, down and enter
    up_arrow_btn = GuiObject(h, w, '[↑↓]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(17, 2, up_arrow_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    arrow_up_btn_desc = GuiObject(h, w, ' NAVIGATION')
    Utility.stdscr.addstr(17, 6, arrow_up_btn_desc.text)
    entry_btn = GuiObject(h, w, '[ENTER]')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(19, 2, entry_btn.text)
    Utility.stdscr.attroff(curses.color_pair(1))
    entry_btn_desc = GuiObject(h, w, ' SELECTION')
    Utility.stdscr.addstr(19, 9, entry_btn_desc.text)

    # footer line
    footer_line = GuiObject(h, w, ('-' * 80))
    Utility.stdscr.addstr(22, 0, footer_line.text)

    # footer label
    footer_lbl = GuiObject(h, w, 'TOTAL RECORDS: ')
    Utility.stdscr.addstr(23, 2, footer_lbl.text)

# add skin
def add():

    # get screen height and width
    h, w = Utility.stdscr.getmaxyx()

    # add header label
    Utility.stdscr.addstr(3, 20, '                 ')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(3, 20, 'ADD NEW RECORD')
    Utility.stdscr.attroff(curses.color_pair(1))

    # add input labels
    Utility.stdscr.addstr(5, 20, '   ID: ')
    Utility.stdscr.addstr(6, 20, ' NAME: ')
    Utility.stdscr.addstr(7, 20, 'PHONE: ')

# selected record skin
def selected_record():

    # get screen height and width
    h, w = Utility.stdscr.getmaxyx()

    # add header label
    Utility.stdscr.addstr(3, 20, '                 ')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(3, 20, 'SELECTED RECORD')
    Utility.stdscr.attroff(curses.color_pair(1))

    # add input labels
    Utility.stdscr.addstr(5, 20, '   ID: ')
    Utility.stdscr.addstr(6, 20, ' NAME: ')
    Utility.stdscr.addstr(7, 20, 'PHONE: ')

# search skin
def search():

    # get screen height and width
    h, w = Utility.stdscr.getmaxyx()

    # search header label
    Utility.stdscr.addstr(3, 20, '                 ')
    Utility.stdscr.attron(curses.color_pair(1))
    Utility.stdscr.addstr(3, 20, 'SEARCH RECORDS')
    Utility.stdscr.attroff(curses.color_pair(1))

# clear message line
def clear_message():
    
    # clears messages
    Utility.stdscr.addstr(23, 40, ' '*40)