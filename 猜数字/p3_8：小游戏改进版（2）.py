#程序员请认真阅读说明！！！
#此版本新增防泄露答案功能（答案每次自动随机给出）。
import random
ZQDA = random.randint(0,10)#正确答案自动随机给出
print("-----第一个小游戏-----")
UG = int(input("猜一下我心里想着什么数字（请不要输入文本！！！）："))
PDZ = int(UG)
while PDZ != ZQDA:
    if int(UG) > ZQDA: 
        print("大了大了！！！")
    else:
        print("小了小了！！！")
    UG = input("错了。重新猜一次吧：")
    PDZ = int(UG)
    
    if int(PDZ)== int(ZQDA):
        print("对啦！！！")
        print("不过猜对了也没奖励。")
    elif int(UG) > int(ZQDA): 
        print("大了大了！！！")
    else:
        print("小了小了！！！")
print("对啦！！！")
print("好了，游戏结束，不玩了。")
