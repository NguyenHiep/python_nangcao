
# Sử dụng debug với thư viện pdb

## Cai dat pygame:  py -m pip install -U pygame --user

##Cai dat pyexex:  pip install py2exe 
import pdb
import math

def tinh_bmi(can_nang, chieu_cao):
    bmi =can_nang / math.pow(chieu_cao, 2)
    return bmi

def danh_gia_bmi(bmi):
    kq = ''
    if bmi < 18.5:
        kq = 'gầy'
    elif bmi < 25:
        kq = 'bình thường'
    else:
        kq = 'thừa cân'
    return kq

if __name__ == '__main__':
    can_nang  = eval(input('Nhập cân nặng (kq): \n'))
    chieu_cao = eval(input('Nhập chiều cao (m): \n'))
    pdb.set_trace() # Debug từng dòng
    bmi = tinh_bmi(can_nang, chieu_cao)
    print('Chỉ số BMI của bạn %.2f'%bmi)
    print('Kết quả: Bạn ', danh_gia_bmi(bmi))