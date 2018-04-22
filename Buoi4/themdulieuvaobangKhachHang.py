import sqlite3

conn = sqlite3.connect('du_lieu/SQLVatTu.db')

# tao table VatTu
chuoiSQL = '''INSERT INTO `tlbKhachHang`(`TenKH`,`DiaChi`,`Email`)
 VALUES ('Nguyen Van A','Tan binh','');'''
conn.execute(chuoiSQL)


conn.commit()
conn.close()