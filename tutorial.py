import curses
# Wrapper initializes curses, and when program is done, it will reset everything back to original state
from curses import wrapper

# variable, stdscr = standard output screen


def main(stdscr):
    # changes text color and then, bg  color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()  # clears
    stdscr.addstr(1, 5, 'Hello World!')  # adds string
    stdscr.refresh()  # refreshes screen
    stdscr.getkey()  # program doesnt immediately close, it needs an interaction from the user

    # wrapper is a function, will print out hello world
wrapper(main)


# use python3 tutorial.py to run code
