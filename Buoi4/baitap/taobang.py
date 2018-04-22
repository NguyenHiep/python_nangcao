import sqlite3

conn = sqlite3.connect('du_lieu/product.db')

# tao table VatTu
chuoiSQL = '''CREATE TABLE `product` (
	`Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`Name`	TEXT NOT NULL,
	`Price`	REAL NOT NULL,
	`Amount`INTEGER NOT NULL
);'''

conn.execute(chuoiSQL)
conn.close()