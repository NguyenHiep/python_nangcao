from tkinter import *
from tkinter import messagebox

def bai1_1():
    messagebox.showinfo('Giải phương trình bậc nhất', 'Viết phương trình giải phương trình bậc bậc nhất')

top = Tk()

top.title('Hệ thống bài tập nâng cao PyThon')
top.geometry('600x300')
top.resizable(0,0)

menubar = Menu(top)
# Menu 1
chuong_1 = Menu(menubar, tearoff = 0)
chuong_1.add_command(label = '1.1', command = bai1_1)
chuong_1.add_command(label = '1.2')
chuong_1.add_command(label = '1.3')
chuong_1.add_command(label = '1.4')
chuong_1.add_command(label = '1.5')
chuong_1.add_command(label = '1.6')
chuong_1.add_command(label = '1.7')
chuong_1.add_command(label = '1.8')
chuong_1.add_command(label = '1.9')
chuong_1.add_separator()
chuong_1.add_command(label = 'Exit', command = top.quit)
menubar.add_cascade(label = 'Chương 1', menu = chuong_1)

# Menu 2
chuong_2 = Menu(menubar, tearoff = 0)
chuong_2.add_command(label = '2.1')
chuong_2.add_command(label = '2.2')
chuong_2.add_command(label = '2.3')
chuong_2.add_command(label = '2.4')
chuong_2.add_command(label = '2.5')
chuong_2.add_command(label = '2.6')
chuong_2.add_command(label = '2.7')
chuong_2.add_command(label = '2.8')
chuong_2.add_command(label = '2.9')
chuong_2.add_separator()
chuong_2.add_command(label = 'Exit', command = top.quit)
menubar.add_cascade(label = 'Chương 2', menu = chuong_2)


# Menu 3
chuong_3 = Menu(menubar, tearoff = 0)
chuong_3.add_command(label = '3.1')
chuong_3.add_command(label = '3.2')
chuong_3.add_command(label = '3.3')
chuong_3.add_command(label = '3.4')
chuong_3.add_command(label = '3.5')
chuong_3.add_command(label = '3.6')
chuong_3.add_command(label = '3.7')
chuong_3.add_command(label = '3.8')
chuong_3.add_command(label = '3.9')
chuong_3.add_separator()
chuong_3.add_command(label = 'Exit', command = top.quit)
menubar.add_cascade(label = 'Chương 3', menu = chuong_3)


# Menu 4
chuong_4 = Menu(menubar, tearoff = 0)
chuong_4.add_command(label = '4.1')
chuong_4.add_command(label = '4.2')
chuong_4.add_command(label = '4.3')
chuong_4.add_command(label = '4.4')
chuong_4.add_command(label = '4.5')
chuong_4.add_command(label = '4.6')
chuong_4.add_command(label = '4.7')
chuong_4.add_command(label = '4.8')
chuong_4.add_command(label = '4.9')
chuong_4.add_separator()
chuong_4.add_command(label = 'Exit', command = top.quit)
menubar.add_cascade(label = 'Chương 4', menu = chuong_4)


top.config(menu = menubar)
top.mainloop()