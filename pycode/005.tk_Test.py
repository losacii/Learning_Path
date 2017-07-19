from mod.tkMod import *
import os
os.system("clear")

#tk_Frames()
#tmp()
#tk_Labels()


root = Tk()

lframe = Frame(root)
lframe.pack(side=LEFT)

rframe = Frame(root)
rframe.pack(side=LEFT)

lb1 = Label(lframe, text='label_One', bg='green', fg='red')
lb1.pack(side=TOP)

lb2 = Label(lframe, text='label_Two', bg='blue', fg='white')
lb2.pack(side=TOP)

lb3 = Label(rframe, text='label_One', bg='green', fg='red')
lb3.pack(side=TOP)

lb4 = Label(rframe, text='label_Two', bg='blue', fg='white')
lb4.pack(side=TOP)



root.mainloop()

print "Quit!"

