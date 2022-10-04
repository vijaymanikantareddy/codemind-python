import math
def fun(n):
    if n==0 or n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
a = int(input())
if fun(a):
    if(fun(int(str(a)[::-1]))):
        print("circular prime")
    else:
        print('prime but not a circular prime')
else:
    print("not prime")