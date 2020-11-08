#主函数
#整个游戏的地图结构，以及各个城市的参数
class city():
    def __init__(self,city_name):
        self.name=city_name
        if city_name=='长沙':
            self.seat=[0]
            self.city_way=3
        elif city_name=='桂林':
            self.city_way=1#cost_way的意思是收费方式是按照加法
            self.seat=[1]
            self.price=1800
            self.cost_0=100
            self.cost_1=500
            self.cost_2=1000
            self.cost_3=3000
        elif city_name=='苏州':
            self.city_way=1
            self.seat=[2]
            self.price=2400
            self.cost_0=200
            self.cost_1=700
            self.cost_2=1500
            self.cost_3=4000
        elif city_name=='火车站':
            #火车站的技能
            self.city_way=3
            self.cost_way=0#火车站的收费方式
            self.seat=[3]
            self.price=3000
        elif city_name=='天津':
            self.city_way=1
            self.price=2400
            self.seat=[4]
            self.cost_0=200
            self.cost_1=700
            self.cost_2=1500
            self.cost_3=4000
        elif city_name=='安阳':
            self.seat=[5]
            self.city_way=1
            self.price=2200
            self.cost_0=200
            self.cost_1=600
            self.cost_2=1500
            self.cost_3=3500
        elif city_name=='洛阳':
            self.seat=[6]
            self.city_way=2#收费方式按照乘法计算
            self.price=3000
            self.cost_0=2
            self.cost_1=3
            self.cost_2=4
            self.cost_3=5
        elif city_name=='古玩市场':
            self.seat=[7]#到达了古玩市场，古玩市场的技能
            self.city_way=3#古玩市场的收费方式
            self.price=3000
            self.city_way=3

        elif city_name=='揽金阁':#揽金阁的收费方式
            self.seat=[8,9]
            self.city_way=1
            self.price=5000
            self.cost_0=400
            self.cost_1=1000
            self.cost_2=2000
            self.cost_3=4500
        elif city_name=='郑州':
            self.seat=[10]
            self.price=3000
            self.city_way=1
            self.cost_0=300
            self.cost_1=900
            self.cost_2=2000
            self.cost_3=5000
        elif city_name=='盘口':#到达了盘口一号
            self.seat=[11]
            self.city_way=3
        elif city_name=='南京':
            self.seat=[12]
            self.city_way=1
            self.price=3000
            self.cost_0=300
            self.cost_1=900
            self.cost_2=2000
            self.cost_3=5000
        elif city_name=='广州':
            self.seat=[13]
            self.city_way=1
            self.price=3400
            self.cost_0=300
            self.cost_1=1000
            self.cost_2=2500
            self.cost_3=5500
        elif city_name=='杭州':
            self.city_way=3
            print('可以选择购买一个伙计，选择下一次移动的方向')
            self.seat=[14]
            self.seat_1=[26]
        elif city_name=='古墓':
            self.city_way=3
            self.seat=[15,16,18,19,21,22,24,25]#到达古墓的选择方式
        elif city_name=='长安':
            self.seat=[17]
            self.seat_1=[23]
            self.city_way=2#收费方式按照乘法计算
            self.price=3000
            self.cost_0=2
            self.cost_1=3
            self.cost_2=4
            self.cost_3=5
        elif city_name=='关隘':
            self.city_way=3
            self.seat=[20]
            self.seat_1=[20]#到达关隘可以直接移动到文物局
        elif city_name=='栈道':
            self.city_way=3
            self.seat=[23]
            self.seat_1=[17]#到达栈道的选择方式
        elif city_name=='上海':
            self.seat=[27]
            self.city_way=1
            self.price=4000
            self.cost_0=400
            self.cost_1=1200
            self.cost_2=3000
            self.cost_3=7000
        elif city_name=='成都':
            self.seat=[28]
            self.city_way=1
            self.price=3800
            self.cost_0=300
            self.cost_1=1100
            self.cost_2=2500
            self.cost_3=6500
        elif city_name=='合肥':
            self.seat=[29]
            self.city_way=1
            self.price=3800
            self.cost_0=300
            self.cost_1=1100
            self.cost_2=2500
            self.cost_3=6500
        elif city_name=='酒楼':#到达酒楼的处理方式
            self.seat=[30]
            self.price=3000
            self.city_way=3
        elif city_name=='珍宝堂':#珍宝堂的收费方式
            self.seat=[31,32]
            self.city_way=1
            self.price=5800
            self.cost_0=400
            self.cost_1=1200
            self.cost_2=2500
            self.cost_3=5500
        elif city_name=='燕京':
            self.seat=[33]
            self.city_way=2#收费方式按照乘法计算
            self.price=3000
            self.cost_0=2
            self.cost_1=3
            self.cost_2=4
            self.cost_3=5
        elif city_name=='文物局':
            self.seat=[34]#到了文物局的方法
            self.city_way=3
        elif city_name=='济南':
            self.seat=[35]
            self.city_way=1
            self.price=2700
            self.cost_0=200
            self.cost_1=800
            self.cost_2=2000
            self.cost_3=4500
        elif city_name=='襄阳':
            self.seat=[36]
            self.city_way=1
            self.price=2700
            self.cost_0=200
            self.cost_1=800
            self.cost_2=2000
            self.cost_3=4500
        elif city_name=='盘口二号':#到达了盘口二号
            self.seat=[37]
            self.city_way=3
        elif city_name=='长春':
            self.seat=[38]
            self.city_way=1
            self.price=2300
            self.cost_0=200
            self.cost_1=600
            self.cost_2=1500
            self.cost_3=3500
        elif city_name=='金陵':
            self.seat=[39]
            self.city_way=2#收费方式按照乘法计算
            self.price=3000
            self.cost_0=2
            self.cost_1=3
            self.cost_2=4
            self.cost_3=5
        
            
