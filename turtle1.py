from turtle import *
colors = ['red', 'blue', 'pink', 'green', 'orange', 'yellow', 'dark blue', 'purple']
shape("turtle")
pensize(4)
speed(10)
while True:
    for x in colors:
        backward(5)
        color(x)
        right(330)