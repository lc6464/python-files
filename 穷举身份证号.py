from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from typing import Union
import datetime
from bs4 import BeautifulSoup as bs


def CheckCode(id17):
    return '10X98765432'[sum(map(lambda x: int(x[0]) * x[1], zip(id17[0:17], [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]))) % 11]


def GetDateRange(start, stop, step=1):
    begin = datetime.date(
        int(start.split('-')[0]), int(start.split('-')[1]), int(start.split('-')[2]))
    stop = datetime.date(
        int(stop.split('-')[0]), int(stop.split('-')[1]), int(stop.split('-')[2]))
    dates = []
    for i in range(0, (stop - begin).days, step):
        dates.append(str(datetime.date(int(start.split('-')[0]), int(start.split('-')[1]), int(
            start.split('-')[2]))+datetime.timedelta(days=i)).replace('-', ''))
    return dates


def GetStudentData(id: Union[str, list]):
    def Get(id: str):
        res = urlopen(
            'http://www.lcyzczb.com/cjcx/edut_student_1.asp?id=g%s' % id)
        result = res.read().decode('gb18030', 'ignore')
        if result.find('<script>alert("不存在该ID的学生");window.history.go(-1);</script>') > -1:
            return False
        else:
            soup = bs(result, 'lxml')
            def getValue(selector): return soup.select(
                selector)[0].attrs['value']
            data = {}
            data['name'] = getValue('#sname')
            data['ID'] = getValue('#sid').upper()
            data['class'] = getValue('#cla_id').replace(
                '(', '（').replace(')', '）') + '班'
            data['student_ID'] = getValue('#ksh')
            return data
    if isinstance(id, list):
        result = []
        for i in id:
            result.append(Get(i))
        return result
    else:
        return Get(id)


def GetByDate(start: str, stop: str, sex: Union[int, None] = None):
    """穷举的范围包括 start 但不包括 stop，均为日期，格式为 YYYY-m-d；sex 传入 0 为不指定，1 为男，2 为女。"""
    if sex == None:
        sex = 0
    elif sex not in [0, 1, 2]:
        raise Exception('性别指定错误！')
    students = []
    for date in GetDateRange(start, stop):
        for n in range((1 if sex == 1 else 0), 1000, (1 if sex == 0 else 2)):
            id17 = "441622%s%s" % (date, str(n).zfill(3))
            id = id17 + CheckCode(id17)
            try:
                data = GetStudentData(id)
                if data:
                    students.append(data)
                    print(data)
            except HTTPError as e:
                print('HTTPError', e)
                print('Error at', id)
            except URLError as e:
                print('URLError', e)
                print('Error at', id)
            except Exception as e:
                print('Error', e)
                print('Error at', id)
    return students


# print(GetByDate('2000-1-1', '2000-1-2'))
