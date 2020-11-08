def dingPost(token,secKey,jsonFileName='json.json',encoding='utf-8'):
    from dingSign import sign
    from urllib.request import Request,urlopen
    from json import load,dumps
    from time import strftime
    tAs=sign(secKey)
    headers = {"Content-Type": "application/json; charset=UTF-8"}
    url = "https://oapi.dingtalk.com/robot/send?access_token=%s&timestamp=%s&sign=%s"%(token,tAs['timestamp'],tAs['sign'])
    with open(jsonFileName,encoding=encoding) as f:
        data=dumps(load(f)).encode()
    response = urlopen(Request(url,data,headers)).read().decode()
    nT=strftime('%Y-%m-%d %H:%M:%S')
    return {"time": nT, "response": response}
if __name__=='__main__':
    tk=input("请输入Access Token：")
    sn=input("请输入SEC Key：")
    print(dingPost(tk,sn))