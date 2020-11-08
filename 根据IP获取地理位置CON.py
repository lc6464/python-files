from urllib.request import urlopen,Request
from urllib.error import HTTPError
from urllib.parse import urlencode
from json import loads
from re import findall
def getAddress(ip):
    "输入参数：ip，类型：str，内容：IP地址；\n返回类型：str（少数错误情况可能为dict）"
    try:
        ip=findall('^((25[0-5]|2[0-4]\d|[01]?\d?\d)(\.(25[0-5]|2[0-4]\d|[01]?\d?\d)){3})$',ip)[0][0]
    except:
        return 'IP输入有误'
    for i in range(0,25):
        try:
            headers={'Referer': 'http://ip.360.cn/','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
            req=Request("http://ip.360.cn/IPQuery/ipquery",urlencode({'ip':ip}).encode(),headers)
            html=urlopen(req).read().decode()
            break
        except HTTPError as e:
            if e.code == 403:
                if i == 24:
                    return "发生 HTTP %s 错误"%e.code
                continue
            elif e.code == 503:
                if i == 24:
                    return "发生 HTTP %s 错误"%e.code
                continue
            else:
                return "发生 HTTP %s 错误"%e.code
        except:
            return "发生未知错误"
    json=loads(html)
    if json['errno']==0 and json['errmsg']=='' and ('data' in json.keys()):
        return '地理位置：%s'%json['data']
    return json['errmsg']
if __name__=='__main__':
    print(help(getAddress))
    print(getAddress(input('请输入IP地址：')))