#各种古董卡片
class curio():
    def __init__(self,curio_name):
        self.name=curio_name
        if self.name=='碎片':
            self.price=200
            self.number=7
            self.sd=2#表示摇到多大可以带走
        elif self.name=='瓷器':
            self.price=500
            self.number=6
            self.sd=3
        elif self.name=='石像':
            self.price=1000
            self.number=5
            self.sd=4
        elif self.name=='古籍':
            self.price=1500
            self.number=3
            self.sd=5
        elif self.name=='珠宝':
            self.price=2000
            self.number=2
            self.sd=6
        elif self.name=='灵器':
            self.price=3000
            self.number=1
            self.sd=7
       
    
            
            
#各种伙计的数量
class mate():
    def __init__(self,mate_name):
        self.name=mate_name
        if self.name=='卦师':
            self.number=2
            self.price=1000
        elif self.name=='探险队员':
            self.number=4
            self.price=1000
        elif self.name=='土夫子':
            self.number=1
            self.price=1000
        elif self.name=='山村村长':
            self.number=1
            self.price=1000
        elif self.name=='无效伙计':
            self.number=0
            self.price=1000

import random
#产生随机数
def run():
    return random.randint(1,6)
#定义的是各种玩家
class gamer():
    def __init__(self,gamer_name):
        self.gamer_name=gamer_name
        self.seat=0#保存每个玩家到达的位置
        self.money=20000
        self.city=[]
        self.mate=[]#每个玩家伙计的数量
        self.curio=[]#玩家的古董
#定义一个列表，存储每个城市到达的等级
city_grade={'桂林':0,'苏州':0,'天津':0,'火车站':0,'安阳':0,'洛阳':0,'揽金阁':0,'古玩市场':0,'郑州':0,'南京':0,'广州':0,'长安':0,'上海':0,'成都':0,'合肥':0,'酒楼':0,'珍宝堂':0,'燕京':0,'济南':0,'襄阳':0,'长春':0,'金陵':0}

