import sqlite3

def TaoTableSanPham():
    try:
        conn= sqlite3.connect(r'du_lieu/QLSanPham.db')
        #tao table VatTu
        chuoiSQL='''CREATE TABLE `tblSanPham` (
            `Id`	 INTEGER PRIMARY KEY AUTOINCREMENT,
            `Name`	 TEXT,
            `Price`	 REAL,
            `Amount` REAL
        );'''
        conn.execute(chuoiSQL)
        conn.commit()
        conn.close()
    except:
        pass
def ThemSanPham(sanpham):
    conn= sqlite3.connect(r'du_lieu/QLSanPham.db')
    chuoiSQL='''
        insert into tblSanPham(Name,Price,Amount)
        values(?,?,?)
        '''
    conn.execute(chuoiSQL,(sanpham.Name,sanpham.Price,sanpham.Amount))
    conn.commit()
    conn.close()
    print("Da them thanh cong")
def CapNhatSanPham(sanpham):
    conn= sqlite3.connect(r'du_lieu/QLSanPham.db')
    chuoiSQL='''
        update tblSanPham
        set Name=?, Price=?,Amount=?
        where Id=?
        '''
    conn.execute(chuoiSQL,(sanpham.Name,sanpham.Price,sanpham.Amount,sanpham.Id))
    conn.commit()
    conn.close()
    print("da cap nhat")
def XoaSanPham(sanpham):
    conn= sqlite3.connect(r'du_lieu/QLSanPham.db')
    chuoiSQL='''
        delete from tblSanPham where Id=?
        '''
    conn.execute(chuoiSQL,(sanpham.Id))
    conn.commit()
    conn.close()
def DocDanhSachSanPham():
    conn= sqlite3.connect(r'du_lieu/QLSanPham.db')
    chuoiSQL='''
        select Id, Name,Price,Amount from tblSanPham
        '''
    cursor=conn.execute(chuoiSQL)
    for sp in cursor:
        print(sp[0],sp[1],sp[2],sp[3])
    conn.commit()
    conn.close()
def TimKiemSanPham(GTTim):
    conn= sqlite3.connect(r'du_lieu/QLSanPham.db')
    chuoiSQL='''
        select Id, Name,Price,Amount from tblSanPham Where Name like ?
        '''
    cursor=conn.execute(chuoiSQL,('%'+GTTim+'%'))
    for sp in cursor:
        print(sp[0],sp[1],sp[2],sp[3])
    conn.commit()
    conn.close()