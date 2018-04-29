import tkinter
from tkinter.constants import MULTIPLE, END
from tkinter import messagebox

root = tkinter.Tk()
root.title('Chon khoa hoc')

var = tkinter.IntVar()
Lb1 = tkinter.Listbox(root, selectmode = MULTIPLE)
Lb1.insert(END, 'Python')
Lb1.insert(END, 'Perl')
Lb1.insert(END, 'PHP')
Lb1.insert(END, 'Java')
Lb1.insert(END, 'C')
Lb1.insert(END, 'Ruby')
Lb1.pack()
def getSelectedItems():
    tuple_item = Lb1.curselection()
    str1 = ''
    for item in tuple_item:
        str1 += Lb1.get(item) + ';'
    messagebox.showinfo('Cac khoa hoc ban chon', str1)

button = tkinter.Button(root, text='Hien thi', command = getSelectedItems)
button.pack()

root.mainloop()