gamer_1=gamer('老虎')
gamer_2=gamer('兔子')
gamer_3=gamer('小猫')
gamer_4=gamer('黄鼠狼')
gamer_number=4#玩家的数量
list2=[]
list3=[]
list4=[]
n2=0
#找出玩家所有的产业对应的价值
def all_money(gamer):
    #地产的价值
    city_value=0
    list2=gamer.city
    #print(list2)
    for i in list2:
        aa=city(i)
        city_value=city_value+aa.price
    #古董的价值
    list3=gamer.curio
    curio_value=0
    for i in list3:
        bb=curio(i)
        curio_value=curio_value+bb.price
    mate_value=0
    list4=gamer.mate
    #print(list4)
    for i in list4:#---------------------------------------i代表财产名字
        cc=mate(i)
        #print(i2)
        mate_value=mate_value+cc.price
    all_value=gamer.money+city_value+curio_value+mate_value
    return all_value
all_city=['长沙','桂林','苏州','火车站','天津','安阳','洛阳','古玩市场','揽金阁','揽金阁','郑州','盘口','南京','广州','杭州','古墓','古墓','长安','古墓','古墓','关隘','古墓','古墓','栈道','古墓','古墓','杭州''上海','成都','合肥','酒楼','珍宝堂','珍宝堂','燕京','文物局','济南','襄阳','盘口','长春','金陵','长沙']
#定义银行的房产数量
bank_city=['桂林','苏州','火车站','天津','安阳','洛阳','古玩市场','揽金阁','郑州','南京','广州','长安','上海','成都','合肥','酒楼','珍宝堂','燕京','济南','襄阳','长春','金陵']
bank_curio=['碎片','碎片','碎片','碎片','碎片','瓷器','瓷器','瓷器','瓷器','瓷器','碎片','碎片','灵器','瓷器','珠宝','珠宝','古籍','古籍','古籍','石像','石像','石像','石像','石像']
#得到应该抵押哪个财产
def mortgage(gamer):
    all_get=gamer.city+gamer.curio+gamer.mate#所有财产的列表
    #n=len(all_get)
    n=random.sample(all_get,1)#得到应该抵押的财产对应的位置
    mor_city=all_get(n)#得到应该抵押的财产名称
    return mor_city
    
list_mate=['土夫子','探险队员','探险队员','探险队员','探险队员','山村村长','卦师','卦师']   #伙计列表 
    
