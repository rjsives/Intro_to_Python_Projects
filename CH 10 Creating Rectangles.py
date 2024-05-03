from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=500, height=500)
canvas.pack()
"""The create line method takes four parameters. The top left corner has coordinates (0,0) 
the bottom right corner has the coordinates (500,500) on the specified canvas"""
canvas.create_line(500,500,0,0)
"""The first two parameters in the create_rectangle() method define the coordiates of first corner of the rectange (10,10) for example
and the second two name the coordinates of the opposite corner(50,50). """

canvas.create_rectangle(10,10,50,50)
canvas.create_rectangle(50,50,90,90)
canvas.create_rectangle(90,90,300,130)
canvas.create_rectangle(300,130,340,340)
tk.mainloop()
