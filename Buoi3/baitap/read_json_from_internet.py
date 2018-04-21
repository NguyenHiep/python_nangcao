
#Link json:  http://dev-er.com/service_api_ban_sach/api_service_sach.php

import urllib.request
import json
from pprint import *

def doc_json_api_unicode(URL):
    DEFAULT_ENCODING = 'utf-8'
    urlResponse = urllib.request.urlopen(URL)

    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING

    data = json.loads(urlResponse.read().decode(encoding))
    return data



if __name__=='__main__':    
    url='http://dev-er.com/service_api_ban_sach/api_service_sach.php'
    noi_dung=doc_json_api_unicode(url)
    #pprint(noi_dung) # in dung cau truc json
    #print(noi_dung);
    print('Thong ke:')
    print('Tong so sach la: ',len(noi_dung));
    print('Danh sach cac sach:')
    stt = 1
    for sach in noi_dung:
        print(stt, ' / ', str(sach['ten_sach']), '\tNgay xuat ban: ', str(sach['ngay_xuat_ban']), '\tGia bia: ', str(sach['gia_bia']) )
        stt += 1