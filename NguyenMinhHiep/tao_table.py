import sqlite3

def TaoTableUser():
    try:
        conn= sqlite3.connect(r'du_lieu/quan_ly_cd.db')
        #tao table User
        chuoiSQL='''CREATE TABLE `user` (
             `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
             `username` TEXT NOT NULL UNIQUE, 
             `password` TEXT NOT NULL 
        );'''
        conn.execute(chuoiSQL)
        conn.commit()
        conn.close()
    except:
        pass

def TaoTableCd():
    try:
        conn= sqlite3.connect(r'du_lieu/quan_ly_cd.db')
        #tao table User
        chuoiSQL='''CREATE TABLE `cd` (
             `id` INTEGER PRIMARY KEY AUTOINCREMENT, 
              `ten` TEXT NOT NULL, 
              `ca_sy` TEXT NOT NULL, 
              `so_bai_hat` INTEGER NOT NULL, 
              `gia_thanh` REAL NOT NULL, 
              `hinh` TEXT  
        );'''
        conn.execute(chuoiSQL)
        conn.commit()
        conn.close()
    except:
        pass

def ThemUser():
    try:
        conn= sqlite3.connect(r'du_lieu/quan_ly_cd.db')
        sql1 = "INSERT INTO `user` (`username`,`password`) VALUES ('phuong', '123456' )" 
        sql2 = "INSERT INTO `user` (`username`,`password`) VALUES ('thanhthanh', '123456' )" 
        sql3 = "INSERT INTO `user` (`username`,`password`) VALUES ('duyen', '123456789' )" 
        
        conn.execute(sql1) 
        conn.execute(sql2) 
        conn.execute(sql3)
        conn.commit()
        conn.close()
        print("Them user thanh cong")
    except:
        pass

def ThemCD():
    try:
        conn= sqlite3.connect(r'du_lieu/quan_ly_cd.db')
        sql1 = "INSERT INTO `cd`(`ten`,`ca_sy`,`so_bai_hat`, `gia_thanh`,`hinh`) VALUES ('Happy new year','ABBA', 10, 255000.00,'happy_new_year.gif')" 
        
        conn.execute(sql1) 
        conn.commit()
        conn.close()
        print("Them cd thanh cong")
    except:
        pass

if __name__ == '__main__':
    TaoTableUser()
    TaoTableCd()
    ThemUser()
    ThemCD()

