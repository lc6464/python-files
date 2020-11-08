import random
a = ''#新建变量
while True:
    guess = random.randint(1, 3)#随机生成数字
    while True:
        ask = input('1石头,2剪刀,3布\n请输入数字:')#a.读取用户输入
        if (ask in '123') and (len(ask) == 1):#a
            ask = int(ask)#a
            break#a
        else:#a-1.判断是否输入错误
            print('输入错误,请重新输入：')#a-1
            continue#a-1
    
    gus = ['石头', '剪刀', '布']#电脑可选项目
    if guess == 1:#判断+电脑选择
        print('电脑出了%s,你出的是%s，\n你赢了！' % (gus[ask-3], gus[ask-1]))
    elif guess == 2:
        print('电脑出了%s,你出的是%s，\n你输了！' % (gus[ask-2], gus[ask-1]))
    else:
        print('电脑出了%s,你出的是%s，\n平局。' % (gus[ask-1], gus[ask-1]))
    a = str(input('按回车键继续，按其他字母，数字或空格键位后按回车键退出。'))
    if a == '':#判断是否继续
        continue
    else:
        break
print('好玩吗？好玩就支持下吧！')
