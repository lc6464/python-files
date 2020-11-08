from random import randint
secret = randint(0,9)
print('------------------程序加载成功！------------------')
temp = input("猜一下我现在心里想的是哪个数字（是一个数字哦！）：")
t = 1
while True:
    while not (temp.isdigit() and len(temp) == 1):
        try:
            guess = int(temp)
        except:
            temp = input("输入数据类型错误！请重新输入：")
        if not (0<=guess<=9):
            temp = input("输入数据长度错误！请重新输入：")
    guess = int(temp)
    if guess == secret:
        if t == 1:
            print('我靠，你是作者心里的蛔虫吗？！一次就中！')
        else:
            number = str(t)
            print('你共猜了'+number+'次就猜对了！')
        print("不过，猜中了也没有奖励！")
        break
    else:
        t += 1
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        temp = input("请重新输入吧：")
print("游戏结束，不玩啦^_^")
print('---------------------END---------------------')
input()
