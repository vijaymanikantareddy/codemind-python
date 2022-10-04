import math
def isprime(n):
    if n==0 or n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def fun(n):
    for i in range(2, n//2):
        if isprime(i) and isprime(n//i) and i*(n//i)==n:
            return {i,n//i}
    return {-1}

n = int(input())
for i in fun(n):
    print(i, end=' ')