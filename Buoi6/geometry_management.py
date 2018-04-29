import tkinter

root =  tkinter.Tk()
root.title('Grid')
color = ('red', 'green', 'blue', 'white', 'yellow')

for r in range(3):
    for c in range(3):
        tkinter.Label(root, text = 'Dong %s/ Cot %s'%(r,c), 
        borderwidth = 1, bg = color[(r+c) - 1]).grid(row = r, column = c)

root.mainloop()