import curses
import os
import argparse as arg
import sys
from pathlib import Path as ppp

def cli() -> None:
    parser = arg.ArgumentParser(
        description="Nein! Simple Terminal Text Editor just like Nano! not Vim cuz i don't know how to exit Vim -_-"
    )
    parser.add_argument("filename", type=ppp, nargs="?", default="L.txt")
    parser.add_argument("Ctrl+S", type=str, nargs="?", help="Save the file", default="L.txt")
    parser.add_argument("Ctrl+X", type=str, nargs="?", help="Exit the editor", default="L.txt")
    parser.add_argument("Ctrl+Q", type=str, nargs="?", help="Move to left word", default="L.txt")
    parser.add_argument("Ctrl+W", type=str, nargs="?", help="Move to right word", default="L.txt")
    parser.add_argument("Ctrl+B", type=str, nargs="?", help="Copy selected text", default="L.txt")
    parser.add_argument("Ctrl+F", type=str, nargs="?", help="Cut selected text", default="L.txt")
    parser.add_argument("Ctrl+V", type=str, nargs="?", help="Paste selected text", default="L.txt")

    filename = parser.parse_args().filename
    curses.wrapper(main, filename)

def update_scroll(y, x, scroll_y, scroll_x, height, width):
    text_height = height - 2
    text_width = width - 1

    # Vertical scrolling
    if y < scroll_y:
        scroll_y = y
    elif y >= scroll_y + text_height:
        scroll_y = y - text_height + 1

    # Horizontal scrolling
    if x < scroll_x:
        scroll_x = x
    elif x >= scroll_x + text_width:
        scroll_x = x - text_width + 1
    return scroll_y, scroll_x

def goto_left(line, x):
    if not line:
        return 0

    while x > 0 and line[x - 1].isspace():
        x -= 1

    while x > 0 and not line[x - 1].isspace():
        x -= 1

    return x

def goto_right(line, x):
    if not line:
        return 0

    while x < len(line) - 1 and line[x].isspace():
        x += 1

    while x < len(line) - 1 and not line[x].isspace():
        x += 1

    return x

def ctrl_backspace(line, x):
    if not line or x == 0:
        return line, x

    start = goto_left(line, x)
    new_line = line[:start] + line[x:]
    new_x = start

    return new_line, new_x

clipboard = ""

def copy(line):
    if not line:
        return ""
    return line

def cut(line):
    if not line:
        return "", 0
    return "", 0

def paste(line, x, clipboard):
    if not line:
        return clipboard, len(clipboard)
    new_line = line[:x] + clipboard + line[x:]
    new_x = x + len(clipboard)
    return new_line, new_x

def main(stdscr, filename):
    global clipboard
    curses.curs_set(1)
    stdscr.nodelay(False)
    scroll_y, scroll_x = 0, 0

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            box = f.read().splitlines() # Semacam Buffer lah ya
        if not box: box = [""] # lu gak tau buffer? buffer tuh semacam text box yang kerja di nano
    else:
        box = [""]

    y, x = 0, 0
    msg = f"Now Editing: {filename} "

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        #Rendering
        for screen_y in range(height - 2):
            file_y = scroll_y + screen_y

            if file_y >= len(box):
                break
            
            line = box[file_y]
            visible_line = line[scroll_x:scroll_x + width - 1]

            try:
                stdscr.addstr(screen_y, 0, visible_line)
            except curses.error:
                pass

        #Menu
        try:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(height-2, 0, msg[:width-1].ljust(width-1))
            
            stdscr.insstr(height-1, 0, "^X Exit | ^S Save | ^Q Left Word | ^W Right Word | ^B Copy | ^F Cut | ^V Paste".ljust(width-1))
            stdscr.attroff(curses.A_REVERSE)
        except curses.error:
            pass 

        # Cursor Position
        scroll_y, scroll_x = update_scroll(
            y, x,
            scroll_y, scroll_x,
            height, width
        )

        screen_y = y - scroll_y
        screen_x = x - scroll_x
        stdscr.move(screen_y, screen_x)
        
        # Keyboard Input
        key = stdscr.getch()
        if key == 24: # CTRL+X (Exit)
            break
        elif key == 17: # CTRL+Q (Move to Left Word)
            x = goto_left(box[y], x)
        elif key == 23: # CTRL+W (Move to Right Word)
            x = goto_right(box[y], x)
        elif key == 4: # CTRL+D (Backspace)
            box[y], x = ctrl_backspace(box[y], x)
        elif key == 22: # CTRL+V (Paste)
            box[y], x = paste(box[y], x, clipboard)
        elif key == 2: # CTRL+B (Copy)
            clipboard = copy(box[y])
        elif key == 6: # CTRL+F (Cut)
            clipboard = copy(box[y])
            box[y], x = cut(box[y])
        elif key == 19: # CTRL+S (Save)
            try:
                with open(filename, "w") as f:
                    f.write("\n".join(box))
                msg = f"Saved to {filename}! "
            except Exception as e:
                msg = f"Error saving: {e} "
        elif key == curses.KEY_UP: #UP
            if y > 0:
                y -= 1
                x = min(x, len(box[y]))
        elif key == curses.KEY_DOWN: #D
            if y < len(box) - 1:
                y += 1
                x = min(x, len(box[y]))
        elif key == curses.KEY_LEFT: #L
            if x > 0:
                x -= 1
            elif y > 0:
                y -= 1
                x = len(box[y])
        elif key == curses.KEY_RIGHT:
            if x < len(box[y]):
                x += 1
            elif y < len(box) - 1: # Pindah ke awal baris berikutnya
                y += 1
                x = 0
        elif key in (8, 127, curses.KEY_BACKSPACE):
            if x > 0:
                box[y] = box[y][:x-1] + box[y][x:]
                x -= 1
            elif y > 0:
                old_x = len(box[y-1])
                box[y-1] += box[y]
                box.pop(y)
                y -= 1
                x = old_x
        elif key in (10, 13): # Enter
            enter = box[y]
            box[y] = enter[:x]
            box.insert(y + 1, enter[x:])
            y += 1 # Kebawah / tombol enter 1 baris
            x = 0
        elif key == curses.KEY_PPAGE: #P UP
            if x > 0:
                x -= 1
            elif y > 0:
                y -= 5
                x = len(box[y])
        elif key == curses.KEY_NPAGE: #P DOWN
            if x > 0:
                x += 1
            elif y > 0:
                y += 5
                x = len(box[y])
        elif 32 <= key <= 126:
            box[y] = box[y][:x] + chr(key) + box[y][x:]
            x += 1

if __name__ == "__main__":
    cli()