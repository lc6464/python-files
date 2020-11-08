from urllib.request import *
import datetime
def getX(Id):return '10X98765432'[sum(map(lambda x:int(x[0])*x[1],zip(Id[0:17],[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2])))%11]
def get3(n):
    if n < 10:a="00%s"%n
    elif n < 100:a="0%s"%n
    else:a=str(n)
    return a
def getRange(s,e):
    begin = datetime.date(int(s.split('-')[0]),int(s.split('-')[1]),int(s.split('-')[2]))
    end = datetime.date(int(e.split('-')[0]),int(e.split('-')[1]),int(e.split('-')[2]))
    return range((end - begin).days+1)

def get(s,e):
    list0=[]
    for i in getRange(s,e):
        dateStr = str(datetime.date(int(s.split('-')[0]),int(s.split('-')[1]),int(s.split('-')[2]))+datetime.timedelta(days=i)).replace('-','')
        for n in range(2,1000):
            hz='%s%s'%(dateStr,get3(n))
            id0="441622"+hz
            id0='g'+id0+getX(id0)
            #print(hz)
            html=urlopen('http://www.lcyzczb.com/cjcx/edut_student_1.asp?id='+id0).read().decode('gb18030')
            if html.find(id0.upper())>-1:
                print(id0)
                list0.append(id0)
    return list0

print(get('2000-1-1','2000-1-1'))
