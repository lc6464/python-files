#程序员请认真阅读说明！！！
ZQDA = 6#正确答案
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
    
    if PDZ == ZQDA:
        print("对啦！！！")
        print("不过猜对了也没奖励。")
    elif int(UG) > ZQDA: 
        print("大了大了！！！")
    else:
        print("小了小了！！！")
print("对啦！！！")
print("好了，游戏结束，不玩了。")
