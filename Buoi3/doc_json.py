import urllib.request
import json
from pprint import *
def doc_url(path):
    DEFAULT_ENCODING = 'utf-8'
    urlResponse = urllib.request.urlopen(path)

    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING

    data = json.loads(urlResponse.read().decode(encoding))
    return data

if __name__=='__main__':    
    url='https://api.github.com/users?since=100'
    noi_dung=doc_url(url)
    pprint(noi_dung)