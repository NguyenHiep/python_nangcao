import json
from pprint import*

def doc_noi_dung_json(filename):
    data_file = open(filename, encoding = "utf-8")
    data = json.load(data_file)
    data_file.close()
    return data    


if __name__ == '__main__':
    url_data = 'du_lieu/QLCT_1.json'
    noi_dung = doc_noi_dung_json(url_data)
    #pprint(noi_dung) # Show content json
    cong_ty  = noi_dung['CONG_TY'][0] # Lay cong ty dau tien
    don_vi   = noi_dung['DON_VI']
    tong_so_nv = 0

    print('Ten cong ty:', cong_ty['Ten'])
    print('Dia chi cong ty: ', cong_ty['Dia_chi'])
    print(' Tong so nhanz vien: ')