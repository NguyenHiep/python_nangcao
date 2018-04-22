import sqlite3

conn = sqlite3.connect('du_lieu/SQLVatTu.db')

# update table VatTu
chuoiSQL = '''UPDATE `tlbVatTu` 
 SET `TenVatTu` = 'Laptop Mac 15inch', `DonGiaNhap` = 45000000, `DonGiaBan` = 50000000
 WHERE `MaVatTu` = 10
 '''
conn.execute(chuoiSQL)

conn.commit()
conn.close()