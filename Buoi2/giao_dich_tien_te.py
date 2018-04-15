from library.abc_giao_dich import*

class Giao_Dich_Tien_Te(GiaoDich):

    def __init__(self, ma, ngay, soluong, loai, loai_tien_te, tygia, action):
        self.ma            = ma
        self.ngay          = ngay
        self.soluong       = soluong
        self.loai          = loai
        self.loai_tien_te  = loai_tien_te
        self.tygia         = tygia
        self.action        = action
    
    def tinh_tien(self):
        
        if self.action == 1:
            thanhtien = self.soluong * self.tygia
        else:
            thanhtien = self.soluong * self.tygia * 1.05
        return thanhtien

    def in_giao_dich(self):
        result = ''
        if self.action == 1:
            result += 'GD mua: '
        else:
            result += 'GD ban: '
        result += str(self.ma) + ' - ' + str(self.ngay) + ' - ' + str(self.loai_tien_te)
        result += ' - ' + str(self.tygia) + ' - ' + str(self.soluong)
        result += ' - Thanh tien = ' + str(self.tinh_tien())
        return result
        
if __name__ == '__main__':

    gd_tien_te = Giao_Dich_Tien_Te(1,'12/12/12',2,2,'USD',16000, 'ban')
    print(gd_tien_te.tinh_tien())
    print(gd_tien_te.in_giao_dich())