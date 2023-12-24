import tkinter
import random

game_over = False
score = 0
SquaresToClear = 0


def layout_window(window):
    for row_number, row_list in enumerate(bombfield):
        if random.randint(0, 100) < 25:
            square = tkinter.Label(window, text="    ", bg="darkgreen")



def play_bombarger():
    create_bombfield(bombfield)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


bombfield = []


def create_bombfield(bombfield):
    global SquaresToClear
    for row in range(0, 10):
        rowlist = []
        for column in range(0, 10):
            if random.randint(0, 100) < 20:
                rowlist.append(1)
            else:
                rowlist.append(0)
                SquaresToClear = SquaresToClear + 1
        bombfield.append(rowlist)

def print_bombfield(bombfield):
    print(bombfield)

# play_bombarger()

create_bombfield(bombfield)
print(bombfield)