# Drawing A Car
import turtle

t = turtle.Turtle()
# basic red car shape
t.reset()
t.color(1, 0, 0)
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
# first wheel
t.color(0, 0, 0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
# second wheel
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.circle(10)
t.end_fill()
# Demostrate creating a filled yellow circle
# sets the position
t2 = turtle.Turtle()
t2.up()
t2.right(90)
t2.forward(50)
# sets the color and draws the circle
t2.color(1, 1, 0)
t2.begin_fill()
t2.circle(20)
t2.end_fill()
# Create a function to draw a filled circle
t3 = turtle.Turtle()
t3.up()
t3.left(90)
t3.forward(100)
t3.down()


def myCircle(red, green, blue, size):
    t3.color(red, green, blue)
    t3.begin_fill()
    t3.circle(size)
    t3.end_fill()


# Draw a large gold circle using the function
myCircle(0.9, 0.75, 0, 50)
# Draw medium light pink circle
myCircle(1, .7, .75, 30)
# Draw small orange circle
myCircle(1, .5, 0, 15)
# Draw tiny light taupe circle
myCircle(.9, .5, .15, 7)
# Experiment with mixing your own colors
t3.up()
t3.right(90)
t3.forward(100)
t3.down()

myCircle(0.5, 0.5, 0, 50)
myCircle(0.5, 0.5, 0.75, 30)
myCircle(0, 0.75, .5, 15)
myCircle(0, 0, 0.9, 7)

# create a square drawing function
t4 = turtle.Turtle()


def mysquare(red, green, blue, size):
    t4.color(red, green, blue)
    t4.begin_fill()
    for x in range(1, 5):
        t4.forward(size)
        t4.left(90)
    t4.end_fill()


mysquare(0, 0, 0, 50)


# create a function with a parameter giving the option to have a filled or not filled square
t5 = turtle.Turtle()

def dynamicsquare(red, green, blue, size, filled):
    t5.color(red, green, blue)
    if filled == "True":
        t5.begin_fill()
        for x in range(1, 5):
            t5.forward(size)
            t5.left(90)
        t5.end_fill()
    else:
        for x in range(1, 5):
            t5.forward(size)
            t5.left(90)


dynamicsquare(1, .2, .4, 40, "True")
dynamicsquare(.5, .3, .2, 20, "False")
dynamicsquare(0, 0, 0, 10, "False")

turtle.done()
