# import các thư viện cần thiết 
from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox 
from tkinter import filedialog 
import shutil,os 
from database_manage import * 
from cd import CD


def win1(): #man hinh dang nhap 
    mainframe = ttk.Frame(root, padding = '3 3 12 12') 
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
    mainframe.columnconfigure(0, weight = 1) 
    mainframe.rowconfigure(0, weight = 1) 
     
    ttk.Label(master=mainframe, text="Username").grid(row = 0, column = 0)   
    ttk.Entry(master=mainframe, textvariable=var_user).grid(row = 0, column = 1) 
     
    ttk.Label(master=mainframe, text="Password").grid(row = 1, column = 0)   
    ttk.Entry(master=mainframe, show="*", textvariable=var_pass).grid(row = 1, column = 1)    
    
  
    ttk.Button(mainframe, text = 'Đăng nhập', command = win2).grid( row = 2, column = 1, sticky = W)
    root.mainloop()
def win2(): # main window 
    # lấy dữ liệu người dùng nhập 
    global var_user, var_pass 
    username = var_user.get() 
    password = var_pass.get() 
     
    list_users = select_user()
    flag = False 
    for user in list_users: 
        if user[1] == username and user[2] == password: 
            flag = True 
    if flag: 
        # đăng nhập thành công 
        str_kq = "Chào mừng bạn " + username + " đến với CD store!" 
        messagebox.showinfo("Welcome", str_kq)    
        root.withdraw() 
        # xây dựng màn hình cửa hàng  
        new = Toplevel() 
        new.title('Cửa hàng CD') 
        new.geometry("400x300") 
        new.resizable(0, 0) 
        # tạo memu bar 
        menubar = Menu(new) 
        chuc_nang = Menu(menubar, tearoff=0) 
    
        chuc_nang.add_command(label="Thêm sản phẩm mới", command=win3) 
        chuc_nang.add_command(label="Tìm kiếm sản phẩm", command=win4) 
        chuc_nang.add_command(label="Cập nhật sản phẩm", command=win5) 
        chuc_nang.add_command(label="Xóa sản phẩm", command=win6) 
    
 
        chuc_nang.add_separator() 
        chuc_nang.add_command(label="Thoát", command=new.quit) 
         
        menubar.add_cascade(label="Danh mục chức năng", menu= chuc_nang) 
           
        #main frame 
        mainframe = ttk.Frame(new, padding = '3 3 12 12') 
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
        mainframe.columnconfigure(0, weight = 1) 
        mainframe.rowconfigure(0, weight = 1) 
         
        new.config(menu=menubar) 
         
        logo1 = PhotoImage(file="images/store_1.gif") 
        L = ttk.Label(master=mainframe, image=logo1)
        L.image = logo1 
        L.grid(row=0, column=1, sticky=W) 
    else:  
    # đăng nhập không thành công 
        messagebox.showinfo("Warning",  "Username  và  Password  chưa  chính xác!")    
        var_user.set("") 
        var_pass.set("")

def upload_file():     
    des = "images/" 
    file_path = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) 
        
    if (os.path.isfile(file_path)): 
        shutil.copy(file_path, des)         
        fname = str(file_path).split('/')[-1:][0] 
        messagebox.showinfo( "File moving...", "Success: " + fname) 
        global var_hinh 
        var_hinh.set(fname) 
    else: 
        messagebox.showinfo( "File moving...", "Fail")
def them():     
    global var_ten, var_ca_sy, var_gia, var_bai_hat, var_hinh 
    ten = var_ten.get() 
    ca_sy = var_ca_sy.get() 
    so_bai_hat = int(var_bai_hat.get()) 
    gia_thanh = float(var_gia.get()) 
    hinh = var_hinh.get() 
     
    cd = CD(ten, ca_sy, so_bai_hat, gia_thanh, hinh) 
     
    result = insert_cd(cd) 
    if result: 
        messagebox.showinfo("Success", "Thêm mới thành công!")  
    else: 
        messagebox.showinfo("Fail", "Thêm mới không thành công!") 
    
