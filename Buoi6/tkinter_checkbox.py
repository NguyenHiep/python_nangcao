import tkinter
from tkinter.constants import LEFT
from tkinter import messagebox

top = tkinter.Tk()
top.title('Check button')

Checkvar1 = tkinter.IntVar()
Checkvar2 = tkinter.IntVar()
Checkvar3 = tkinter.IntVar()
Checkvar4 = tkinter.IntVar()

var1 = tkinter.StringVar()
var2 = tkinter.StringVar()
var3 = tkinter.StringVar()
var4 = tkinter.StringVar()

var1.set('Java')
var2.set('PHP')
var3.set('Python')
var4.set('C/C++')

C1 = tkinter.Checkbutton(top, text = var1.get(), variable = Checkvar1, onvalue = 1, offvalue = 0, height = 1, width = 10 )
C2 = tkinter.Checkbutton(top, text = var2.get(), variable = Checkvar2, onvalue = 1, offvalue = 0, height = 1, width = 10 )
C3 = tkinter.Checkbutton(top, text = var3.get(), variable = Checkvar3, onvalue = 1, offvalue = 0, height = 1, width = 10 )
C4 = tkinter.Checkbutton(top, text = var4.get(), variable = Checkvar4, onvalue = 1, offvalue = 0, height = 1, width = 10 )

C1.pack(side = LEFT)
C2.pack(side = LEFT)
C3.pack(side = LEFT)
C4.pack(side = LEFT)

def getSelectedItems():
    str1 = ''
    if Checkvar1.get() == 1:
        str1 += var1.get() + ';'
    if Checkvar2.get() == 1:
        str1 += var2.get() + ';'
    if Checkvar3.get() == 1:
        str1 += var3.get() + ';'
    if Checkvar4.get() == 1:
        str1 += var4.get() + ';'

    messagebox.showinfo('Mon ban chon', str1)

B = tkinter.Button(top, text = 'Ket qua', command = getSelectedItems)
B.pack()
top.mainloop()