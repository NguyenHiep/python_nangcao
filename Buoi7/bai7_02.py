from libraries.XL_BMI import *
import tkinter
from tkinter.constants import RAISED
from email.mime import image

def in_kq():
    can_nang  = float(kqCanNang.get())
    chieu_cao = float(kqChieuCao.get())
    bmi       = tinh_bmi(chieu_cao, can_nang)
    kqBMI.set(round(bmi,2))
    kqKetLuan.set(ket_luan(bmi))

top = tkinter.Tk()
top.geometry('600x250')
top.resizable(0,0)
kqCanNang  = tkinter.StringVar() # Cân nặng
kqChieuCao = tkinter.StringVar() # Chiều cao
kqBMI      = tkinter.StringVar() # BMI
kqKetLuan  = tkinter.StringVar() # Kết luận

top.title('Tính BMI')
logo = tkinter.PhotoImage(file = 'hinh/bmi.png')
showlogo = tkinter.Label(top, image = logo).grid(row = 0, column = 0)

lblCanNang    = tkinter.Label(top, text = 'Nhập cân nặng (kg)', width = 30).grid(row = 0, column = 1)
entryCanNang  = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqCanNang, relief = RAISED).grid(row = 0, column = 2)

lblChieuCao   = tkinter.Label(top, text = 'Nhập chiều cao (m)', width = 30).grid(row = 1, column = 1)
entryChieuCao = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqChieuCao, relief = RAISED).grid(row = 1, column = 2)

lblBMI        = tkinter.Label(top, text = 'BMI', width = 30).grid(row = 4, column = 1)
entryBMI      = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqBMI, relief = RAISED, bg = 'yellow').grid(row = 4, column = 2)

lblKetLuan    = tkinter.Label(top, text = 'Kết luận', width = 30).grid(row = 5, column = 1)
entryKetLuan  = tkinter.Entry(top, bd = 2, width = 40, textvariable = kqKetLuan, relief = RAISED, bg = 'green').grid(row = 5, column = 2)

# Set empty
kqCanNang.set('')
kqChieuCao.set('')
kqBMI.set('')
kqKetLuan.set('')

btnTinhBMI = tkinter.Button(top, text = 'Tính BMI', command = in_kq).grid(row = 3, column = 2)


top.mainloop()