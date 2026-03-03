# Nein Nein Nein
import sys
import curses
from curses import wrapper as wra

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    attr = curses.color_pair(1)
    stdscr.addstr(0, 50, "Nein\n", attr)

    x, y = 0, 0
    while True:
        insert = stdscr.getkey()
        if insert == "KEY_LEFT":
            x -= 1
        elif insert == "KEY_RIGHT":
            x += 1
        elif insert == "KEY_UP":
            y -= 1
        elif insert == "KEY_DOWN":
            y += 1

        stdscr.clear()
        stdscr.addstr(y,x, "0")
        stdscr.refresh()


wra(main)