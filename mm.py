from math import log,pow

def t(n):
    if n==1:
        return 2
    return t(n-1)*t(n-1)


def s(n):
    return sum(log(t(i),2) for i in range(1,int(log(n,2))))


def s2(n):
    if n<=2:
        return 2
    return s2(n/2)+n/2


def cont2(n):
    return pow(2,int(log(n,2)))


for i in range(1,1000):
    print(i,"",cont2(i))




for i in range(1,1):
    print(i," " ,s(i))
    print(i," ",s2(i))
