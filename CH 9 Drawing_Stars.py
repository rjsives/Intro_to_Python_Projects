import turtle

t = turtle.Turtle()
t.speed(7)
for x in range(1, 9):
    t.forward(100)
    t.left(225)

t.left(180)
t.penup()
t.forward(150)
t.pendown()
t.pencolor("blue")
t.speed(0)


for x in range(1, 39):
    t.forward(100)
    t.left(175)

t.penup()
t.forward(150)
t.left(90)
t.forward(100)
t.pendown()
t.pencolor("green")
t.speed(0)

for x in range(1, 20):
    t.forward(100)
    t.left(95)


t.reset
t.speed(5)
t.penup()
t.forward(50)
t.right(90)
t.forward(150)
t.pendown()
t.pencolor("red")

for x in range(1, 150):
    t.forward(100)
    t.left(115)

turtle.done()