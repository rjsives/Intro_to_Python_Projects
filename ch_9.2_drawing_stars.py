import turtle

t = turtle.Turtle()
t2 = turtle.Turtle()
t.speed(7)
for x in range(1, 9):
    t.forward(100)
    t.left(225)

t.left(180)
t.penup()
t.forward(100)
t.left(90)
t.forward(20)
t.right(90)
t.pendown()
t.pencolor("dodgerblue")
t.speed(0)

for x in range(1, 39):
    t.forward(100)
    t.left(175)

t.penup()
t.forward(125)
t.left(90)
t.forward(100)
t.pendown()
t.pencolor("green")
t.speed(0)

for x in range(1, 20):
    t.forward(100)
    t.left(95)


t.speed(10)
t.penup()
t.forward(50)
t.right(90)
t.forward(150)
t.pendown()
t.pencolor("red")

for x in range(1, 73):
    t.forward(100)
    t.left(115)

t2.reset()
t2.speed(7)
t2.penup()
t2.forward(175)
t2.right(90)
t2.forward(20)
t2.left(90)
t2.pendown()
t2.pencolor("greenyellow")

# adding an if statement based on the condition of the iterator x being even or odd
for x in range(1, 19):
    t2.forward(50)
    if x % 2 == 0:
        t2.left(175)
    else:
        t2.left(225)

# Multicolored Spirograph design using rhombus
t2.up()
t2.right(90)
t2.forward(100)
t2.down()

for x in range(1, 81):
    t2.pencolor("orangered")
    t2.forward(10)
    t2.pencolor("green")
    t2.forward(30)
    t2.pencolor("orangered")
    t2.forward(10)
    if x % 2 == 0:
        t2.left(111)
    else:
        t2.pencolor("orangered")
        t2.forward(25)
        t2.pencolor("dodgerblue")
        t2.forward(10)
        t2.left(60)

# Creating a filled Star using a function
t3 = turtle.Turtle()
t3.up()
t3.right(90)
t3.forward(100)
t3.down()
t3.speed(0)


def my_star(size, color, filled):
    t3.color(color)
    if filled:
        t3.begin_fill()
    for y in range(1, 19):
        t3.forward(size)
        if y % 2 == 0:
            t3.left(175)
        else:
            t3.left(225)
    if filled:
        t3.end_fill()


my_star(200, "teal", True)
my_star(200, "red", False)
my_star(100, "black", True)
my_star(100, "red", False)
my_star(50, "yellow", True)
my_star(50, "red", False)
my_star(25, "blue", True)
my_star(25, "red", False)
my_star(12.5, "slategrey", True)
my_star(12.5, "red", False)

turtle.done()
