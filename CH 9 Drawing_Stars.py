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
t.pencolor("blue")
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


t.reset
t.speed(9)
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
t2.pencolor("dark grey")

#adding an if statement based on the condition of the iterator x being even or odd
for x in range(1, 19):
    t2.forward(50)
    if x % 2 == 0:
        t2.left(175)
    else:
        t2.left(225)

turtle.done()