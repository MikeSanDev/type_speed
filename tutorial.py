import curses
# Wrapper initializes curses, and when program is done, it will reset everything back to original state
from curses import wrapper
import time
# variable, stdscr = standard output screen

# START SCREEN


def start_screen(stdscr):
    stdscr.clear()  # clears
    stdscr.addstr(0, 0, 'Test Your Speed!')  # adds string
    stdscr.addstr('\nPress any key to begin!')  # adds string
    stdscr.refresh()  # refreshes screen# program does'nt immediately close, it needs an interaction from the user
    stdscr.getkey()


# OVER LAYING TEXT
# these are the parameters, wpm is an optional parameter and will default to 0 if none is specified
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)  # adds string

    # enumerate will get us the element from current_text as well as the index (i) in the list
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # if correct, will turn green
        if char != correct_char:
            color = curses.color_pair(2)  # if incorrect, will turn red

        # this will overlayed on top of the target text - starting with the index 0
        stdscr.addstr(0, i, char, color)

# USER KEY PRESSES


def wpm_test(stdscr):
    target_text = 'Hello world this is a test'  # first string that gets shown
    current_text = []  # keeps track of all keys that have been pressed
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        # characters per minute
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        # example: 30 chars 15 seconds
        # 15 sec / 60 sec = 0.25
        # 30 chars / 0.25 = 120 characters per minute

        # character/minute / 5 = words per minute (WPM)
        # used round function to round up WPM

        stdscr.clear()  # clears
        display_text(stdscr, target_text, current_text, )

        stdscr.addstr(curses.LINES - 1, 0, f'WPM: {wpm}', curses.color_pair(3))
        stdscr.refresh()  # refreshes screen# program does'nt immediately close, it needs an interaction from the user

        # check if user current text is equal to target text
        if "".join(current_text) == target_text:  # adds spaces to current_text list
            stdscr.nodelay(False)
            break  # breaks if nodelay is false

        try:  # app wont crash if the user does not type anything
            key = stdscr.getkey()
        except:
            continue  # brings back to the while loop

        if ord(key) == 27:  # 27 is the ASCII character for esc
            break
        # if key is back space and other keys then it will pop off last key in current text
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()  # much easier to pop values off in a list vs an array
        elif len(current_text) < len(target_text):
            current_text.append(key)

# TEXT STYLING


def main(stdscr):
    # changes text color and then, bg  color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    # function is called to show Press any key text
    start_screen(stdscr)
    while True:  # this will reset the game
        wpm_test(stdscr)
        stdscr.addstr(
            2, 0, "You completed the test! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

    # wrapper is a function, will print out hello world
wrapper(main)


# use python3 tutorial.py to run code
