import curses
# Wrapper initializes curses, and when program is done, it will reset everything back to original state
from curses import wrapper

# variable, stdscr = standard output screen


def main(stdscr):
    stdscr.clear()  # clears
    stdscr.addstr('Hello World!')
    stdscr.refresh()  # refreshes screen
    stdscr.getkey()  # program doesnt immediately close, it needs an interaction from the user


    # wrapper is a function, will print out hello world
wrapper(main)


# use python3 tutorial.py to run code
