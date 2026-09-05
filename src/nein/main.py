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
    filename = parser.parse_args().filename
    curses.wrapper(main, filename)


def main(stdscr, filename):
    curses.curs_set(1)
    stdscr.nodelay(False)
    
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
        for idx, line in enumerate(box):
            if idx < height - 2: # Sisakan ruang untuk baris status
                stdscr.addstr(idx, 0, line[:width-1])

        #Menu
        try:
            stdscr.attron(curses.A_REVERSE)
            #Tambah MSG, jadi keinget micin coy -_- 
            stdscr.addstr(height-2, 0, msg[:width-1].ljust(width-1))
            
            stdscr.insstr(height-1, 0, "Ctrl+X Exit | Ctrl+S Save".ljust(width-1))
            stdscr.attroff(curses.A_REVERSE)
        except curses.error:
            pass 

        # 3. Pindahkan kursor
        stdscr.move(y, x)
        
        # 4. Input Keyboard
        key = stdscr.getch()

        if key == 24: # CTRL+X (Exit)
            break
        
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