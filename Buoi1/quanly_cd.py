from thuvien.XL_CD import *

tt = 1
DSCD = []

while tt == 1:
    tenCD    = input('Ten CD: ')
    TenCaSi  = input('Ten ca sy: ')
    SoBaiHat = int(input('So bai hat: '))
    Giatien  = eval(input('Gia tien: '))
    cd       = XL_CD(tenCD, TenCaSi, SoBaiHat, Giatien)
    DSCD.append(cd)
    tt = eval(input('1: Tiep tuc, 0: Dung lai! '))

tongtien = 0

for cd in DSCD:
    tongtien += cd.Giatien
    print(cd.thong_tin_cd())
print('Tong tien la: ', tongtien)
    
