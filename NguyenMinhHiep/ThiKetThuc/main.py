from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
from nhanvien import NhanVien
from libraries.XL_NhanVien import *

def them_nhanvien():     
    global var_ma_nv, var_hoten_nv, var_ngaysinh, var_noisinh, var_trinhdo, var_chuyenmon
    ma_nv     = var_ma_nv.get() 
    hoten_nv  = var_hoten_nv.get() 
    ngaysinh  = var_ngaysinh.get() 
    noisinh   = var_noisinh.get() 
    trinhdo   = var_trinhdo.get()
    chuyenmon = var_chuyenmon.get()
     
    nhanvien = NhanVien(ma_nv, hoten_nv, ngaysinh, noisinh, trinhdo, chuyenmon) 
    result = insert_nhanvien(nhanvien) 
    if result: 
        messagebox.showinfo("Success", "Thêm mới thành công!")  
    else: 
        messagebox.showinfo("Fail", "Thêm mới không thành công!") 

def frm_them_nhanvien():
    top.withdraw()
    new = Toplevel() 
    new.title('Thêm nhân viên') 
    new.geometry("400x300") 
    new.resizable(0, 0)   
            
    mainframe = ttk.Frame(new, padding = '3 3 12 12') 
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
    mainframe.columnconfigure(0, weight = 1) 
    mainframe.rowconfigure(0, weight = 1) 
             
    ttk.Label(master=mainframe, text="Mã nhân viên").grid(row = 0, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_ma_nv).grid(row = 0, column = 1) #var_ma_nv
     
    ttk.Label(master=mainframe, text="Họ tên nhân viên").grid(row = 1, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_hoten_nv).grid(row = 1, column = 1) #var_hoten_nv 
     
    ttk.Label(master=mainframe, text="Ngày sinh").grid(row = 2, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_ngaysinh).grid(row = 2, column = 1) #var_ngaysinh 
     
    ttk.Label(master=mainframe, text="Nơi sinh").grid(row = 3, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_noisinh).grid(row = 3, column = 1) #var_noisinh 
    
    ttk.Label(master=mainframe, text="Trình độ").grid(row = 4, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_trinhdo).grid(row = 4, column = 1) #var_trinhdo 

    ttk.Label(master=mainframe, text="Chuyên môn").grid(row = 5, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_chuyenmon).grid(row = 5, column = 1) #var_chuyenmon 

      
    ttk.Button(mainframe, text = 'Thêm nhân viên mới', command = them_nhanvien).grid( row = 6, column = 1, sticky = W)

def xuat_json():
    list_nhanvien = []
    data_item = dict()
    ds_nhanvien = select_nhanvien()
    for nhanvien in ds_nhanvien:
        data_item['Ma_NV']      = nhanvien[1]
        data_item['Ten_NV']     = nhanvien[2]
        data_item['Ngay_sinh']  = nhanvien[3]
        data_item['Noi_sinh']   = nhanvien[4]
        data_item['Trinh_do']   = nhanvien[5]
        data_item['Chuyen_mon'] = nhanvien[6]
        list_nhanvien.append(data_item)
    data_file = open("du_lieu/ql_nhanvien.json", "w")
    json.dump(list_nhanvien, data_file, indent=4)
    data_file.close()

top = Tk()

top.title('Kiểm tra kết thúc python nâng cao')
top.geometry('600x300')
top.resizable(0,0)

menubar = Menu(top)
# Menu 1
menu_nhanvien = Menu(menubar, tearoff = 0)
menu_nhanvien.add_command(label = 'Thêm nhân viên', command = frm_them_nhanvien)
menu_nhanvien.add_command(label = 'Xuất thành file Json', command = xuat_json)
menu_nhanvien.add_separator()
menu_nhanvien.add_command(label = 'Đóng ứng dụng', command = top.quit)
menubar.add_cascade(label = 'Nhân viên', menu = menu_nhanvien)
top.config(menu = menubar)

# Them moi nhan vien

var_ma_nv     = StringVar() 
var_hoten_nv  = StringVar() 
var_ngaysinh  = StringVar() 
var_noisinh   = StringVar() 
var_trinhdo   = StringVar()
var_chuyenmon = StringVar()


top.mainloop()