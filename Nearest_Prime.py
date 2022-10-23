import math
def isprime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def near(n):
    if isprime(n):
        return n
    l = n-1
    r = n+1
    while(True):
        if isprime(l):
            return l
        if isprime(r):
            return r
        l-=1
        r+=1
n = int(input())
for i in range(n):
    a = int(input())
    print(near(a))