from tkinter import *

expression = ''

def press(num): 

    global expression 
  
    expression = expression + str(num)
    equation.set(expression) 
  
def equalpress(): 

    try: 
        global expression 

        total = str(eval(expression)) 
        equation.set(total) 

        expression = '' 

    except: 
        equation.set(' error ') 
        expression = '' 
  
def clear():
    
    global expression 
    expression = '' 
    equation.set('0')

root = Tk()

root.geometry('355x475')
  
root.configure(bg='#ccccff')
  
root.title('Calculator') 

root.iconbitmap('c.ico')

root.resizable(False,False)
  
button_frame = Frame(root,bg='#ccccff')
button_frame.pack()

equation = StringVar()
equation.set('0')
    
expression_field = Entry(button_frame,textvariable=equation,justify='right',
                                 font = ('arial',20,'bold'))
    
button1 = Button(button_frame,font= ('times new roman',12),text=' 1 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(1), height=3, width=8) 
 
button2 = Button(button_frame,font= ('times new roman',12),text=' 2 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(2), height=3, width=8) 
  
button3 = Button(button_frame,font= ('times new roman',12),text=' 3 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(3), height=3, width=8) 

plus = Button(button_frame,font= ('times new roman',12),text=' + ',bd=1,relief='ridge',
              fg='black', bg='#e6ecff',command=lambda: press("+"), height=3, width=8) 
  
button4 = Button(button_frame,font= ('times new roman',12),text=' 4 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(4), height=3, width=8) 

button5 = Button(button_frame,font= ('times new roman',12),text=' 5 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(5), height=3, width=8) 
  
button6 = Button(button_frame,font= ('times new roman',12),text=' 6 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(6), height=3, width=8) 

minus = Button(button_frame,font= ('times new roman',12),text=' - ',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command=lambda: press("-"), height=3, width=8) 
  
button7 = Button(button_frame,font= ('times new roman',12),text=' 7 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(7), height=3, width=8) 
  
button8 = Button(button_frame,font= ('times new roman',12),text=' 8 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(8), height=3, width=8) 
  
button9 = Button(button_frame,font= ('times new roman',12),text=' 9 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(9), height=3, width=8) 

multiply = Button(button_frame,font= ('times new roman',12),text=' * ',bd=1,relief='ridge',
                  fg='black', bg='#e6ecff',command=lambda: press("*"), height=3, width=8) 
  
button0 = Button(button_frame,font= ('times new roman',12),text=' 0 ',bd=1,relief='ridge',
                 fg='black', bg='#e6ecff',command=lambda: press(0), height=3, width=8) 

decimal= Button(button_frame,font= ('times new roman',12),text='.',bd=1,relief='ridge',
                fg='black', bg='#e6ecff',command=lambda: press('.'), height=3, width=8) 

clear = Button(button_frame,font= ('times new roman',12),text='C',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command=clear, height=3, width=8) 
  
divide = Button(button_frame,font= ('times new roman',12),text=' / ',bd=1,relief='ridge',
                fg='black', bg='#e6ecff',command=lambda: press("/"), height=3, width=8) 

equal = Button(button_frame,font= ('times new roman',12),text=' = ',bd=1,relief='ridge',
               fg='black', bg='#e6ecff',command=equalpress,height=3) 

expression_field.grid(row=0,column=0,ipadx=8,columnspan = 4,ipady=25,pady=15)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
plus.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
minus.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)

button0.grid(row=4, column=0)
decimal.grid(row=4, column=1)
clear.grid(row=4, column=2)
divide.grid(row=4, column=3)

equal.grid(row=5, column=0,columnspan = 4,sticky='nsew')

root.mainloop() 
