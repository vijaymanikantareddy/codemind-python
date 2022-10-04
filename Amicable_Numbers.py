
def fun(a,b):
    asum=0
    bsum=0
    for i in range(1,a//2+1):
        if a%i==0:
            asum+=i
    for i in range(1, b//2+1):
        if b%i==0:
            bsum+=i
    return asum==b and bsum==a

a = int(input())
b = int(input())
if fun(a,b):
    print("Amicable")
else:
    print("Not Amicable")