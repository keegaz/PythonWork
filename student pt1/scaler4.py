from tkinter import *

root = Tk()
root.config (bg="green")
minutes = Label(root, text="Minutes:")
minutes.pack(side=RIGHT)

scale = Scale(root, from_=1, to=45, orient=HORIZONTAL, length=300)
scale.pack()

button = Button(root, text="Start timing", command=quit)
button.pack()

root.mainloop()
