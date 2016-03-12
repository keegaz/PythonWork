from tkinter import *

import tkinter.messagebox as tkMessageBox

def show_alert() :
    root.bell()
    tkMessageBox.showinfo("Ready!", "DING DING DING!")
   



root = Tk()


button = Button(root, text="Click Me", command=show_alert)
button.grid(row=10, column=10)

root.mainloop()
