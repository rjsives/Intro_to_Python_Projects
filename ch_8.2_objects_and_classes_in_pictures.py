import turtle

# When we use turtle.Turtle(), Python creates an object of the Turtle class that is provided by the turtle module.
# We can create two Turtle objects (named Avery and Kate).
avery = turtle.Turtle()
kate = turtle.Turtle()
# Each turtle object (avery and kate) is a member of the Turtle class.
# Having created our Turtle objects, we can call functions on each, and they will draw independently.
avery.forward(50)
avery.right(90)
avery.forward(20)

kate.pencolor("red")
kate.left(90)
kate.penup()
kate.forward(5)
kate.pendown()
kate.forward(60)


jacob = turtle.Turtle()
jacob.pencolor("turquoise")
jacob.left(180)
jacob.penup()
jacob.forward(5)
jacob.pendown()
jacob.forward(27)

# Here we can demonstrate the three objects operate independently
avery.right(90)
jacob.right(90)
kate.right(97)
avery.forward(12)
avery.right(90)
avery.forward(15)
kate.forward(78)
jacob.forward(46)
jacob.left(46)
jacob.forward(35)

turtle.done()
