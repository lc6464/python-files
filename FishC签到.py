from urllib.request import Request,urlopen
def findUrl(Cookies):
    "参数Cookies，值：鱼C账号的Cookies。\n以Windows 10 64位的UA，合适的Referer以及你的账号的Cookies为请求头，\n向鱼C签到页面发起请求获取签到链接。"
    url='https://fishc.com.cn/plugin.php?id=k_misign:sign'
    cookies=Cookies if Cookies != '' else None
    if cookies==None:
        print('未输入Cookies！')
        return False
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Referer':'https://fishc.com.cn/','Cookie':cookies}
    req=Request(url=url,headers=headers)
    print('正在请求签到链接……')
    html=urlopen(req).read().decode('gbk')
    print('服务器已响应，正在查找签到链接……')
    a=html.find('<a id="JD_sign" href="')+22 if html.find('<a id="JD_sign" href="')>-1 else -1
    b=html.find('" onclick=',a)
    rootUrl=html[a:b]
    if rootUrl=='':
        print('未找到签到链接！')
        return False
    else:
        return 'https://fishc.com.cn/'+rootUrl
def SignIn(Cookies,URL):
    "参数Cookies，值：鱼C账号的Cookies，\nURL：签到URL。\n以Windows 10 64位的UA，合适的Referer以及你的账号的Cookies为请求头，\n向签到链接发起请求。"
    cookies=Cookies if Cookies != '' else None
    if cookies==None:
        print('未输入Cookies！')
        return False
    Url=URL if not URL in ["",None,False] else None
    if Url == None:
        print('未输入签到链接！')
        return False
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36','Referer':'https://fishc.com.cn/plugin.php?id=k_misign:sign','Cookie':cookies}
    req=Request(url=Url,headers=headers)
    try:
        urlopen(req)
    except:
        print('签到失败！')
        return False
    return '完成！'
if __name__=='__main__':
    c=input('请输入你的鱼C账号的Cookies：')
    print(SignIn(c,findUrl(c)))
    #致小白：若要实现定时自动签到，
    #直接把上面的“input(...)”改成你的鱼C账号的cookies即可。
