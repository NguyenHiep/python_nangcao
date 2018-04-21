from thu_vien.GiaoDich import *
if __name__ == "__main__":
# pdb.set_trace()
print("Quản lý giao dịch:")
list_vang = []
list_tien = []
tiep_tuc = 1
while tiep_tuc == 1:        
    ma = input("Nhập mã GD:\t")
    ngay = input("Nhập ngày GD:\t")
    
    so_luong = int(input("Nhập số lượng:\t"))
    
    
    i = int(input("Chọn loại giao dịch: 1: Vàng, 2: Tiền Tệ:\t"))
    if i == 1:
        tong_slv = 0
        tong_tien_vang = 0
        loai = input("Chọn loai: 18k / 24k / 9999:\t")
        don_gia = eval(input("Nhập đơn giá:\t"))
        gdv = GiaoDich(ma, ngay, don_gia, so_luong, loai)
        list_vang.append(gdv)
        for item in list_vang:
            tong_slv += item.so_luong
            tong_tien_vang += item.thanh_tien()
            print(item.in_giao_dich())        
        print("Tổng số lượng:", tong_slv)
        print("Tổng số tiền:", tong_tien_vang)
    if i == 2:
        tong_slt = 0
        tong_tien_tien = 0
        loai = input("Chọn loai: USD / EUR / AUD:\t")
        don_gia = eval(input("Nhập tỷ giá:\t"))
        mua = True
        gd = int(input("Bạn mua hay bán? 1: mua, 0: bán:\t"))
        if gd == 0:
            mua = False 
        gdtt = GiaoDichTienTe(ma, ngay, don_gia, so_luong, loai, mua)
        list_tien.append(gdtt)
        for item in list_tien:
            tong_slt += item.so_luong
            tong_tien_tien += item.thanh_tien()
            print(item.in_giao_dich())        
        print("Tổng số lượng:", tong_slt)
        print("Tổng số tiền:", tong_tien_tien)
    
    tiep_tuc = int(input("Bạn muốn tiếp tục giao dịch? 1: Có, 0: Không\t")) 