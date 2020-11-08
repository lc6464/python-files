def getX(Id):
    return '10X98765432'[sum(map(lambda x:int(x[0])*x[1],zip(Id[0:17],[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2])))%11]
