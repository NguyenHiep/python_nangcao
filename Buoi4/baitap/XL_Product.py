import sqlite3

class XL_Product():
    def __init__(self):
        self.Id     = ''
        self.Name   = ''
        self.Price  = ''
        self.Amount = ''

    def taobang_sanpham(self):
        try:
            conn = sqlite3.connect('du_lieu/product.db')
            chuoiSQL = '''CREATE TABLE `product` (
                `Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                `Name`	TEXT NOT NULL,
                `Price`	REAL NOT NULL,
                `Amount`INTEGER NOT NULL
            );'''
            conn.execute(chuoiSQL)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
    
    def danhsach_sanpham(self):
        conn = sqlite3.connect('du_lieu/product.db')
        chuoiSQL = '''SELECT * FROM product'''
        cursor   = conn.execute(chuoiSQL)
        conn.commit()
        for item in cursor:
            print(item)
        conn.commit()     
        conn.close()
    ## Xem lai cho nay    
    def them_sanpham(self):
        try:
            conn = sqlite3.connect('du_lieu/product.db')
            chuoiSQL='''INSERT INTO `product` (`Name`, `Price`, `Amount`)
                        VALUES(?,?,?)'''
            conn.execute(chuoiSQL,(self.Name,self.Price,self.Amount))
            conn.commit()
            print("Thêm thành công")
        except Exception as ex:
            print('Error:', ex)
        finally:
            conn.close()
    
    def timkiem_sanpham(self, GTTim):
        try:
            conn= sqlite3.connect(r'du_lieu/product.db')
            chuoiSQL='''SELECT Id, Name, Price, Amount FROM `product` WHERE Name LIKE ?'''
            cursor=conn.execute(chuoiSQL,('%'+GTTim+'%'))
            for sp in cursor:
                print(sp[0],sp[1],sp[2],sp[3])
            conn.commit()
            
        except Exception as ex:
            print('Error:', ex)
        finally:
            conn.close()

    def capnhat_sanpham(self):
        try:
            conn= sqlite3.connect(r'du_lieu/product.db')
            chuoiSQL='''UPDATE `product`
                        SET Name = ?, Price = ?,Amount = ?
                        WHERE Id = ?
                     '''
            conn.execute(chuoiSQL,(self.Name,self.Price,self.Amount,self.Id))
            conn.commit()
            print("Cập nhật thành công!")
        except Exception as ex:
            print('Error: ', ex)
        finally:
            conn.close()
        
        
        
    def xoa_sanpham(self):
        try:
            conn= sqlite3.connect(r'du_lieu/product.db')
            chuoiSQL='''DELETE from `product` WHERE Id = ?'''
            conn.execute(chuoiSQL,(self.Id))
            conn.commit()
            print('Xóa thành công!')
        except Exception as ex:
            print('Error: ', ex)    
        finally:
            conn.close()

    