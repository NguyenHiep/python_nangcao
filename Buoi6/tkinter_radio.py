import tkinter
from tkinter.constants import W
from tkinter import messagebox

root = tkinter.Tk()
root.title('Radio button')

var = tkinter.IntVar()
def sel():
    selection = 'Ban vua chon thuoc tinh ' + str(var.get())
    label.config(text = selection)

R1 = tkinter.Radiobutton(root, text = 'Option 1', variable = var, value = 1, command = sel)
R1.pack(anchor = W)

R2 = tkinter.Radiobutton(root, text = 'Option 2', variable = var, value = 2, command = sel)
R2.pack(anchor = W)

R3 = tkinter.Radiobutton(root, text = 'Option 3', variable = var, value = 3, command = sel)
R3.pack(anchor = W)

label = tkinter.Label(root)
label.pack()

root.mainloop()