import tkinter as tk
gui=tk.Tk()
gui.title('calculator')
gui.geometry('400x400')
l1=tk.Label(gui,text='ans')
l1.grid(column=0,row=0)

def abc():
    a=e1.get()
    l1.configure(text=a)
    b=e2.get()
    l1.configure(text=b)
    result=int(a)+int(b)
    l1.configure(text=result)

def abd():
    a=e1.get()
    l1.configure(text=a)
    b=e2.get()
    l1.configure(text=b)
    result=int(a)-int(b)
    l1.configure(text=result)


def abe():
    a=e1.get()
    l1.configure(text=a)
    b=e2.get()
    l1.configure(text=b)
    result=int(a)*int(b)
    l1.configure(text=result)


def abf():
    a=e1.get()
    l1.configure(text=a)
    b=e2.get()
    l1.configure(text=b)
    result=int(a)/int(b)
    l1.configure(text=result)

    
b1=tk.Button(gui,text='+',command=abc,bg='red',activebackground='yellow')
b1.grid(column=5,row=10)

b2=tk.Button(gui,text='-',command=abd,bg='blue',activebackground='purple')
b2.grid(column=6,row=10)

b3=tk.Button(gui,text='*',command=abe,bg='green',activebackground='brown')
b3.grid(column=7,row=10)

b4=tk.Button(gui,text='/',command=abf,bg='pink',activebackground='orange')
b4.grid(column=8,row=10)

e1=tk.Entry(gui)
e1.grid(column=2,row=2)

e2=tk.Entry(gui)
e2.grid(column=3,row=3)



