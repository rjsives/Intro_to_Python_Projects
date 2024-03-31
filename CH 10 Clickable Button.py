from tkinter import *


def hello():
    print('hello there')


def goodbye():
    print("goodbye then")


tk = Tk()
btn = Button(tk, text='click me', command=hello)
btn.pack()
btn2 = Button(tk, text='click me', command=goodbye)
btn2.pack()
tk.mainloop()
"""
The lesson I am working on suggested to use lines 1-4.  However, in Pycharm, I did not get the expected results.
With minimal research, I learned that the mainloop method was needed as a listener and handler for all methods and
without it, the code would run without any runtime errors, but the display would not be activated.
"""
