import random
secret = random.randint(0,9)#随机给出正确答案
print('------------------程序加载成功！------------------')
temp = input("猜一下我现在心里想的是哪个数字（是一个数字哦！）：")#获取输入内容
while True:
    while not (temp.isdigit() and len(temp) == 1):#判断输入内容类型及长度是否符合条件，不符合则循环
        if not temp.isdigit():#判断数据类型是否出错
            temp = input("输入数据类型错误，请重新输入：")
        elif len(temp) != 1:#判断数据长度是否出错
            temp = input("输入数据长度错误，请重新输入：") 
    guess = int(temp)
    if guess == secret:#判断输入内容是否正确
        print("我靠，你是作者心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
        break#正确时处理方式
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")        
        temp = input("哎呀，猜错了，请重新输入吧：")#错误时处理方式
print("游戏结束，不玩啦^_^")
print('---------------------END---------------------')
