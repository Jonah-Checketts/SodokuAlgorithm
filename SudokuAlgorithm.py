#import tkinter to your file
from tkinter import *

#main window
root = Tk()

#creating the canvas
Canvas = Canvas(root, width = 500, height = 500)

#main vertical lines for the board
Canvas.create_line(2,0,2,500)
Canvas.create_line(166,0,166,500)
Canvas.create_line(333,0,333,500)
Canvas.create_line(500,0,500,500)


#horizontal lines for the board
Canvas.create_line(0,2,500,2)
Canvas.create_line(0,166,500,166)
Canvas.create_line(0,333,500,333)
Canvas.create_line(0,500,500,500)

#putting the canvas on the main window
Canvas.pack()

#main loop
root.mainloop()
