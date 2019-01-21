# python-simple-calculator
simple calculator
import tkinter as tkn
gui=tk.Tk()
gui.title('calculator')
gui.geometry('400x400')
l1=tk.Label(gui,text='ans')
l1.grid(column=0,row=0)

def abc():
    a=e1.get()
    b=e2.get()
    l1=int(a)+int(b)
    l1.configure(text='ans')
        
b1=tk.Button(gui,text='+',command=abc)
b1.grid(column=5,row=10)

b2=tk.Button(gui,text='-',command=abc)
b2.grid(column=6,row=10)
b3=tk.Button(gui,text='*',command=abc)
b3.grid(column=7,row=10)
b4=tk.Button(gui,text='/',command=abc)
b4.grid(column=8,row=10)

e1=tk.Entry(gui)
e1.grid(column=2,row=2)

e2=tk.Entry(gui)
e2.grid(column=3,row=3)



