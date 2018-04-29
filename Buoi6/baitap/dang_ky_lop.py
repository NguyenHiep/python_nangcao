import tkinter
from tkinter.constants import RAISED, MULTIPLE, LEFT, RIGHT, END
from tkinter import messagebox
from tkinter import font

top = tkinter.Tk()
top.title('Đăng ký lớp')
top.geometry('540x400')
top.resizable(0,0)
appFontTieuDe   = font.Font(family = 'Helvetia', size = 20)
appFontNoiDung  = font.Font(family = 'Helvetia', size = 12)

font.families()

lblTieuDe = tkinter.Label(top, text = 'THÔNG TIN HỌC VIÊN', font = appFontTieuDe).grid(row = 0, column = 0, columnspan = 2)
lblHoTen = tkinter.Label(top, text="Họ và tên", padx = 5, pady = 5, font = appFontNoiDung).grid(row = 1, column = 0)
entryHoTen = tkinter.Entry(top, border = 1, width = 40, font = appFontNoiDung)
entryHoTen.grid(row = 1, column = 1)
varHoTenErr = tkinter.StringVar()
lblHoTenErr = tkinter.Label(top, textvariable = varHoTenErr, padx = 5, pady = 5, fg = 'red', font=appFontNoiDung).grid(row = 1, column = 2)
varHoTenErr.set('')

def XyLyDuLieu():
    flag = True
    HoTen = entryHoTen.get().strip()
    if HoTen == '':
        varHoTenErr.set('*')
        flag = False
    else:
        varHoTenErr.set('')

'''
var = tkinter.IntVar()
LbLopHoc = tkinter.Listbox(top, selectmode = MULTIPLE)
LbLopHoc.insert(END, 'Python')
LbLopHoc.insert(END, 'Perl')
LbLopHoc.insert(END, 'PHP')
LbLopHoc.insert(END, 'Java')
LbLopHoc.insert(END, 'C')
LbLopHoc.insert(END, 'Ruby')
LbLopHoc.pack()
def getSelectedItems():
    tuple_item = LbLopHoc.curselection()
    str1 = ''
    for item in tuple_item:
        str1 += LbLopHoc.get(item) + ';'
    messagebox.showinfo('Lớp học bạn đã đăng ký', str1)

button = tkinter.Button(top, text='Hien thi', command = getSelectedItems)
button.pack()

'''
btnSave = tkinter.Button(top, border = 1, width = 10, padx = 5, pady = 5, text = 'Lưu', font=appFontNoiDung, command = XyLyDuLieu).grid(row = 2, column = 0, columnspan = 2)
top.mainloop()