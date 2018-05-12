
class CD ():
    def __init__(self, ten, ca_sy, so_bai_hat, gia_thanh, hinh):
        self.ten        = ten 
        self.ca_sy      = ca_sy 
        self.so_bai_hat = so_bai_hat 
        self.gia_thanh  = gia_thanh
        self.hinh       = hinh 

    def thong_tin_cd(self):
        thongtin = '';
        thongtin += '#' + str(self.ten) + '--' + str(self.ca_sy) + '--' + str(self.so_bai_hat) + '--' + str(self.gia_thanh)+ '--' + str(self.hinh)
        return thongtin
