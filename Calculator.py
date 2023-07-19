#SIMPLE CALCULATOR

from tkinter import *
expression=''   #Empty String

#GUI
gui=Tk()
gui.configure(bg='pink')    #Background color
gui.title('Calculator') #GUI window title
gui.geometry('265x125') #265x125

#Numbers
def press(num):
    global expression   #Expression is global
    expression=expression+str(num)  #Displays as a string
    equation.set(expression)    #Prints the entire expression

#Equal 
def equalpress():
    try:
        global expression  #Equation is stored in expression so make it global 
        total=str(eval(expression))  #Evaluates the expression in string format
        equation.set(total) #Finds the answer and prints it
        expression=''   #Back to normal
    except:
        equation.set('Error')   #If equation not valid, it will display an error
        expression=''   #Back to normal

#Clear
def clear():
    global expression
    equation.set('')
    expression=''

#Entry Box
equation=StringVar()   #Stores the numbers that are entered in the variable that is in string format
e1=Entry(gui,textvariable=equation)
e1.grid(columnspan=5,ipadx=55) #Covers 4 columns with columnspan
                                    #The padding helps put the entrybox together
equation.set('Enter the equation')  #Displays a message on the entrybox

#Buttons
b1=Button(gui,text='1',fg='black',bg='white',height=1,width=7,command=lambda:press(1))
b1.grid(row=2,column=1)

b2=Button(gui,text='2',fg='black',bg='white',height=1,width=7,command=lambda:press(2))
b2.grid(row=2,column=2)

b3=Button(gui,text='3',fg='black',bg='white',height=1,width=7,command=lambda:press(3))
b3.grid(row=2,column=3)

b4=Button(gui,text='4',fg='black',bg='white',height=1,width=7,command=lambda:press(4))
b4.grid(row=3,column=1)

b5=Button(gui,text='5',fg='black',bg='white',height=1,width=7,command=lambda:press(5))
b5.grid(row=3,column=2)

b6=Button(gui,text='6',fg='black',bg='white',height=1,width=7,command=lambda:press(6))
b6.grid(row=3,column=3)

b7=Button(gui,text='7',fg='black',bg='white',height=1,width=7,command=lambda:press(7))
b7.grid(row=4,column=1)

b8=Button(gui,text='8',fg='black',bg='white',height=1,width=7,command=lambda:press(8))
b8.grid(row=4,column=2)

b9=Button(gui,text='9',fg='black',bg='white',height=1,width=7,command=lambda:press(9))
b9.grid(row=4,column=3)

b0=Button(gui,text='0',fg='black',bg='white',height=1,width=7,command=lambda:press(0))
b0.grid(row=5,column=1)

b10=Button(gui,text='clear',fg='black',bg='white',height=1,width=7,command=lambda:clear())
b10.grid(row=5,column=2)

b11=Button(gui,text='=',fg='black',bg='white',height=1,width=7,command=lambda:equalpress())
b11.grid(row=5,column=3)

b12=Button(gui,text='+',fg='black',bg='white',height=1,width=7,command=lambda:press('+'))
b12.grid(row=2,column=4)

b13=Button(gui,text='-',fg='black',bg='white',height=1,width=7,command=lambda:press('-'))
b13.grid(row=3,column=4)

b14=Button(gui,text='*',fg='black',bg='white',height=1,width=7,command=lambda:press('*'))
b14.grid(row=4,column=4)

b15=Button(gui,text='/',fg='black',bg='white',height=1,width=7,command=lambda:press('/'))
b15.grid(row=5,column=4)
