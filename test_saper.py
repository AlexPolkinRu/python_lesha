import random

bombfield = []
for row in range(0, 10):
    rowlist = []
    for column in range(0, 10):
        if random.randint(0, 100) < 20:
            rowlist.append(1)
        else:
            rowlist.append(0)
    bombfield.append(rowlist)

for rowlist in bombfield:
    print(rowlist)