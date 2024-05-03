# Here we will import the random module and then create a function that uses a random
# number for the coordinates (top left and lower right corners).


from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

"""Uses the randrange function provided by the random module. When we give this function
a number, it returns a random integer between 0 and the number given"""


def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(width)
    y2 = random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)


# Creates a different random rectangle each time you run
# random_rectangle(400, 400)

for x in range(0, 30):
    random_rectangle(400, 400)
    tk.mainloop()
