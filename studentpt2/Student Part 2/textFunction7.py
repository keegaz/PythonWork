from tkinter import *       
from random import *        #This library allows us to generate random numbers
                            


def one_to_ten():
    ran = "I am angry,"
    ran = ran + "\nI am ill"
    ran = ran + "\nI am as ugly as sin"
    print (ran)

    
window = Tk()     

stacy = Button(window, text = 'yoyo', command = one_to_ten)  


stacy.pack()    
window.mainloop() 
