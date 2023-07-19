#DIGITAL CLOCK

'''
1. import tkinter
2. object
3. grid
4. mainloop
'''

from tkinter import *
import time   #Import time module


#Create a funtion
def tick():
    output=time.strftime('%H:%M:%S')    #Output will take the time from your computer
    clock.config(text=output)
    clock.after(2,tick)   #Calls the function every 2 milliseconds



root=Tk()
root.title('Digital Clock')

clock=Label(root,text='hello',font=('calibri',120),bg='light blue',fg='white')

clock.grid(row=0,column=0)


tick()  #Call the function 


root.mainloop
