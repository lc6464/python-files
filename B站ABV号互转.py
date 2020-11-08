from urllib.request import Request,urlopen
from json import loads
import sys
ar=sys.argv
ar.pop(0)
h={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36 Edg/81.0.416.58'}
def getLink(vid):
    if vid[:2] == 'av':
        return 'https://api.bilibili.com/x/web-interface/archive/stat?%s=%s'%('aid',vid[2:])
    elif vid[:2] == 'BV':
        return 'https://api.bilibili.com/x/web-interface/archive/stat?%s=%s'%('bvid',vid[2:])
    else:
        return None
def vidConvert(vid):
    if not vid[:2] in ['av','BV']:return "AV号请以av开头，BV号请以BV开头！区分大小写！"
    req=Request(getLink(vid),headers=h)
    json=urlopen(req).read().decode()
    data=loads(json)
    if data['code']!=0:
        return{'code':data['code'],'message':data['message']}
    else:
        data=data['data']
        return{'av':'av%s'%data['aid'],'bv':data['bvid']}
if __name__=='__main__':
    print("请联网使用！否则将会报错退出！！！")
    print("请联网使用！否则将会报错退出！！！")
    print("请联网使用！否则将会报错退出！！！\n")
    for Vid in ar:
        print(vidConvert(Vid))
    while True:
        ip=input('请输入AV/BV号：')
        if ip in ['exit','esc','e','break']:break
        print(vidConvert(ip))
