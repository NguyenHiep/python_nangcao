
class XL_SoNguyen():

    def __init__(self, songuyen):
        self.songuyen = songuyen

    def is_sochan(self):
        if self.songuyen % 2 == 0:
            return True
        return False

    def is_sole(self):
        if self.songuyen % 2 != 0:
            return True
        return False
        
    