def win3():
    root.withdraw()
    new = Toplevel() 
    new.title('Thêm CD mới') 
    new.geometry("400x300") 
    new.resizable(0, 0)   
            
    mainframe = ttk.Frame(new, padding = '3 3 12 12') 
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
    mainframe.columnconfigure(0, weight = 1) 
    mainframe.rowconfigure(0, weight = 1) 
             
    ttk.Label(master=mainframe, text="Tên CD").grid(row = 0, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_ten).grid(row = 0, column = 1) #var_ten 
     
    ttk.Label(master=mainframe, text="Ca sỹ").grid(row = 1, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_ca_sy).grid(row = 1, column = 1) #var_ca_sy 
     
    ttk.Label(master=mainframe, text="Số bài hát").grid(row = 2, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_bai_hat).grid(row = 2, column = 1) #var_bai_hat 
     
    ttk.Label(master=mainframe, text="Giá thành").grid(row = 3, column = 0)   
    ttk.Entry(master=mainframe, width=50, textvariable=var_gia).grid(row = 3, column = 1) #var_gia 
     
    ttk.Label(master=mainframe, text="Hình").grid(row = 4, column = 0)   
    #ttk.Entry(master=mainframe, width=50).grid(row = 4, column = 1) 
    ttk.Label(master=mainframe, textvariable=var_hinh, width=25).grid(row = 4, column = 1, sticky = W)   
    ttk.Button(mainframe, text='Chọn hình...', command=upload_file).grid( row = 4, column = 1, sticky=E)  
      
    ttk.Button(mainframe, text = 'Thêm CD mới', command = them).grid( row = 5, column = 1, sticky = W)

def tim(mainframe):   
    global var_ten  
    ten = var_ten.get() 
    list_cds = select_cd()     
     
    ttk.Label(mainframe, text='Tên CD', borderwidth=1, relief="raised").grid(row=2,column=0)  
    ttk.Label(mainframe, text='Ca sỹ', borderwidth=1, relief="raised").grid(row=2,column=1)             
    ttk.Label(mainframe, text='Giá thành', borderwidth=1, relief="raised").grid(row=2,column=2)    
    ttk.Label(mainframe, text='Hình', borderwidth=1, relief="raised").grid(row=2,column=3)                            
    r =3
    count = 0   
    for cd in list_cds: 
        if cd[1].lower().find(ten.lower()) != -1:  
            count +=1 
            ttk.Label(mainframe, text=cd[1], borderwidth=1).grid(row=r,column=0) 
            ttk.Label(mainframe, text=cd[2], borderwidth=1).grid(row=r,column=1)   
            ttk.Label(mainframe, text=cd[4], borderwidth=1).grid(row=r,column=2) 
         
            hinh = 'images/' + cd[5] 
            logo1 = PhotoImage(file=hinh) 
         
            L = ttk.Label(master=mainframe, image=logo1)
            L.image = logo1 
            L.grid(row=r, column=3, sticky=W)  
                           
            r +=1 
    if count==0: 
        messagebox.showinfo( "Fail", "Không tìm thấy CD") 
def win4():
    root.withdraw() 
    new = Toplevel() 
    new.title('Tìm kiếm CD') 
     
    mainframe = ttk.Frame(new, padding = '3 3 12 12') 
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
    mainframe.columnconfigure(0, weight = 1) 
    mainframe.rowconfigure(0, weight = 1) 
    
    ttk.Label(master=mainframe, text="Tên CD").grid(row = 0, column = 0)   
    ttk.Entry(master=mainframe, width=20,textvariable=var_ten).grid(row = 0, column = 1) 
     
    ttk.Button(mainframe, text = 'Tìm', command = lambda:tim(mainframe)).grid( 
        row = 1, column = 1, sticky = W)
def win5():
    root.withdraw() 
    new = Toplevel() 
    new.title('Cập nhật CD') 
    new.geometry("400x300") 
    new.resizable(0, 0)   
     
    
    mainframe = ttk.Frame(new, padding = '3 3 12 12') 
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
    mainframe.columnconfigure(0, weight = 1) 
    mainframe.rowconfigure(0, weight = 1)       
    
    ttk.Label(master=mainframe, text="Mã  CD  muốn  cập  nhật").grid(row =  0, column = 0)   
    ttk.Entry(master=mainframe, width=30, textvariable=var_id).grid(row = 0, column = 1) 
     
    ttk.Button(mainframe, text =  'Hiển  thị  thông  tin CD', command = hien_thi_cd).grid( row = 1, column = 1, sticky = W) 

