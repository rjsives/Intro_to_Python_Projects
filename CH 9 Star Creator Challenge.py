import turtle

t1 = turtle.Turtle()
t1.up()
t1.left(180)
t1.forward(300)
t1.down()


def star_maker(size, points):
    double_points = points * 2
    angle1 = 180 - (360/points)
    angle2 = angle1 * 3

    for x in range(0, double_points):
        t1.forward(size)
        if x % 2 == 0:
            t1.left(angle1)
        else:
            t1.left(angle2)

star_maker(50, 7)


def star_designer(size, points):
    angle = 360 / points
    for x in range(0, points):
        t1.forward(size)
        t1.left(180 - angle)
        t1.forward(size)
        t1.right(180 - (angle * 2))

t1.up()
t1.left(180)
t1.forward(300)
t1.down()

star_designer(50, 5)

t1.up()
t1.forward(300)
t1.down()


def double_star(size, points):
    star_maker(size, points)
    star_designer(size, points)

double_star(55, 31)

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
shape_maker(50, 10)





turtle.done()