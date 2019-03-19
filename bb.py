from math import log

def t(n):
    if n<=1:
        return 1
    return t(n/5)+t(4*n/5)+n


def s(n):
    return log(n,2)


def nstd(n):
    i=0
    cnt=0
    while i<n:
        j=1
        while j<i:
            cnt+=1
            j*=2
        i*=2
    return cnt



for i in range(1,10000):
   print(i," ",nstd(i)," ",nstd(i)/(i*i*i))


n=100000000
print(s(100000*n)/s(n))
