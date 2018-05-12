import sqlite3

def TaoTableNhanVien():
    try:
        conn= sqlite3.connect(r'du_lieu/quan_ly_nhanvien.db')
        #tao table User
        chuoiSQL='''CREATE TABLE `nhanvien` (
              `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
              `Ma_NV` TEXT, 
              `Ten_NV` TEXT, 
              `Ngay_sinh` TEXT, 
              `Noi_sinh` TEXT, 
              `Trinh_do` TEXT,
              `Chuyen_mon` TEXT
        );'''
        conn.execute(chuoiSQL)
        conn.commit()
        conn.close()
    except:
        pass

if __name__ == '__main__':
   TaoTableNhanVien()

