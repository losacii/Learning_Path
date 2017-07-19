from Tkinter import *

def tmp():
    root = Tk()

    root.mainloop()

def tk_grid_layout():
    root = Tk()

    lb1 = Label(root, text='Name')
    lb2 = Label(root, text='Password')
    entry1 = Entry(root)
    entry2 = Entry(root)

    root.mainloop()

def tk_Frames():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()

    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    btn1 = Button(topFrame, text="One", bg='green', fg='white')
    btn2 = Button(topFrame, text="Two", bg='blue', fg='white')
    btn3 = Button(topFrame, text="Three", bg='green', fg='white')
    btn4 = Button(bottomFrame, text="Four", bg='blue', fg='white')
    btn5 = Button(bottomFrame, text="Five", bg='green', fg='white')
    btn6 = Button(bottomFrame, text="Six", bg='blue', fg='white')

    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=LEFT)
    btn5.pack(side=BOTTOM)
    btn6.pack(side=BOTTOM)

    root.mainloop()

def tk_Labels():
    root = Tk()

    lb1 = Label(root, text="Hello World!", bg="green", fg='white')
    lb1.pack(fill=X)

    lb2 = Label(root, text="Welcome to Tkinter", bg="blue", fg='yellow')
    lb2.pack(fill=X)

    root.mainloop()
