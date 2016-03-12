from tkinter import *       
from random import *        #This library allows us to generate random numbers
                            


def one_to_ten():
    ran = uniform(1,10) # creates a random decimal between the two numbers
    print (ran)

    
window = Tk()     

stacy = Button(window, text = 'yoyo', command = one_to_ten)  


stacy.pack()    
window.mainloop() 
