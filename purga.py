import random
from turtle import *
from random import randint


def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)


def snowflakeArm(size):
    for x in range(0, 4):
        forward(size)
        vshape(size)
    backward(size*4)


def snowflake(size):
    for x in range(0, 6):
        color(random.choice(colors))
        snowflakeArm(size)
        right(60)


hideturtle()
speed(10)
pensize(6)
Screen().bgcolor('turquoise')
colors = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]
for i in range(0,10):
    size = randint(5,30)
    x = randint(-400,400)
    y = randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)


while True:
    pass