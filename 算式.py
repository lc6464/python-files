import re

def check(string):
    """
    检查输入算式的合法性
    """
    # step0:去空格
    string = re.sub("\s", "", string)
    #step1:检查非法字符
    res1 = re.search("[^\d()*+\-./]+", string)
    if res1 != None:return None,1, res1.group()
    #step2：检查括号
    checkString = re.sub("[^()]", "", string[:])
    while "()" in checkString:
        checkString = re.sub("\(\)", "", checkString)
    if checkString != "":return None,2, checkString
    #step3:检查算数运算符
    res3 = re.search("[-+/]{2,}|[*]{3,}", string)
    if res3 != None:return None,3, res3.group()
    #step4:检查左括号和算数运算符
    res4 = re.search("\([+*/]", string)
    if res4 != None:return None,4,res4.group()
    #step5:检查小数点
    res5 = re.search("([^\d]\.)|(\.{2,})|(\.[^\d])|(\.\d+\.)", string)
    if res5 != None:return None, 5, res5.group()
    return string

def string_to_num(string):
    """
    把用f表示的负数转换成真正的负数进行运算
    :param string:用f表示的负数字符串
    :return:负数非字符串表示
    """
    string = re.sub("f", "-", string)
    return int(string) if "." not in string else float(string)

def num_to_string(string):
    """
    把负数的-变成f以便于脱括号
    :param string:负数的非字符串表示
    :return:用f表示的负数(字符串)
    """
    string = re.sub("-", "f", str(string))
    return string

def myPower(string):
    """
    若一个字符串中间包含乘方，则计算乘方并替换
    """
    while True:
        parm = re.compile("(?P<first>f{0,1}[\d.]+)[*]{2}(?P<last>f{0,1}[\d.]+)")
        equation = re.search(parm, string)
        if equation == None:return string
        first, last = string_to_num(equation.group("first")), string_to_num(equation.group("last"))
        try:
            res = num_to_string(pow(first, last))
        except Exception as e:
            print("不支持复数运算:", e)
            exit()
        string = string.replace(equation.group(), res)

def multiplication_and_division(string):
    """
    计算乘法和除法
    """
    while True:
        parm = re.compile("(?P<first>f{0,1}[\d.]+)(?P<flag>[*/])(?P<last>f{0,1}[\d.]+)")
        equation = re.search(parm, string)
        if equation == None:return string
        first, flag, last = string_to_num(equation.group("first")), equation.group("flag"), string_to_num(equation.group("last"))
        res = first * last if flag=="*" else first/last
        res = num_to_string(res)
        string = string.replace(equation.group(), res)

def add_and_subtraction(string):
    """
    计算加法和减法
    """
    while True:
        parm = re.compile("(?P<first>f{0,1}[\d.]+)(?P<flag>[+\-])(?P<last>f{0,1}[\d.]+)")
        equation = re.search(parm, string)
        if equation == None:return string
        first, flag, last = string_to_num(equation.group("first")), equation.group("flag"), string_to_num(equation.group("last"))
        res = first + last if flag == "+" else first - last
        res = num_to_string(res)
        string = string.replace(equation.group(), res)

def compute(string):
    string = myPower(string)
    string = multiplication_and_division(string)
    string = add_and_subtraction(string)
    return string

def main(string):
    """
    step1:检查算式合法性
    step2:从内向外脱括号，优先级：乘方，乘除，加减
    step3：反复计算，直到没有括号，然后再算一次
    step4：最后转成数字
    """
    string = check(string)
    if isinstance(string, tuple):
        print("算式不合法,错误代码%d,在“%s”处存在错误."%(string[1], string[2]))
        exit()
    while True:
        parm = re.compile("\([^(]+\)")
        equation_k = re.search(parm, string)
        if equation_k == None:break
        equation = equation_k.group()[1:-1]
        equation2 = compute(equation)
        string = string.replace(equation_k.group(), equation2)
    string = compute(string)
    return string_to_num(string)

if __name__ == '__main__':
    string = "(3 + 1.5) * 8 ** 0.5 - 6 / 4"
    res = main(string)
    print(res)
