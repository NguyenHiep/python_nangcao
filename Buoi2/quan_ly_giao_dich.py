from giao_dich_tien_te import *
from giao_dich_vang import *

if __name__ == '__main__':
 
    tt = 1
    DSGD = []
    print('Quan ly giao dich: \n')
    while tt == 1:
        magd   = input('Nhap ma giao dich: \t')
        ngaydg = input('Nhap ngay giao dich: \t')
        soluong = int(input('Nhap so luong: \t'))
        loai_gd = eval(input('Chon loai giao dich: 1: Vang, 2: Tien te: '))
        if loai_gd == 1:
            loai = input('Chon loai: 18k / 24k / 9999: \t')
        else:
            loai = input('USD / EUR / AUD: \t')
        dongia = eval(input('Nhap don gia: \t'))
        
        if loai_gd != 1:
            action = int(input('Ban mua hay ban: 1: mua, 0: ban: \t'))

        if loai_gd == 1:
            GD = Giao_Dich_Vang(magd,ngaydg,soluong,loai_gd,loai,dongia)
        else:
            GD = Giao_Dich_Tien_Te(magd,ngaydg,soluong,loai_gd,loai,dongia, action)
        DSGD.append(GD)

        tt = eval(input('Ban muon tiep tuc giao dich? 1: Co, 0: Khong \t'))
    
    for gd in DSGD:
        print(gd.in_giao_dich())