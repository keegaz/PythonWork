from tkinter import *


def Call():
        myText = ""
        for x in range(1, 11):
                myText = myText + str(x) + " times 10 is : " + str(x*10) +"\n"
        lab= Label(root, text = myText)
        lab.pack()
        button['bg'] = 'blue'
        button['fg'] = 'white'

root = Tk()
root.geometry('100x110+350+70')
button = Button(root, text = 'Press me', command = Call)
button.pack()

root.mainloop()
