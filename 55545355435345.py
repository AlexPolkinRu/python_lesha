from random import randint
m = []
for y in range(5):
    a = randint(1, 3)
    if a == 1:
        m.append(1)
    elif a == 2:
        m.append(2)
    else:
        m.append(3)
print(m)