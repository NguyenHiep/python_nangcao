
class XL_CD ():
    def __init__(self, tenCD, TenCaSi, SoBaiHat, Giatien):
        self.tenCD    = tenCD
        self.TenCaSi  = TenCaSi
        self.SoBaiHat = SoBaiHat
        self.Giatien  = Giatien

    def thong_tin_cd(self):
        thongtin = '';
        thongtin += '#' + str(self.tenCD) + '--' + str(self.TenCaSi) + '--' + str(self.SoBaiHat) + '--' + str(self.Giatien)
        return thongtin
