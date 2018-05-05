from libraries.XL_BMI import *
import tkinter
from tkinter.constants import RAISED
from tkinter import messagebox

def thanh_tien():
    messagebox.showinfo('Thông báo', 'Chức năng đang phát triển :)) tạm dừng')

top = tkinter.Tk()
top.geometry('600x250')
top.resizable(0,0)
kqLoaiXe      = tkinter.StringVar() # Loại xe
kqSoKM        = tkinter.StringVar() # Số kilomet
kqThoiGianCho = tkinter.StringVar() # BMI
kqThanhTien   = tkinter.StringVar() # Kết luận

top.title('Tính tiền cước taxi')

lblLoaiXe        = tkinter.Label(top, text = 'Chọn loại xe', width = 30).grid(row = 0, column = 1)
entryLoaiXe      = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqLoaiXe, relief = RAISED).grid(row = 0, column = 2)

lblSoKM          = tkinter.Label(top, text = 'Sô km', width = 30).grid(row = 1, column = 1)
entrySoKM        = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqSoKM, relief = RAISED).grid(row = 1, column = 2)

lblThoiGianCho   = tkinter.Label(top, text = 'Thời gian chờ', width = 30).grid(row = 4, column = 1)
entryThoiGianCho = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqThoiGianCho, relief = RAISED).grid(row = 4, column = 2)

lblThanhTien     = tkinter.Label(top, text = 'Kết luận', width = 30).grid(row = 5, column = 1)
entryThanhTien   = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqThanhTien, relief = RAISED).grid(row = 5, column = 2)

# Set empty
kqLoaiXe.set('')
kqSoKM.set('')
kqThoiGianCho.set('')
kqThanhTien.set('')

btnTinhTien = tkinter.Button(top, text = 'Tính Tiền', command = thanh_tien).grid(row = 3, column = 2)


top.mainloop()