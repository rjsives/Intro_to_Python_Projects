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
# Demonstrate creating a filled yellow circle
# set the position
t2 = turtle.Turtle()
t2.up()
t2.right(90)
t2.forward(50)
# set the color and draw the circle
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


def my_circle(red, green, blue, size):
    t3.color(red, green, blue)
    t3.begin_fill()
    t3.circle(size)
    t3.end_fill()


# Draw a large gold circle using the function
my_circle(0.9, 0.75, 0, 50)
# Draw medium light pink circle
my_circle(1, .7, .75, 30)
# Draw small orange circle
my_circle(1, .5, 0, 15)
# Draw tiny light taupe circle
my_circle(.9, .5, .15, 7)
# Experiment with mixing your own colors
t3.up()
t3.right(90)
t3.forward(100)
t3.down()

my_circle(0.5, 0.5, 0, 50)
my_circle(0.5, 0.5, 0.75, 30)
my_circle(0, 0.75, .5, 15)
my_circle(0, 0, 0.9, 7)

# create a square drawing function
t4 = turtle.Turtle()


def my_square(red, green, blue, size):
    t4.color(red, green, blue)
    t4.begin_fill()
    for x in range(1, 5):
        t4.forward(size)
        t4.left(90)
    t4.end_fill()


my_square(0, 0, 0, 50)

# create a function with a parameter giving the option to have a filled or not filled square
t5 = turtle.Turtle()


def dynamic_square(red, green, blue, size, filled):
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


dynamic_square(1, .2, .4, 40, "True")
dynamic_square(.5, .3, .2, 20, "False")
dynamic_square(0, 0, 0, 10, "False")

# make a function to draw an octagon with an outline
t6 = turtle.Turtle()


def octagon_maker(size, fill_color, outline_color):
    t6.color(fill_color)
    t6.begin_fill()
    for x in range(1, 9):
        t6.pensize(1)
        t6.forward(size)
        t6.right(45)
    t6.end_fill()
    for x in range(1, 9):
        t6.pensize(5)
        t6.color(outline_color)
        t6.forward(size)
        t6.right(45)
        t6.pensize(1)


t6.up()
t6.left(180)
t6.forward(80)
t6.left(90)
t6.forward(50)
t6.down()

octagon_maker(100, "red", "grey")
t6.up()
t6.forward(115)
t6.right(90)
t6.forward(95)
t6.down()
octagon_maker(50, "pink", "purple")

turtle.done()
