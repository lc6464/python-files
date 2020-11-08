import random
secret = random.randint(1,10)
print('------------------------------------')
temp = input("不妨猜一下我现在心里想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp = input("哎呀,猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("对啦！！！你是我心里的蛔虫吗？！！")
        print("不过，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("给个提示吧："/n + "大了大了!")
        else:
            print("给个提示吧："/n + "小了小了!")
print("游戏结束，不玩啦^_^")
