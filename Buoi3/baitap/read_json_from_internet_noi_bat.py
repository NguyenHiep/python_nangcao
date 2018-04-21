from read_json_from_internet import *

from pprint import *

if __name__ == '__main__':
    url = 'http://dev-er.com/service_api_ban_sach/api_service_sach.php?task=sach_noi_bat'
    ds_sach = doc_json_api_unicode(url)
    tong_sach = len(ds_sach)
    '''
 tên sách, tác giả, ngày xuất bản, giá bìa, giới thiệu 
    '''
    print('--- Danh sach %d sach noi bat---'%tong_sach)
    for sach in ds_sach:
        print('Ten sach:' + sach['ten_sach'] +
        ', Tac gia: '+ sach['ten_tac_gia'] + 
        ', Ngay xuat ban: '+ str(sach['ngay_xuat_ban']) +
        ', Gia bia: ' +  str(sach['gia_bia']) +
        ', Gioi thieu:' +  sach['gioi_thieu'][0:200])
        print('\n')