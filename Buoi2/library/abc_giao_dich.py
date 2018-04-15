import abc

class GiaoDich(abc.ABC):
    
    @abc.abstractclassmethod
    def __init__(self, ma, ngay, soluong, loai):
        pass

    @abc.abstractclassmethod
    def tinh_tien(self):
        pass

    @abc.abstractclassmethod
    def in_giao_dich(self):
        pass
    

    