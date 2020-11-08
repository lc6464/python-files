import turtle

xiaowang = turtle.Turtle()

#====================移动函数====================
def move(x,y):
    xiaowang.penup()
    xiaowang.goto(x,y)
    xiaowang.pendown()
#======================end======================

#=====================画星星=====================
def drawStar(direction,size):
    xiaowang.pencolor("yellow")
    xiaowang.fillcolor("yellow")
    xiaowang.seth(direction)
    xiaowang.begin_fill()
    for j in range(5):
        xiaowang.forward(size)
        xiaowang.right(144)
    xiaowang.end_fill()
#======================end======================

#====================画旗面=====================
move(20 * -12,20 * 8)

xiaowang.pencolor("red")

xiaowang.fillcolor("red")
xiaowang.begin_fill()

for i in range(2):    #循环两次 画国旗底面
    xiaowang.forward(20*24)
    xiaowang.right(90)
    xiaowang.forward(20*16)
    xiaowang.right(90)
xiaowang.end_fill()
#======================end======================

#====================画星星====================

#大号星星
move(20 * -10,20 * 4)
drawStar(0,20 * 4)
#end

#右上星星
move(20 * -3,20 * 6.5)
drawStar(350,20 * 2)
#end

#中上星星
move(20 * -1,20 * 4)
drawStar(25,20 * 2)
#end

#中下星星
move(20 * -1,20 * 1.3)
drawStar(0,20 * 2)
#end

#右下星星
move(20 * -3,20 * -0.2)
drawStar(350,20 * 2)
#end

#====================写上文字====================
move(20 * -10,20 * 10)
xiaowang.pencolor("red")
xiaowang.write("武汉加油！中国加油！",font = ("楷体",40,"normal"))
#======================end======================

turtle.done()
