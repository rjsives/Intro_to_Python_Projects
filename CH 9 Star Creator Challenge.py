import time
import math
import turtle
from turtle import Turtle
pi = 3.1415926535897932

t1: Turtle = turtle.Turtle()
"""t1.up()
t1.left(180)
t1.forward(300)
t1.down()"""


def star_maker(size, points):
    double_points = points * 2
    angle1 = 180 - (360/double_points)
    angle2 = (angle1 * 3)
    for x in range(0, double_points):
        t1.speed(0)
        t1.forward(size)
        if x % 2 == 0:
            t1.left(angle1)
        else:
            t1.right(angle2)

# star_maker(50, 7)

def star_designer(size, points):
    angle = 360 / points
    for x in range(0, points):
        t1.speed(0)
        t1.forward(size)
        t1.left(180 - angle)
        t1.forward(size)
        t1.right(180 - (angle * 2))

def complicated_star(size, points):
    double_points = points * 2
    angle1 = 180 - (180/points)
    angle2 = (angle1*3)-360
    angle3 = 180/points
    angle4 = 180 - (180/points)*3


    for x in range(0, double_points):
        t1.speed(0)
        t1.forward(size)
        if points % 2 != 0:
            if x % 2 == 0:
                t1.left(angle1)
            else:
                t1.left(angle2)

        else:
            t1.speed(2)
            if x < points-1:
                if x % 2 == 0:
                    t1.left(angle1)
                else:
                    t1.left(angle2)
            elif x == points-1:

                t1.pencolor("green")
                t1.left(180)
                t1.forward(size)
                t1.right(angle1 + (180-angle1)/2)
                t1.forward((size*pi)/2)
                t1.right(angle1 + (180-angle1)/2)
                t1.forward(size)
                t1.left(180)
                time.sleep(2)
                #t1.right(angle1)
                #t1.forward(size*2)
                #t1.right(90)
                #t1.forward(size)
                #t1.right(90)
                #t1.forward(size)
                #t1.right(90)
                #t1.forward(size)
                #t1.right(angle1 + (180-angle1)/2)
                #t1.forward((size/points*2))
                #t1.right((180-angle1)*2)

                #t1.right(70)
                #t1.forward((size / points * 2))
                #t1.left(angle2*1.5)

                time.sleep(2)



            else:
                if x % 2 == 0:
                    t1.pencolor("red")
                    t1.left(angle1)
                else:
                    t1.left(angle2)






def ultra_complicated_star(size, points):
    double_points = points * 2
    angle1 = 180 - (360/points)
    angle2 = (angle1 * 3)
    for x in range(0, double_points):
        t1.speed(0)
        t1.forward(size)
        if x % 2 == 0:
            t1.left(angle1)
        else:
            t1.left(angle2)

def throwing_star(size, points):
    double_points = points * 2
    angle1 = 180 - (360 / points)
    angle2 = (angle1 * 3)
    for x in range(0, double_points):
        t1.speed(0)
        t1.forward(size)
        if x % 2 == 0:
            t1.left(angle1)
        else:
            t1.right(angle2)
            t1.forward(size)
"""t1.up()
t1.left(180)
t1.forward(300)
t1.down()

# star_designer(50, 5)

t1.up()
t1.forward(300)
t1.down()"""


def double_star(size, points):
    turtle.resetscreen()
    """t1.speed()
    star_maker(size, points)
    t1.left(180)
    t1.up()
    t1.forward(225)
    t1.down()
    star_designer(size, points)
    t1.left(180)
    t1.up()
    t1.forward(350)
    t1.down()"""
    complicated_star(size, points)
    """t1.up()
    t1.forward(130)
    t1.down()
    ultra_complicated_star(size, points)
    t1.up()
    t1.forward(150)
    t1.down()
    throwing_star(size, points)"""
    time.sleep(2)

def progressive_stars():
    for x in range (5, 19):
        double_star(300, x)

progressive_stars()
"""
def shape_maker(size, points):
    angle = 360/points
    for x in range(1, points + 1):
        t1.left(angle)
        t1.forward(size)

shape_maker(50, 3)
shape_maker(50, 4)
shape_maker(50, 5)
shape_maker(50, 6)
shape_maker(50, 7)
shape_maker(50, 8)
shape_maker(50, 9)
shape_maker(50, 10)"""





turtle.done()