import tkinter
from tkinter.constants import LEFT, END
from tkinter import messagebox

root = tkinter.Tk()
root.title('Ten cua ban la gi?')

L1 = tkinter.Label(root, text='Ho vao ten:')
L1.pack(side = LEFT)

E1 = tkinter.Entry(root, bd = 1)
E1.pack(side = LEFT)
E1.insert(END, 'Nhap ten o day')

def message_welcom():
    name = 'Xin chao ' + E1.get()
    messagebox.showinfo('Xin chao', name)

#them nut button voi message
button = tkinter.Button(root, text='Xin chao', command=message_welcom)
button.pack(side = LEFT)

root.mainloop()