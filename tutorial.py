import curses
# Wrapper initializes curses, and when program is done, it will reset everything back to original state
from curses import wrapper

# variable, stdscr = standard output screen


def start_screen(stdscr):
    stdscr.clear()  # clears
    stdscr.addstr(0, 0, 'Test Your Speed!')  # adds string
    stdscr.addstr('\nPress any key to begin!')  # adds string
    stdscr.refresh()  # refreshes screen# program does'nt immediately close, it needs an interaction from the user
    stdscr.getkey()


def wpm_test(stdscr):
    target_text = 'Hello world this is a test'  # first string that gets shown
    current_text = []

    while True:
        key = stdscr.getkey()
        current_text.append(key)

        stdscr.clear()  # clears
        stdscr.addstr(target_text)  # adds string

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

            stdscr.refresh()  # refreshes screen# program does'nt immediately close, it needs an interaction from the user


def main(stdscr):
    # changes text color and then, bg  color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # function is called to show Press any key text
    start_screen(stdscr)
    wpm_test(stdscr)

    # wrapper is a function, will print out hello world
wrapper(main)


# use python3 tutorial.py to run code
