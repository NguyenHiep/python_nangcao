import tkinter
from tkinter.constants import RAISED
from tkinter import messagebox

def message_welcom():
    messagebox.showinfo('welcome', 'Chao mung ban den voi ung dung quan ly vat tu')

def message_errors():
    messagebox.showerror('errors', 'Thong bao loi')

def message_warning():
    messagebox.showwarning('warning', 'Canh bao')

top = tkinter.Tk()
top.title(' Ung dung quan ly vat tu')
top.geometry('500x500')
top.resizable(0,0)
#them nut button
button = tkinter.Button(top, text='Hello', width=20)
button.pack()
#them label
label = tkinter.Label(top, text='Ho va ten khach hang', width=20)
label.pack()
# them label hinh anh
logo = tkinter.PhotoImage(file='img/welcome.png')
label_img = tkinter.Label(top, image=logo)
label_img.pack()

#them nut button voi message
button = tkinter.Button(top, text='Click show message', width=20, command=message_welcom)
button.pack()


top.mainloop()