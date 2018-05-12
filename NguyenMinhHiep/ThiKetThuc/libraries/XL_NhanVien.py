import sqlite3

def insert_nhanvien(nhanvien): 
    # thêm mới 1 nhan vien vào bảng CD 
    try:
        result = False 
        conn = sqlite3.connect('du_lieu/quan_ly_nhanvien.db') 
        sql = "INSERT INTO `nhanvien` (Ma_NV,Ten_NV,Ngay_sinh, Noi_sinh,Trinh_do,Chuyen_mon) VALUES (?, ?, ?, ?, ?, ?)" 
        if  conn.execute(sql,(nhanvien.ma_nv, nhanvien.hoten_nv, nhanvien.ngaysinh, nhanvien.noisinh, nhanvien.trinhdo, nhanvien.chuyenmon)): 
            print('Thêm mới thành công') 
            result = True 
        conn.commit()     
        conn.close()
        return result
    except:
        pass
    

def select_nhanvien(): 
    # đọc và lấy toàn bộ dữ liệu từ bảng CD 
    try:
        conn = sqlite3.connect('du_lieu/quan_ly_nhanvien.db') 
        list_cds = [] 
        cursor = conn.execute("SELECT *  from `nhanvien`") 
        for row in cursor: 
            list_cds.append(row)       
        
        conn.commit() 
        conn.close() 
        return list_cds
    except:
        pass

 
