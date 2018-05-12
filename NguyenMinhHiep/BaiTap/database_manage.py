import sqlite3

def insert_cd(cd): 
    # thêm mới 1 cd vào bảng CD 
    try:
        result = False 
        conn = sqlite3.connect('du_lieu/quan_ly_cd.db') 
        sql = "INSERT INTO cd (ten,ca_sy,so_bai_hat, gia_thanh,hinh) VALUES (?, ?, ?, ?, ?)" 
        if  conn.execute(sql,(cd.ten, cd.ca_sy, cd.so_bai_hat, cd.gia_thanh,cd.hinh)): 
            print('Thêm mới thành công') 
            result = True 
        conn.commit()     
        conn.close()
        return result
    except:
        pass
    

def select_cd(): 
    # đọc và lấy toàn bộ dữ liệu từ bảng CD 
    try:
        conn = sqlite3.connect('du_lieu/quan_ly_cd.db') 
        list_cds = [] 
        cursor = conn.execute("SELECT *  from CD") 
        for row in cursor: 
            list_cds.append(row)       
        
        conn.commit() 
        conn.close() 
        return list_cds
    except:
        pass

def select_user():
    # đọc và lấy toàn bộ dữ liệu từ bảng user
    try:
        conn = sqlite3.connect('du_lieu/quan_ly_cd.db') 
        print ("Opened database successfully") 
        list_users = [] 
        cursor = conn.execute("SELECT *  from user") 
        for row in cursor:  
            list_users.append(row) 
        
        print ("Operation done successfully") 
        conn.commit() 
        conn.close() 
        return list_users
    except:
        pass
 
def delete_cd(id_cd):
    try: 
        conn = sqlite3.connect('du_lieu/quan_ly_cd.db') 
        print ("Opened database successfully")         
        cur = conn.cursor() 
        sql ='''delete from CD where id = ?''' 
        cur.execute(sql, (id_cd,))        
        conn.commit() 
        conn.close()
    except:
        pass  
 
def update_cd(id_cd, so_bai_hat, gia_thanh):
    try:
        conn = sqlite3.connect('du_lieu/quan_ly_cd.db') 
        print ("Opened database successfully")         
        cur = conn.cursor() 
        sql = ''' UPDATE CD 
                SET so_bai_hat = ?, gia_thanh = ?                   
                WHERE id = ?''' 
        cur.execute(sql, (so_bai_hat, gia_thanh, id_cd)) 
    
        conn.commit() 
        conn.close()
    except:
        pass