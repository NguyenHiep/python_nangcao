import sqlite3

conn = sqlite3.connect('du_lieu/SQLVatTu.db')

# tao table VatTu
chuoiSQL = '''INSERT INTO `tlbVatTu`(`TenVatTu`,`DonViTinh`,`DonGiaNhap`,`DonGiaBan`,`ThoiGianBaoHanh`)
 VALUES ('Laptop Dell ','Cái',15000000,15500000,1);'''
conn.execute(chuoiSQL)

chuoiSQL = '''INSERT INTO `tlbVatTu`(`TenVatTu`,`DonViTinh`,`DonGiaNhap`,`DonGiaBan`,`ThoiGianBaoHanh`)
 VALUES ('Laptop Asus ','Cái',15000000,15500000,1);'''
conn.execute(chuoiSQL)

chuoiSQL = '''INSERT INTO `tlbVatTu`(`TenVatTu`,`DonViTinh`,`DonGiaNhap`,`DonGiaBan`,`ThoiGianBaoHanh`)
 VALUES ('Laptop LG ','Cái',15000000,15500000,1);'''
conn.execute(chuoiSQL)

chuoiSQL = '''INSERT INTO `tlbVatTu`(`TenVatTu`,`DonViTinh`,`DonGiaNhap`,`DonGiaBan`,`ThoiGianBaoHanh`)
 VALUES ('Laptop Sony ','Cái',15000000,15500000,1);'''
conn.execute(chuoiSQL)

chuoiSQL = '''INSERT INTO `tlbVatTu`(`TenVatTu`,`DonViTinh`,`DonGiaNhap`,`DonGiaBan`,`ThoiGianBaoHanh`)
 VALUES ('Laptop Mac ','Cái',25000000,15500000,1);'''
conn.execute(chuoiSQL)

conn.commit()
conn.close()