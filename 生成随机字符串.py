def rStr(n):
    "生成包含数字和 ASCII 32~126 的随机字符串。"
    from random import choice
    l=list(range(32,127))
    s=''
    for i in range(0,n):
        r=choice(l)
        s+='%c'%r if r > 10 else str(r)
    return s

if __name__=="__main__":
    print(help(rStr))
    print(rStr(500))
