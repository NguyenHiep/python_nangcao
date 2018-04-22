import sqlite3

conn = sqlite3.connect('du_lieu/SQLVatTu.db')

# tao table VatTu
chuoiSQL = '''CREATE TABLE `tlbVatTu` (
	`MaVatTu`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`TenVatTu`	TEXT,
	`DonViTinh`	TEXT,
	`DonGiaNhap`	REAL,
	`DonGiaBan`	REAL,
	`ThoiGianBaoHanh`	INTEGER
);'''
conn.execute(chuoiSQL)

#tao table KhachHang
chuoiSQL = '''CREATE TABLE `tblKhachHang` (
	`MaKH`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`TenKH`	TEXT,
	`DiaChi`	TEXT,
	`Email`	TEXT
);'''

conn.execute(chuoiSQL)
conn.close()