# Simple GUI
# Demonstrates creating a window

from tkinter import *

# create the root window
root = Tk()

root.title("Python is such fun!!!!")

#first two parameters are width and height
#the last two are position of screen
root.geometry("250x150+300+300")

# kick off the window's event loop
root.mainloop()