def hien_thi_cd():     
    global var_id  
    id_cd = var_id.get() 
    list_cds = select_cd() 
     
    cd_tim = None 
    for cd in list_cds: 
        if int(id_cd) == int(cd[0]): 
            cd_tim = cd 
            break 
    if cd_tim !=None:            
        root.withdraw() 
        new = Toplevel() 
        new.title('Cập nhật CD') 
        new.geometry("400x300") 
        new.resizable(0, 0)   
                    
        mainframe = ttk.Frame(new, padding = '3 3 12 12') 
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
        mainframe.columnconfigure(0, weight = 1) 
        mainframe.rowconfigure(0, weight = 1)         
 
        var_id.set(cd_tim[0]) 
        var_ten.set(cd_tim[1]) 
        var_bai_hat.set(cd[3]) 
        var_gia.set(cd[4]) 
 
        ttk.Label(master=mainframe, text="Mã CD").grid(row = 0, column = 0) 
        ttk.Label(master=mainframe, width=50, textvariable=var_id).grid(row = 0, column = 1)             
            
        ttk.Label(master=mainframe, text="Tên CD").grid(row = 1, column = 0)   
        ttk.Label(master=mainframe, width=50, textvariable=var_ten).grid(row = 1, column = 1) #var_ten     
        
        ttk.Label(master=mainframe, text="Số bài hát").grid(row = 2, column = 0)   
        ttk.Entry(master=mainframe, width=50, textvariable=var_bai_hat).grid(row = 2, column = 1) #var_bai_hat 
         
        ttk.Label(master=mainframe, text="Giá thành").grid(row = 3, column = 0)   
        ttk.Entry(master=mainframe, width=50, textvariable=var_gia).grid(row = 3, column = 1) #var_gia  
        
        ttk.Button(mainframe, text = 'Cập nhật', command = cap_nhat).grid( row = 5, column = 1, sticky = W)     
    else: 
        messagebox.showinfo("Thông báo", "Không tìm thấy CD này!") 

def cap_nhat(): 
    global var_id 
    global var_bai_hat 
    global var_gia 
      
    id_cd = var_id.get() 
    so_bai_hat = var_bai_hat.get() 
    gia_thanh = var_gia.get() 
     
    list_cds = select_cd() 
    find = False 
    for cd in list_cds: 
        if int(id_cd)  == int(cd[0]): 
            # goi hàm xoa 
            value = messagebox.askokcancel("Xác nhận cập nhật", "Bạn có thật sự muốn cập nhật hay không?") 
            print(value) 
            if value: 
                update_cd(id_cd, so_bai_hat, gia_thanh) 
                messagebox.showinfo("Xác nhận", "Đã cập nhật CD!") 
            find = True 
            break     
    if find != True: 
        messagebox.showinfo("Thông báo", "Không có CD này nên không thể cập nhật!")

def xoa_cd(): 
    global var_id  
    id_cd = var_id.get() 
    list_cds = select_cd() 
    find = False 
    for cd in list_cds: 
        if int(id_cd)  == int(cd[0]): 
            # goi hàm xóa 
            value = messagebox.askokcancel("Xác nhận xóa", "Bạn có thật sự muốn xóa hay không?") 
            print(value) 
            if value: 
                delete_cd(id_cd) 
                messagebox.showinfo("Xác nhận", "Đã xóa xong CD!") 
            find = True 
            break     
    if find != True: 
        messagebox.showinfo("Thông  báo",  "Không  tìm  thấy  CD  này  nên không thể xóa!")

def win6():
    root.withdraw() 
    new = Toplevel() 
    new.title('Xóa CD') 
    new.geometry("400x150") 
    new.resizable(0, 0)   
     
    mainframe = ttk.Frame(new, padding = '3 3 12 12') 
    mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S)) 
    mainframe.columnconfigure(0, weight = 1) 
    mainframe.rowconfigure(0, weight = 1)    
    
         
    ttk.Label(master=mainframe, text="Mã CD muốn xóa").grid(row = 0, column = 0)   
    ttk.Entry(master=mainframe, width=30, textvariable=var_id).grid(row = 0, column = 1) #var_ma 
     
    ttk.Button(mainframe, text = 'Xóa', command = xoa_cd).grid( row = 1, column = 1, sticky = W) 

    
root = Tk()   
root.title('Đăng nhập') 
root.geometry("200x100") 
root.resizable(0, 0) 
# khai báo biến cần thiết cho màn hình đăng nhập 
var_user = StringVar() 
var_pass = StringVar() 
#man hinh them moi 
var_ten = StringVar() 
var_ca_sy = StringVar() 
var_bai_hat = StringVar() 
var_gia = StringVar() 
var_hinh = StringVar()
var_id = StringVar()
# gọi màn hình đăng nhập 
win1() 



