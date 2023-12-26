import tkinter
import random

game_over = False
score = 0
SquaresToClear = 0
bomb_field = []


def layout_window(window):
    for row_number, row_list in enumerate(bomb_field):
        for columnnumber, row_list in enumerate(bomb_field):
            if random.randint(0, 100) < 25:
                square = tkinter.Label(window, text="     ", bg="dark green")
            elif random.randint(1, 100) > 75:
                square = tkinter.Label(window, text="     ", bg="sea green")
            else:
                square = tkinter.Label(window, text="     ", bg="green")
            square.grid(row=row_number, column=columnnumber)


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


def play_bombdodger():
    create_bombfield(bomb_field)
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()


def print_bombfield(bombfield):
    print(bombfield)


play_bombdodger()


def print_field(bf):
    for rowList in bf:
        print(rowList)


print_field(bomb_field)