other_gamer_citys=[]    
k=1
x1=0
while k:
    #判断是否有玩家达到了40000元，或者其他玩家全部破产
    if all_money(gamer_1)>=40000:
        print('最终的胜利者是：')
        print('gamer_1:老虎')
        break
    elif all_money(gamer_2)>=40000:
        print('最终的胜利者是：')
        print('gamer_2:兔子')
        break
    elif all_money(gamer_3)>=40000:
        print('最终的胜利者是：')
        print('gamer_3:小猫')
        break
    elif all_money(gamer_4)>=40000:
        print('最终的胜利者是：')
        print("gamer_4:黄鼠狼")
        break
    gamers=[gamer_1,gamer_2,gamer_3,gamer_4]
    
    for f in range(1,5):
        #print('f=')
        #print(f)
        if f==1:
            i=gamer_1
            other_gamer=[gamer_2,gamer_3,gamer_4]
        elif f==2:
            i=gamer_2
            other_gamer=[gamer_1,gamer_3,gamer_4]
        elif f==3:
            i=gamer_3
            other_gamer=[gamer_1,gamer_2,gamer_4]
        elif f==4:
            i=gamer_4
            other_gamer=[gamer_1,gamer_2,gamer_3]
        #print(other_gamer)
        x1=x1+1
        if x1%5==0:
            #print('请输入0或1')
            #x3=input('是否继续')
            print('这个回合的战斗结果，各个玩家的财产')
            print('老虎的全部财产:',end="")
            print(all_money(gamer_1),end="")
            print(gamer_1.city)
            print('兔子的全部财产:',end="")
            print(all_money(gamer_2),end="")
            print(gamer_2.city)
            print('小猫的全部财产:',end="")
            print(all_money(gamer_3),end="")
            print(gamer_3.city)
            print('黄鼠狼的全部财产:',end="")
            print(all_money(gamer_4),end="")
            print(gamer_4.city)
        x=run()#玩家投掷一次骰子
        #print('i=')
        #print(i)
        gamers=[gamer_1,gamer_2,gamer_3,gamer_4]
        #other_gamer=gamers.remove(i)#其他的玩家
        #print(other_gamer)
        #print(type(i.seat))
        #print(type(x))
        i.seat=i.seat+x
        #print('拥有伙计的数量')
        #print(i.mate)
        if i.seat>40:
            i.seat=i.seat-40
            i.money=i.money+2000#经过起点，奖励两千元
        elif i.seat==40:#直接到达起点的情况
            i.seat=i.seat-40
            #买一个伙计
            if len(list_mate)>0:
                the_mate=list_mate[0]
                i.money=i.money-1000
                i.mate.append(the_mate)#伙计变多
                list_mate.remove(the_mate)
        elif i.seat==14 or i.seat==26:#到达杭州的情况
            if len(list_mate)>0:
                the_mate=list_mate[0]
                i.money=i.money-1000
                i.mate.append(the_mate)#伙计变多
                list_mate.remove(the_mate)
            #买一个伙计
            '''the_mate=list_mate[0]
            i.money=i.money-1000
            i.mate.append(the_mate)#伙计变多
            list_mate.remove(the_mate)'''
        elif i.seat==23:#到达栈道的情况
            #丢失一个伙计
            #the_mate=random.sample(list_mate,1)
            if len(i.mate)>0:
                del i.mate[0]#-------------------------
            else:
                i.money=i.money-1200
        elif i.seat==20:
            i.seat=34#从关隘直接到达文物局
            if '碎片' in i.curio:
                i.curio.remove('碎片')
                i.money=i.money+1000
                bank_curio.append('碎片')#银行的古董+1
        elif i.seat==34:
            if '碎片' in i.curio:
                i.curio.remove('碎片')
                i.money=i.money+1000
                bank_curio.append('碎片')#银行的古董+1
        #到达火车站的情况
        elif i.seat==3:#产生0到100的随机数
            if random.randint(1,100)>50:
                i.seat=13
                i.money=i.money-1000
            else:
                pass
        #到达古玩市场的情况
        elif i.seat==7:
            if random.randint(1,100)>30 and len(bank_curio)>0:
                #length=len(bank_curio)
                #n=random.randint(0,length)#n代表要买的古董对应的位置?????????
                curio_name=bank_curio[0]
                bank_curio.remove(curio_name)
                i.curio.append(curio_name)
                curio_now=curio(curio_name)#要买的古董的实例化对象
                i.money=i.money-curio_now.price
        #到达盘口之后的情况,
        elif i.seat==11:
            n=run()
            if '探险队员' in i.mate:
                n=n+1
            for j in other_gamer:
                curio_1=j.curio#这个玩家的全部古董列表
                for c in curio_1:
                    c_name=curio(c)#此古董的实例化对象
                    if c_name.sd==n or c_name.sd==n-1:
                        j.curio.remove(c)
                        i.curio.append(c)
        elif i.seat==37:
            n=run()
            for j in other_gamer:
                curio_1=j.curio#这个玩家的全部古董列表
                for c in curio_1:
                    c_name=curio(c)#此古董的实例化对象
                    if c_name.sd==n:
                        j.curio.remove(c)
                        i.curio.append(c)
        #到达古墓后的情况
        elif i.seat==15 or i.seat==16 or i.seat==18 or i.seat==19 or i.seat==21 or i.seat==22 or i.seat==24 or i.seat==25:
            n1=run()
            if '卦师' in i.mate:
                n2=run()
            
            if '探险队员' in i.mate:
                n1=n1+1
            n1=max(n1,n2)
            #length=len(bank_curio)
            #n=random.randint(0,length-1)
            #n_name=bank_curio[0]
            #n_curio=curio(n_name)#该古董的实例化对象
            #print('古董的名称')
            #print(n_name)
            #print(n_curio)
            #print(n_curio.sd)
            if len(bank_curio)>0:
                n_name=bank_curio[0]
                n_curio=curio(n_name)#该古董的实例化对象 
                if n1>=n_curio.sd:#------------++++++++++++++++++++++
                    bank_curio.remove(n_name)
                    i.curio.append(n_name)
            #向有村长的玩家交钱
            for k in other_gamer:
                if '山村村长' in k.curio:
                    k.money=k.money+200
                    i.money=i.money-200
        #到达普通城市后的情况
        #print(i.seat)
        now_city1=all_city[i.seat]#该位置对应的城市名称#----------------------
        if now_city1 in i.city:
            pass
        else:
            #print(type(other_gamer))
            #得到其他玩家手中的城市列表
            other_gamer_citys=other_gamer[0].city+other_gamer[1].city+other_gamer[2].city
            #如果城市已经被其他玩家购买
            if now_city1 in other_gamer_citys:
                #找出这个玩家
                if now_city1 in other_gamer[0].city:
                    x=other_gamer[0]
                elif now_city1 in other_gamer[1].city:
                    x=other_gamer[1]
                elif now_city1 in other_gamer[2].city:
                    x=other_gamer[2]
            #for x in other_gamer:#此处有错误----------------------不能迭代
                    #x是该城市主人的实例化对象
                if now_city1 in x.city:#==================>>>>>>>>>>>>>>>>>>>>.
                    now_city2=city(now_city1)#该城市的实例化对象
                    if city_grade[now_city1]<3 and len(x.curio)>0:
                        city_grade[now_city1]=city_grade[now_city1]+1
                        now_name3=x.curio[0]#要卖的古董的名称
                        curio_0=curio(now_name3)#要卖的古董的实例化对象
                        #print(curio_0)
                        curio_price1=curio_0.price#----------------------------
                        i.money=i.money-curio_price1
                        x.money=x.money+curio_price1
                        i.curio.insert(1,now_name3)#玩家i得到古董，x失去古董
                        x.curio.remove(now_name3)
                    elif city_grade[now_city1]==3 and len(x.curio)>0:
                        #这一步是按照加法卖古董
                        #print(now_city1)
                        #print(now_city2.name)
                        if now_city2.city_way==1:
                            #curio_price1=now_city2.price+curio_0.cost_3
                            now_name4=x.curio[0]#要卖的古董的名称
                            curio_0=curio(now_name4)#要卖的古董的实例化对象
                            #print(now_name4)
                            curio_price1=curio_0.price+now_city2.cost_3
                            i.money=i.money-curio_price1
                            x.money=x.money+curio_price1
                            i.curio.insert(1,now_name4)#玩家i得到古董，x失去古董
                            x.curio.remove(now_name4)#//////////////////////////////////////////////////
                        #按照乘法卖古董
                        if now_city2.city_way==2:
                            now_name4=x.curio[0]#要卖的古董的名称
                            curio_0=curio(now_name4)#要卖的古董的实例化对象
                            curio_price1=curio_0.price*now_city2.cost_3
                            i.money=i.money-curio_price1
                            x.money=x.money+curio_price1
                            i.curio.insert(1,now_name4)#玩家i得到古董，x失去古董
                            x.curio.remove(now_name4)#/////////////////////////////////////////////////////
        if now_city1 in bank_city:
            
            if random.randint(1,10)>=4:
                
                #玩家购买这个城市
                #print(now_city1)
                city_now_ex=city(now_city1)#该城市的实例化对象
                price_now1=city_now_ex.price#--------------------------------------
                i.city.append(now_city1)
                bank_city.remove(now_city1)
                i.money=i.money-city_now_ex.price
        else:
            pass
