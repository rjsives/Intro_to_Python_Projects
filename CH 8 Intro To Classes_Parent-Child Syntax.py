#Classes are defined by using the class keyword followed by the name. The pass statement lets Python know we are not giving any more information.
class Thing:
  pass
#If a class is part of another class, it's considered a child of that class and the other class is the parent. These classes below are child classes to the class Thing.
class Inanimate(Thing):
  pass
class Animate(Thing):
  pass
#Similarly, the class below will be a child class of the class Inanimate
class Sidewalk(Inanimate):
  pass
#We can organize the Animal, Mammal, and Giraffe classes under Animate (which is a child of Thing)
class Animal(Animate):
  pass
class Mammal(Animal):
  pass
class Giraffe(Mammal):
  pass
#Classes are used to create specific objects (aka instances). Here's how to create a specific instance of giraffe (this introduces us to Reginald - a specific giraffe)
reginald = Giraffe()
#Right now reginald doesn't do anything. Alas, he is pretty useless since we used the pass keyword only after declaring each class. It's time to start adding functions to these classes. Here we add functions to each class. When declaring each function, we use "self" as the argument. Each function should apply to the highest level of class that can handle that activity. Every class that falls in a generation below that class can use dot notation to call a function from a higher class (parent, grandparent, or higher).
class Thing:
  def exists(self):
    print(f'I am a thing that exists.')
  pass
class Animate(Thing):
  def is_animate(self):
    print("I have a life.")
  pass
class Animal(Animate):
  def breathes(self):
    print("I breathe in some manner.")
  def moves(self):
    print("I am mobile.")
  def eats(self):
    print("I eat.")
  pass
class Mammal(Animal):
  def feeds_young_with_milk(self):
    print("I feed my young with milk.")
  pass
class Giraffe(Mammal):
    def __init__(self):
      print("I am a giraffe.")
    def has_long_neck(self):
      print("I am known for my long neck.")
#Here we will declare two new objects of the type Giraffe.
sammy = Giraffe()
harriette = Giraffe()
#Here we will call various functions for each Giraffe.
sammy.exists()
harriette.exists()
sammy.is_animate()
harriette.breathes()
harriette.moves()
harriette.eats()
sammy.feeds_young_with_milk()
sammy.has_long_neck()
#Functions Calling other Functions (multitasking) to have a function in the Giraffe class call the move function we would use the self parameter. (It refers to this specific object that is being created).
class Giraffe(Mammal):
#Here we create an initial function to set some behaviors each time we create a new giraffe using the __init__ keyword.
    def __init__(self, name, spots):
      self.giraffe_name = print(f'My name is {name}.')
      print("I am an even cooler giraffe.")
      self.giraffe_spots = print(f'I have {spots} spots.')
#Here we create a function that includes two inherited functions.
    def finds_food(self):
      self.moves()
      print('I\'ve found food!')
      self.eats()
#When create a Giraffe, we now have to supply parameters for name and number of spots.
tiffany = Giraffe("Tiffany", 306)
tiffany.finds_food()
jeremy = Giraffe("Jeremy (the tallest of them all)", 489)