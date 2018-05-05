from tkinter.constants import RAISED, BOTH, YES, NW
import tkinter
from libraries.XL_Nam_Am_Lich import *
from doctest import master

# Viết hàm tính năm => hiển thị kết quả lên window mới
list_can  = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
list_chi  = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tí', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
list_hinh = ['than.gif', 'dau.gif', 'tuat.gif', 'hoi.gif', 'ti.gif', 'suu.gif', 'dan.gif', 'mao.gif', 'thin.gif', 'ty.gif', 'ngo.gif', 'mui.gif']


def tinh_nam():
    nam = int(entryNam.get())
    lblKetQua.set(tinh_can_2(list_can, nam) + ' ' + tinh_chi_2(list_chi, nam))
    hinh = 'hinh/' + tinh_hinh_2(list_hinh, nam)

    novi = tkinter.Toplevel()
    novi.geometry('200x150')
    novi.resizable(0, 0)
    canvas = tkinter.Canvas(novi, width = 64, height = 64)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = tkinter.PhotoImage(file = hinh)
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    canvas.gif1 = gif1
    lblHienThiKetQua = tkinter.Label(novi, textvariable = lblKetQua, relief = RAISED, anchor = NW)
    lblHienThiKetQua.pack()

# Khởi tạo window

top = tkinter.Tk()
top.geometry('300x150')
top.resizable(0,0)
top.title('Tính năm âm lịch')
lblKetQua = tkinter.StringVar()

lblNam = tkinter.Label(master = top, text = 'Nhập năm')
lblNam.pack()

entryNam = tkinter.Entry(master = top, bd = 2)
entryNam.pack(padx = 10, pady = 20)

btnTinh = tkinter.Button(master = top, text = 'Tính', command = tinh_nam, bg = 'yellow')
btnTinh.pack()

top.mainloop()