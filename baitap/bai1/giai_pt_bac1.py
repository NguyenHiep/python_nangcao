
class GiaiPhuongTrinhBacNhat():

    def __init__(self, _a, _b):
        self.a = _a
        self.b = _b

    def tim_nghiem(self):
        nghiem = '';
        if self.a == 0 and self.b != 0:
            nghiem += 'Phuong trinh vo nghiem'
        elif self.a == 0 and self.b == 0:
            nghiem += 'Phuong trinh vo so nghiem'
        else:
            nghiem += str(- self.b / self.a)
        return nghiem
    
    def in_nghiem(self):
        print('Ket qua la: ', self.tim_nghiem())
    

if __name__ == '__main__':
    
    a = eval(input('Nhap a: '))
    b = eval(input('Nhap b: '))

    giai_pt = GiaiPhuongTrinhBacNhat(a,b)
    giai_pt.in_nghiem();