import sqlite3

conn = sqlite3.connect('du_lieu/SQLVatTu.db')

chuoiSQL = '''SELECT *FROM tlbVatTu'''
cursor =conn.execute(chuoiSQL)
#conn.commit()
for item in cursor:
    print(item)

conn.close()
