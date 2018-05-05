from tkinter.constants import OUTSIDE
from tkinter import messagebox
import tkinter

top = tkinter.Tk()
top.title('Place')

def helloCallBack():
    messagebox.showinfo('Hello python','Hello word')

B = tkinter.Button(top, text = 'Hello', command = helloCallBack, bg = 'yellow')
B.pack()
B.place(bordermode = OUTSIDE, height = 100, width = 100, x = 10, y = 10)
top.mainloop()
