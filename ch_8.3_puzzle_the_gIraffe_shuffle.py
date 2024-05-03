# Add functions to the Giraffe Class to move the giraffe's left and right feet forward and backward.
# Then create a function called dance and teach our giraffes ot dance (the function will call the four-foot functions).
# The result of calling the dance function will be a simple dance.

class Thing:
    @staticmethod
    def exists():
        print(f'I am a thing that exists.')

    pass


class Animate(Thing):
    @staticmethod
    def is_animate():
        print("I have a life.")

    pass


class Animal(Animate):
    @staticmethod
    def breathes():
        print("I breathe in some manner.")

    @staticmethod
    def moves(self):
        print("I am mobile.")

    @staticmethod
    def eats(self):
        print("I eat.")

    pass


class Mammal(Animal):
    @staticmethod
    def feeds_young_with_milk(self):
        print("I feed my young with milk.")

    pass


class Giraffe(Mammal):
    # Here we create an initial function to set some behaviors each time we
    # create a new giraffe using the __init__ keyword.
    def __init__(self, name, spots):
        self.giraffe_name = print(f'My name is {name}.')
        print("I am a giraffe.")
        self.giraffe_spots = print(f'I have {spots} spots.')

    # Here we create a function that includes two inherited functions.
    def finds_food(self):
        self.moves()
        print('I\'ve found food!')
        self.eats()

    @staticmethod
    def left_foot_forward(self):
        print("left foot forward")

    @staticmethod
    def right_foot_forward(self):
        print("right foot forward")

    @staticmethod
    def left_foot_backward(self):
        print("left foot back")

    @staticmethod
    def right_foot_backward(self):
        print("right foot back")

    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()


pass
# When create a Giraffe, we now have to supply parameters for name and number of spots.
reginald = Giraffe("Reginald", 112)
tiffany = Giraffe("Tiffany", 306)
jeremy = Giraffe("Jeremy (the tallest of them all)", 489)
tiffany.dance()
