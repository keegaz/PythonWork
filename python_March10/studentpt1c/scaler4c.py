from tkinter import *

root = Tk()
root.title("Everything to scale!")
root.geometry("750x700")
root.config (bg="green")
#minutes = Label(root, text="Minutes:")
#minutes.pack(side=RIGHT)

seconds =Label(root, text="seconds: ")
seconds.pack(side=LEFT)

scale = Scale(root, from_=1, to=45, orient=VERTICAL, length=300)
scale.pack()

button = Button(root, text="Quit Me!", command=quit)
button.pack()

root.mainloop()
