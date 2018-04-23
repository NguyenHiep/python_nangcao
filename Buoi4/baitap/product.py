from XL_Product import *

if __name__ == '__main__':
    tt = 1
    while tt == 1:
        print('Bạn muốn làm gì?')
        print('1. Hiển thị danh sách sản phẩm')
        print('2. Thêm sản phẩm mới')
        print('3. Tìm kiếm sản phẩm theo tên')
        print('4. Cập nhật sản phẩm')
        print('5. Xóa sản phẩm')
        chon = int(input('Chọn: '))
        
        if chon == 1:
            print('Danh sách sản phẩm')
            sp = XL_Product()
            sp.danhsach_sanpham()
        elif chon == 2:
             Name   = input('Nhập tên sản phẩm: ')
             Price  = float(input('Nhập giá sản phẩm: '))
             Amount = int(input('Nhập đơn giá: '))
             sp = XL_Product()
             setattr(sp, 'Name', Name)
             setattr(sp, 'Price', Price)
             setattr(sp, 'Amount', Amount)
             sp.them_sanpham()
        elif chon == 3:
             print('Tìm kiếm sản phẩm theo tên \n')
             search_name = input('Nhập tên sản phẩm cần tìm: \t')
             sp = XL_Product()
             sp.timkiem_sanpham(search_name)
            
        elif chon == 4:
             print('Cập nhật sản phẩm \n')
             Id     = int(input('Nhập id cần cập nhật: '))
             Name   = input('Nhập tên sản phẩm: ')
             Price  = float(input('Nhập giá sản phẩm: '))
             Amount = int(input('Nhập đơn giá: '))
             sp = XL_Product()
             setattr(sp, 'Id', Id)
             setattr(sp, 'Name', Name)
             setattr(sp, 'Price', Price)
             setattr(sp, 'Amount', Amount)
             sp.capnhat_sanpham()
        elif chon == 5:
             print('Xóa sản phẩm\n')
             Id_sp = input('Nhập mã sản phẩm:')
             sp = XL_Product()
             setattr(sp, 'Id', Id_sp)
             sp.xoa_sanpham()
        else:
            print('Không có lựa chọn này!')

        tt = eval(input('\nBan muốn tiếp tục không (1: Tiếp tục, 0: Dừng lại ): '))
            
