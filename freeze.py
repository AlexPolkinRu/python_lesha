from turtle import *


def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)


def snowflakeArm():
    for x in range(0, 4):
        forward(30)
        vshape()
    backward(120)


def snowflake():
    for x in range(0, 19):
        snowflakeArm()
        right(20)


hideturtle()
speed(10)
pencolor('white')
pensize(6)
Screen().bgcolor('turquoise')
snowflake()

while True:
    pass