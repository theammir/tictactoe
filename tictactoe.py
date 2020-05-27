from tkinter import *
import time
import random

MULTIPLAYER = input('Do you want to play with CPU? (y/n): ').strip().lower()
if (MULTIPLAYER == 'n'):
    MULTIPLAYER = True
else:
    MULTIPLAYER = False

YOU = input('What want you to play with? (x/o): ').strip()
if not (YOU.lower() in ('x', 'o')):
    YOU = 'X'
else:
    YOU = YOU.upper()

CURRENT_MOVE = 'X' # O

root = Tk()
root.geometry('275x275')
root.resizable(False, False)

winner = Label(root, font = 'Arial 14', text = 'Current: X', fg = 'blue')


class Cell(Button):
    @property
    def clicked(self):
        return self['text'] in 'XO'

def check_cells(cell1, cell2, cell3):
    if (cell1['text'] == cell2['text'] and cell1['text'] == cell3['text']):
        if (all([cell1.clicked, cell2.clicked, cell3.clicked])):
            return True
    else:
        return False

def checkwin():
    global BUTTONS
    COMBS = ['123', '147', '159', '258', '369', '357', '456', '789']
    for comb in COMBS:
        cell1 = BUTTONS[int(comb[0]) - 1]
        cell2 = BUTTONS[int(comb[1]) - 1]
        cell3 = BUTTONS[int(comb[2]) - 1]
        if (check_cells(cell1, cell2, cell3)):
            return True
    return False

def make_move():
    global BUTTONS, CURRENT_MOVE
    if not (MULTIPLAYER):
        for i in BUTTONS:
            i['state'] = DISABLED
        time.sleep(random.random())
        onclick(BUTTONS.index(random.choice(list(filter(lambda i: i.clicked == False, BUTTONS)))))
        for i in BUTTONS:
            i['state'] = NORMAL


def onclick(index):
    global BUTTONS, CURRENT_MOVE
    if not (BUTTONS[index].clicked):
        BUTTONS[index]['text'] = CURRENT_MOVE
        if (all([i.clicked for i in BUTTONS])):
            winner['text'] = f"It's a draw, man!"
            for i in BUTTONS:
                i['text'] = '_'
                i['command'] = None
            return

        if (checkwin()):
            winner['text'] = f'Winner: {CURRENT_MOVE}!'
            for i in BUTTONS:
                i['text'] = CURRENT_MOVE
                i['command'] = None
            return

        CURRENT_MOVE = 'O' if CURRENT_MOVE == 'X' else 'X'
        winner['text'] = f'Current: {CURRENT_MOVE}'
        if (CURRENT_MOVE != YOU):
            make_move()
    else:
        return False


def move_onclick0():
    onclick(0)

def move_onclick1():
    onclick(1)

def move_onclick2():
    onclick(2)

def move_onclick3():
    onclick(3)

def move_onclick4():
    onclick(4)

def move_onclick5():
    onclick(5)

def move_onclick6():
    onclick(6)

def move_onclick7():
    onclick(7)

def move_onclick8():
    onclick(8)

BUTTONS = [
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick0),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick1),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick2),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick3),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick4),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick5),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick6),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick7),
    Cell(root, text = '_', width = 3, font = 'Ariel 24', command = move_onclick8),
]

distancex = 30
distancey = 30

for i in range(len(BUTTONS)):
    BUTTONS[i].place(x = distancex, y = distancey)
    if (i in [2, 5, 8]):
        distancex = 30
        distancey += 75
    else:
        distancex += 75

winner.pack()

if (CURRENT_MOVE != YOU):
    make_move()

root.mainloop()
