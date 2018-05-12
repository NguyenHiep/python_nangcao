import tkinter.messagebox
from tkinter import *
from tkinter import ttk

def tvSelect(event):
    curItem = tree.focus()
    print(tree.item(curItem))
    tkinter.messagebox.showinfo('Ban vua chon', tree.item(curItem)['values'][0])

root = Tk()
root.title('TreeView')

tree = ttk.Treeview(root)
tree['columns'] = ('one', 'two', 'three')
tree.column('one', stretch = 'yes')
tree.column('two', width = 50)
tree.column('three', width = 50)
tree.heading('one',text = 'Ten san pham')
tree.heading('two',text = 'Don gia')
tree.heading('three',text = 'So luong')

#logo = tkinter.PhotoImage

tree.insert('',0, text = '1', values = ('Xa bong', 20000,200))
tree.insert('',1, text = '2', values = ('Xa bong 2', 30000,100))
tree.insert('',2, text = '3', values = ('Xa bong 3', 40000,400))
tree.insert('',3, text = '4', values = ('Xa bong 4', 50000,300))
tree.insert('',4, 'dir4', text = '5', values = ('Xa bong 5', 60000,400))
tree.insert('dir4',5, text = '5.1', values = ('Xa bong 5.1', 70000,400))
tree.insert('dir4',6, text = '5.2', values = ('Xa bong 5.2', 75000,300))
tree.pack()

tree.bind('<<TreeviewSelect>>', tvSelect)

root.mainloop()