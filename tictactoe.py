from tkinter import *

root = Tk()
root.geometry('275x275')
root.resizable(False, False)

winner = Label(root, font = 'Comic_Sans_MS 14', text = '', fg = 'blue')

class Cell(Button):
    @property
    def clicked(self):
        return self['text'] in 'XO'


def check_cells(cell1, cell2, cell3):
    if (cell1['text'] == cell2['text'] and cell1['text'] == cell3['text']):
        if not (cell1['text'] == '_' and cell2['text'] == '_' and cell3['text'] == '_'):
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

def onclick(index):
    global BUTTONS, CURRENT_MOVE
    if not (BUTTONS[index].clicked):
        BUTTONS[index]['text'] = CURRENT_MOVE
        if (checkwin()):
            for i in BUTTONS:
                i['text'] = CURRENT_MOVE
                i['command'] = None
                winner['text'] = f'Winner: {CURRENT_MOVE}!'
        CURRENT_MOVE = 'O' if CURRENT_MOVE == 'X' else 'X'


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


CURRENT_MOVE = 'X' # O
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
root.mainloop()
