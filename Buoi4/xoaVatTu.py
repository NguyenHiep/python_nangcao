import sqlite3

conn = sqlite3.connect('du_lieu/SQLVatTu.db')

# delete table VatTu
chuoiSQL = '''DELETE FROM `tlbVatTu` 
 WHERE `MaVatTu` = 10
 '''
conn.execute(chuoiSQL)

conn.commit()
conn.close()
