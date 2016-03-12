# Simple GUI
# Demonstrates creating a window

from tkinter import *

# create the root window
root = Tk()

root.title("I love Python more than anything!!")

#first two parameters are width and height
#the last two are position of screen
root.geometry("750x400+300+300")

# kick off the window's event loop
root.mainloop()