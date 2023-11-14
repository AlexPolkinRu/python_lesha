from random import choice
wawe = ['rocet', 'planet','mister', 'alien']
print(wawe[0])
print(wawe[3])
wawe[0] = 'not rocet'
print(wawe)
del wawe[0]
wawe.append('moon')
for a in wawe:
    print(a)
print(choice(wawe))