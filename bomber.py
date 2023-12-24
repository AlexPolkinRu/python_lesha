import random

bombfield = []

def aaa(bombfield):
    global SquaresToClear
    for row in range(0, 10):
        rowlist = []
        for column in range(0, 10):
            if random.randint(0, 100) < 20:
                rowlist.append(1)
            else:
                rowlist.append(0)
                # SquaresToClear = SquaresToClear + 1

        bombfield.append(rowlist)
        print(rowlist)

aaa(bombfield)

# print(bombfield)
