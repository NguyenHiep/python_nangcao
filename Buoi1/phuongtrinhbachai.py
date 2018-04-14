from thuvien.XL_PhuongTrinhBacHai import *
from thuvien.XL_SoNguyen import *

a,b,c = eval(input('Nhap a,b,c: '))
phuong_trinh = XL_PhuongTrinhBacHai(a,b,c)
nghiem = phuong_trinh.TimNghiem()
print(nghiem)

songuyen = eval(input('Nhap so nguyen: '))

xl_songuyen = XL_SoNguyen(songuyen)

if xl_songuyen.is_sochan() == True:
    print('%d la so chan'%songuyen)
else:
    print('%d la so le'%songuyen)     