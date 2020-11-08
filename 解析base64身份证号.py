def sfzhB64Decode():
    """解析Base64编码中的身份证号并输出到工作簿（特别设计，每三个身份证号只输出一个）。"""
    from base64 import b64decode
    from openpyxl import Workbook
    from re import findall
    from os import path,mkdir
    from datetime import datetime
    wb = Workbook()
    ws=wb.active
    b64Str=input('请输入要解码的带身份证号的base64编码字符串：')
    Str=b64decode(b64Str).decode()
    sfzhList=findall('([1-6][1-7]\d{4}(18|19|20)\d{2}(0\d|1[0-2])([0-2]\d|3[01])\d{3}[0-9xX])',Str)
    a=0
    for i in range(0,len(sfzhList)-2,3):
        a+=1
        ws.cell(row=a,column=1).value=sfzhList[i][0]
    nT=datetime.now()
    nTD=nT.strftime('%Y-%m-%d')
    nTS=nT.strftime('%H_%M_%S')
    fname=r"解析身份证号_return(%s)\return(%s).xlsx" % (nTD,nTS)
    if not (path.exists('解析身份证号_return(%s)' % nTD)):
        mkdir('解析身份证号_return(%s)' % nTD)
    wb.save(fname)
    print('已输出到“'+fname+'”。')

if __name__=='__main__':
    print('Loading…')
    sfzhB64Decode()
