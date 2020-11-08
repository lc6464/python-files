from urllib.request import urlopen
def getValue(v,s,e):
    "在指定字符串v中查找字符串s与字符串e之间的内容。"
    f=v.find(s) if v.find(s)>-1 else None
    if f == None:return f
    a=f+len(s)
    b=v.find(e,a)
    return v[a:b]

def idGetVal(v,i):
    "根据di查询value。"
    s='id="'+str(i)+'" value="'
    return getValue(v,s,'"')

def getInfo(xh):    #g441622200609130025
    "利用学籍管理系统通过学籍号获取学生信息。"
    html = urlopen("http://www.lcyzczb.com/cjcx/edut_student_6.asp?id=%s"%xh).read().decode("gb18030")
    if html.find("不存在该ID的学生")>-1:return "不存在该学籍号的学生！"
    d={}
    item=idGetVal(html,'sname')
    d["姓名"]=item
    item=idGetVal(html,'ksh')
    d["考生号"]=item
    d["监护人"]=[{},{}]
    item=idGetVal(html,'jh1_m')
    d["监护人"][0]["姓名"]=item
    item=idGetVal(html,'jh1_sfz')
    d["监护人"][0]["身份证号"]=item
    item=idGetVal(html,'jh1_sj')
    d["监护人"][0]["手机号"]=item
    item=getValue(getValue(html,'id="jh1_gx">','</sel'),'ted>','<')
    d["监护人"][0]["关系"]=item
    item=idGetVal(html,'jh1_sm')
    d["监护人"][0]["关系说明"]=item
    item=idGetVal(html,'jh2_m')
    d["监护人"][1]["姓名"]=item
    item=idGetVal(html,'jh2_sfz')
    d["监护人"][1]["身份证号"]=item
    item=idGetVal(html,'jh2_sj')
    d["监护人"][1]["手机号"]=item
    item=getValue(getValue(html,'id="jh2_gx">','</sel'),'ted>','<')
    d["监护人"][1]["关系"]=item
    item=idGetVal(html,'jh2_sm')
    d["监护人"][1]["关系说明"]=item
    return d

if __name__=='__main__':
    print(help(getInfo))
    print(getInfo('g110000200001010000'))
