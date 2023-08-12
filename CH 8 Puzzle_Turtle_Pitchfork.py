# Create a pitchfork facing to the right using four Turtle objects.

import turtle
turtle_one = turtle.Turtle()
turtle_two = turtle.Turtle()
turtle_three = turtle.Turtle()
turtle_four = turtle.Turtle()

turtle_one.forward(100)
turtle_one.left(90)
turtle_one.forward(50)
turtle_one.right(90)
turtle_one.forward(50)

turtle_two.forward(100)
turtle_two.right(90)
turtle_two.forward(50)
turtle_two.left(90)
turtle_two.forward(50)

turtle_three.forward(115)
turtle_three.right(90)
turtle_three.forward(20)
turtle_three.left(90)
turtle_three.forward(20)

turtle_four.forward(115)
turtle_four.left(90)
turtle_four.forward(20)
turtle_four.right(90)
turtle_four.forward(20)




turtle.done()