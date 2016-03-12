# Lazy Buttons
# Demonstrates creating buttons


from tkinter import *
import tkinter.messagebox as tkMessageBox

def show_alert() :
    tkMessageBox.showinfo("Important Warning","I told you not to click me!")
    root.config (bg="green")
    #quit()
    
# create a root window
root = Tk()
root.title("Rude Buttons")
root.geometry("300x485")



# create a button in the frame
bttn1 = Button(root, text = "Don't click me!",  command=show_alert)
bttn1.grid()


# kick off the root window's event loop
root.mainloop()
