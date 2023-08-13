import turtle

t = turtle.Turtle()
s = turtle.Turtle()
u = turtle.Turtle()

#turte.reset deletes this turtle's drawings and restores it's default values
t.reset()
for x in range(1,5):
    t.forward(50)
    t.left(90)

s.reset()
for x in range(1,5):
    s.forward(150)
    s.left(90)

u.reset()
for x in range(1, 5):
    u.forward(300)
    u.left(90)

#turtle.done()