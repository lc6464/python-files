def epi(number):
    """乘Π（3.1415926）"""
    try:
        num=float(number)
    except ValueError:
        print('输入错误！请输入数字！')
        return('ValueError!')
    ds=num*3.1415926
    return(ds)

def epi_s(number):
    """静默乘Π（3.1415926），无print。"""
    try:
        num=float(number)
    except ValueError:
        return('ValueError!')
    ds=num*3.1415926
    return(ds)

def Sy(r):
    """静默用半径计算圆的面积（Π取3.14）"""
    try:
        r=float(r)
    except ValueError:
        return('ValueError!')
    r=r**2
    ds=r*3.14
    return(ds)

if __name__ == '__main__':
    print('epi:%s' % epi.__doc__)
    print('epi_s:%s' % epi_s.__doc__)
    print('Sy:%s' % Sy.__doc__)
